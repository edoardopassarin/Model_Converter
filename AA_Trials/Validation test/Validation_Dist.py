from AA_Trials.Tool_Codes.DigitalModel import DigitalModel
import json
import pandas as pd
from manpy.simulation import Globals
import statistics
import scipy.stats
import math
import matplotlib.pyplot as plt

directory_in = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Validation test/Arena/LEGO Model dist/Files/"
directory_out = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Validation test/Arena/LEGO Model dist/Output/"

with open("exec_model_validation.json") as f:
    in_data = json.load(f)

# distrM1 = "fixed"
# distrM2 = "fixed"
# paramM1 = [14.4]
# paramM2 = [16.4]
distrM1 = "triangular"
distrM2 = "triangular"
paramM1 = [12, 30, 24]
paramM2 = [12, 35, 19]

distr_dict = {
    "M1": [distrM1, paramM1],
    "M2": [distrM2, paramM2]
}
distr_table = pd.DataFrame(distr_dict)

initWIP = []
init_1 = 8
init_2 = 4
for i in range(init_1):
    initWIP.append(1)
for i in range(init_2):
    initWIP.append(2)
n_pallet = len(initWIP)

model = DigitalModel(in_data)
# model.ObjectList[0].unloadRng.mean += 4.4
print(model.ObjectList[0].unloadRng.mean)
# sim_time = 60*60*8
# n_replications = 5
# confid_level = 0.95
#
# results = model.runStochSimulation(distr_table, sim_time, n_replications, initWIP, 45)
#
# for obj in model.ObjectList:
#     print(obj)
# systime_list = results['elementList'][0]['results']['system_time_trace']
# print(systime_list[0])
# systime_list_mean = Globals.extract_mean_val(systime_list, 2)
# systime_stdev = statistics.stdev(systime_list_mean)
# print(systime_stdev)
# conf_interval_M = Globals.confidence_interval(systime_list_mean, confid_level)
# print(conf_interval_M)
# #
# out_data = pd.read_csv(directory_out + 'Validation_System_Time.txt', sep=" ", header=None)
# del out_data[2]
# del out_data[3]
# out_data.columns = ['Replication', 'System Time']
# grouped = out_data.groupby(['Replication'])
#
# Arena_mean = []
# for i in range(n_replications):
#     temp = grouped.get_group(float(i + 1))[n_pallet:]
#     temp = temp['System Time'].tolist()
#     Arena_mean.append(statistics.mean(temp))

# print(systime_list_mean)
# print(Arena_mean)
# Arena_stdev = statistics.stdev(Arena_mean)
# print(Arena_stdev)
# conf_interval_A = Globals.confidence_interval(Arena_mean, confid_level)
# print(conf_interval_A)

# CI for Arena-Manpy
# t_val = scipy.stats.t.ppf((1 + confid_level) / 2., n_replications - 1)
# var = [Arena_stdev**2, systime_stdev**2]
# mean_diff = conf_interval_A[0] - conf_interval_M[0]
# interval = math.sqrt(sum(var)/n_replications)*t_val
#
# CI_diff = [mean_diff-interval, mean_diff+interval]
# print(CI_diff)

