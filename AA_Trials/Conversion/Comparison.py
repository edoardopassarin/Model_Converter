import json
import pandas as pd
from AA_Trials.Tool_Codes.DigitalModel import DigitalModel
import statistics
from manpy.simulation import Globals
import scipy.stats
import math

# Files directories
dir_mod = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Conversion/Generated Models/"
dir_perf = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Conversion/Output/"

# Names of the different configurations
models_list = ['Flowline', 'MM1K', 'Simple Open', 'Parallel']
model = models_list[0]
print(f'Analysing model named: {model}\n')

# Load the executable model
with open(dir_mod + model + '/' + model + '_executable_final.json') as f:
    exec_model_temp = json.load(f)

exec_model = DigitalModel(exec_model_temp)

# Distributions dictionary

# FLOWLINE
distrM1 = "triangular"
distrM2 = "uniformSP"
distrM3 = "triangular"
distrM4 = "fixed"
distrM5 = "uniformSP"
distrM6 = "triangular"
paramM1 = [17, 23, 20]
paramM2 = [19, 2]
paramM3 = [16, 26, 18]
paramM4 = [20.5]
paramM5 = [18, 4]
paramM6 = [15, 25, 20]

distr_dict = {
    "M1": [distrM1, paramM1],
    "M2": [distrM2, paramM2],
    "M3": [distrM3, paramM3],
    "M4": [distrM4, paramM4],
    "M5": [distrM5, paramM5],
    "M6": [distrM6, paramM6]
}
distr_table = pd.DataFrame(distr_dict)


# PARALLEL
# distrM1 = "triangular"
# distrM2 = "uniformSP"
# distrM3 = "triangular"
# distrM4 = "uniformSP"
# distrM5 = "uniformSP"
# paramM1 = [28, 32, 30]
# paramM2 = [45, 10]
# paramM3 = [35, 55, 45]
# paramM4 = [40, 10]
# paramM5 = [24, 10]
#
# distr_dict = {
#     "M1": [distrM1, paramM1],
#     "M2": [distrM2, paramM2],
#     "M3": [distrM3, paramM3],
#     "M4": [distrM4, paramM4],
#     "M5": [distrM5, paramM5]
# }
# distr_table = pd.DataFrame(distr_dict)

# Run the simulation
confid_level = 0.95
sim_length = 60 * 60 * 24
replications = 5
results = exec_model.runStochSimulation(distr_table, sim_length, replications)
# results = exec_model.runStochSimulation(None, sim_length, replications)
intdep_list = results['elementList'][-1]['results']['intdep_list']
systime_list = results['elementList'][-1]['results']["systime_list"]
Manpy_mean_st = Globals.extract_mean_val(systime_list, 2)
Manpy_mean_id = Globals.extract_mean_val(intdep_list, 2)
Manpy_stdev_st = statistics.stdev(Manpy_mean_st)
Manpy_stdev_id = statistics.stdev(Manpy_mean_id)
Manpy_CI_st = Globals.confidence_interval(Manpy_mean_st, confid_level)
Manpy_CI_id = Globals.confidence_interval(Manpy_mean_id, confid_level)
print('\n\n+++ MANPY +++')
print(f'SYSTEM TIME\nmean= {Manpy_CI_st[0]}\nstdev= {Manpy_stdev_st}\nCI= {Manpy_CI_st[1:]}\n')
print(f'INTERDEPARTURE TIME\nmean= {Manpy_CI_id[0]}\nstdev= {Manpy_stdev_id}\nCI= {Manpy_CI_id[1:]}\n\n')


# Open the system time file
col_st = ['replication', 'time', 'value', 'temp']
systime_in = pd.read_csv(dir_perf + model + '/systime.txt', sep=" ", header=None, names=col_st)
del systime_in['temp']

# Open the interdeparture file
col_dp = ['replication', 'time', 'value', 'temp']
intdep_in = pd.read_csv(dir_perf + model + '/interdeparture.txt', sep=" ", header=None, names=col_dp)
del intdep_in['temp']

grouped_st = systime_in.groupby(['replication'])
Arena_mean_st = []
for i in range(replications):
    temp = grouped_st.get_group(float(i + 1))
    temp = temp['value'].tolist()
    Arena_mean_st.append(statistics.mean(temp))

grouped_id = intdep_in.groupby(['replication'])
Arena_mean_id = []
for i in range(replications):
    temp = grouped_id.get_group(float(i + 1))[1:]
    temp = temp['value'].tolist()
    Arena_mean_id.append(statistics.mean(temp))

Arena_stdev_st = statistics.stdev(Arena_mean_st)
Arena_stdev_id = statistics.stdev(Arena_mean_id)
Arena_CI_st = Globals.confidence_interval(Arena_mean_st, confid_level)
Arena_CI_id = Globals.confidence_interval(Arena_mean_id, confid_level)
print('+++ ARENA +++')
print(f'SYSTEM TIME\nmean= {Arena_CI_st[0]}\nstdev= {Arena_stdev_st}\nCI= {Arena_CI_st[1:]}\n')
print(f'INTERDEPARTURE TIME\nmean= {Arena_CI_id[0]}\nstdev= {Arena_stdev_id}\nCI= {Arena_CI_id[1:]}')

# CI for Arena-Manpy
t_val = scipy.stats.t.ppf((1 + confid_level) / 2., replications - 1)
var_st = [Arena_stdev_st**2, Manpy_stdev_st**2]
var_id = [Arena_stdev_id**2, Manpy_stdev_id**2]
mean_diff_st = Arena_CI_st[0] - Manpy_CI_st[0]
mean_diff_id = Arena_CI_id[0] - Manpy_CI_id[0]
interval_st = math.sqrt(sum(var_st)/replications)*t_val
interval_id = math.sqrt(sum(var_id)/replications)*t_val

CI_diff_st = [mean_diff_st-interval_st, mean_diff_st+interval_st]
CI_diff_id = [mean_diff_id-interval_id, mean_diff_id+interval_id]
print('\n\n+++DIFFERENCE ARENA-MANPY+++')
print(f'SYSTEM TIME\nmean= {mean_diff_st}\nCI= {CI_diff_st}\n')
print(f'INTERDEPARTURE TIME\nmean= {mean_diff_id}\nCI= {CI_diff_id}')
