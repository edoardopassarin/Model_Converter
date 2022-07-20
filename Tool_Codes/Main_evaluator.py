from Evaluator import Evaluator
from interface_DB import interface_DB
from DigitalModel import DigitalModel
import manpy.simulation.Globals as Globals
# import numpy as np
# import scipy.stats
# import math
# import json

# IP = "localhost"
# DB_name = "RTSimulatorDB"
# port = 8086
IP = "192.168.0.50"
DB_name = "RTSimulatorDB"
port = 8086
db = interface_DB(IP, DB_name, port)
time_interval = 20
# ciao = db.queryData("input", "history_validation_Eval")
# print(ciao)
# print(json.loads(ciao[1]['values'][0][2]))
# print(len(ciao))

config = {
    'len_demonstration': 70 * 60,       # length of the demonstration [sec]
    'time_disruption': 5 * 60,          # time after which we initiate the disruption
    'loop_delay': 20                     # delay of the cycle loop
}

evaluator = Evaluator(db, config)
evaluator.start()

# distr_new = db.queryData("proc_time", "distributions", t_query=2)   # 2 is the number of machine
# init_pos = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
# exec_model_temp = db.queryData("executable_model", "model")
# model = DigitalModel(exec_model_temp, 1)
# results = model.runStochSimulation(distr_new, 3600, 20, init_pos)
# # Extract the list with the average throughput for each replication
# intarr_list = results['elementList'][0]['results']['interarrival_trace']
# intarr_list_mean = Globals.extract_mean_val(intarr_list, 2)
# th_list = [1/x for x in intarr_list_mean]
# print(th_list)
# conf_interval
# = Globals.confidence_interval(th_list, 0.95)
# for it, val in enumerate(conf_interval):
#     conf_interval[it] = round(val * 3600, 1)
# print(conf_interval)


# =============================================================
# CHECK IF THE FUNCTION compare_th() WORKS -> IT DOES
# a = [15.5, 16.3, 17.8, 19.2, 15.9]
# b = [13.2, 12.9, 13.5, 14.8, 15.0]
#
# conf_a = Globals.confidence_interval(a, 0.95)
# conf_b = Globals.confidence_interval(b, 0.95)
#
# # print(conf_a)
# # print(conf_b)
#
# a_arr = 1.0 * np.array(a)
# n_a = len(a_arr)
# m_a, var_a = np.mean(a_arr), np.var(a_arr)
#
# b_arr = 1.0 * np.array(b)
# n_b = len(b_arr)
# m_b, var_b = np.mean(b_arr), np.var(b_arr)
#
# t_val = scipy.stats.t.ppf((1 + 0.95) / 2., n_a - 1)
#
# h_diff = math.sqrt(var_b/n_b + var_a/n_a)
# h_diff = t_val * h_diff
# m_diff = m_a - m_b
# conf_diff = [m_diff, m_diff - h_diff, m_diff + h_diff]
# print(conf_diff)
#
# mean_val = [conf_a[0], conf_b[0]]     # means of the two alternatives
# interval = [conf_a[2] - conf_a[0], conf_b[2] - conf_b[0]]   # intervals of the two alternatives
# se = [x/t_val for x in interval]        # squared error of the two alternatives
# se_sq = [pow(x, 2) for x in se]         # error of the two alternatives
# diff_mean = mean_val[0] - mean_val[1]    # difference of the means
# diff_interval = math.sqrt(se_sq[0] + se_sq[1])
# diff_interval = t_val * diff_interval       # new interval
# conf_diff_a = [diff_mean, diff_mean - diff_interval, diff_mean + diff_interval]
# print(conf_diff_a)

# =============================================================
# conf_inter = [0.075862, 0.074956, 0.076249]
# for it, val in enumerate(conf_inter):
#     conf_inter[it] = round(val*3600, 2)
#
# print(conf_inter)
