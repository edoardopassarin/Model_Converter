from AA_Trials.Tool_Codes.ModelConverter import ModelConverter
from AA_Trials.Tool_Codes.DigitalModel import DigitalModel
from AA_Trials.Tool_Codes.interface_DB import interface_DB
import manpy.simulation.Globals as Globals
import pickle
import json
import pandas as pd

path_IN = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Input Files/"
path_OUT = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Output Files/"
#
with open(path_IN + 'Generated_model.json') as f:
    in_data = json.load(f)              # Save the content of the JSON file into a dict variable

print(in_data)
# unload_time = 3.2
# conv_time = 10.66
# print(round(conv_time))

# config_file = {
#     'start': 'M1',
#     'unloadTime': 3.2,
#     'transportationTime': 15,
#     'transportationCap': 2,
#     'queueCap': {
#         'Q1': 8,
#         'Q2': 7,
#     }
# }
# queue = config_file['queueCap']
# for q, c in queue.items():
#     print(q)
#     print(c)
# print(config_file)
# graph_model = ModelConverter(in_data, config_file)
graph_model = ModelConverter(in_data)
# print(graph_model.unloadTime)
exec_model_temp = graph_model.convertModel()
# print(exec_model_temp)
# with open(path_OUT + 'conversion_open.json', 'w') as f:
#     json.dump(exec_model_temp, f, indent=4)
# exec_model_temp['graph']['node']['M1'].update({"gatherSysTime": 1, "gatherIntArr": 1})
# print(exec_model_temp['graph']['node']['M1'])
exec_model = DigitalModel(exec_model_temp, 1)
print(exec_model)
# for i in exec_model.ObjectList:
#     print(i)

# ============================================================================

# with open(path_IN + 'Static_model.json') as f:
#     in_data = json.load(f)

# print(in_data)
# initWIP = [2, 2, 2, 1, 1, 1]
# processing_dict = {
#     "M1": pd.Series([6.0, 6.0, 6.0, 7.0, 8.0, 10.0, 9.0]),
#     "M2": pd.Series([8.0, 8.0, 8.0, 9.0, 8.0, 7.0, 10.0]),
# }
# processing = pd.DataFrame(processing_dict)
# print(processing.iloc[:, 1])

# exec_model = DigitalModel(in_data, 1)
# print(exec_model)
# for obj in exec_model.ObjectList:
#     print(obj)
# results = exec_model.runTraceSimulation(processing, initWIP)
# print(results)
# # print(results['elementList'][0]['id'] == 'M1')
# # for i, a in enumerate(results['elementList']):
# #     print(results['elementList'][i]['id'])
# print(results['elementList'][1])
# print(results['elementList'][0])
#
# print(exec_model.numOfWIP)

# eventlog = results["eventlog"]
# print(eventlog)

# print(results)
# print(exec_model.numOfWIP)

# intarr_list = results['elementList'][0]['results']['interarrival_trace'][0]
# print(intarr_list)

# systime_list = results['elementList'][0]['results']['system_time_trace'][0]
# print(systime_list)

# ===============================================================================

IP = "localhost"
DB_name = "RTSimulatorDB"
port = 8086
database = interface_DB(IP, DB_name, port)

# database.writeData("system_time_digital", "digital_perf", results)


# import pickle
#
# with open(r"System_time_digital_test_edo", mode="wb") as Processing_time:
#     pickle.dump(test, Processing_time)
#
#     Processing_time.close()

# a = [[], []]
# a[0].append(1)
# a[0].append(2)
# print(a)

# systime_list = results['elementList'][0]['results']['system_time_trace'][0]
# print(systime_list)
# timelog_list = []
# for i in range(len(systime_list)):
#     timelog_list.append(systime_list[i][0])
#
# print(timelog_list)
#
# systime_dict = {
#                     "activity": 1,          # TO FIX, INSERT THE ACTIVITY IN THE INPUT DICT result
#                     "replication": 1,       # TO FIX, INSERT THE REPLICATION IN THE INPUT DICT result
#                     "simulator_id": 1,      # TO FIX, INSERT THE SIMULATOR ID IN THE INPUT DICT result
#                     "timelog": pd.Series(timelog_list),
#                 }
# df = pd.DataFrame(systime_dict)
# print(df)
# systime_list = systime_list[exec_model.numOfWIP:]       # removed the first measures with the number of WIP
# print(systime_list)

# ==================================================================================
# infile = open("C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Input Files/eventlog_acquisition_test1", 'rb')
# eventlog = pickle.load(infile)
# infile.close()
# eventlog = eventlog.drop(0)
# print(eventlog)
# eventlog.to_csv("C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Output Files/eventlog.csv")

# ==================================================================================

# distrM1 = "normalSP"
# distrM2 = "gammaSP"
# paramM1 = [5, 4]
# paramM2 = [1, 3, 20]
#
# distr_dict = {
#     "M1": [distrM1, paramM1],
#     "M2": [distrM2, paramM2]
# }
# distr_table = pd.DataFrame(distr_dict)
# print(distr_table)
# distr_out = {"processingTime": {}}
# temp_dict = {"Gamma": {
#             "alpha": paramM2[0],
#             "beta": paramM2[1]
#         }}
# distr_out['processingTime'].update(temp_dict)
# print(distr_out)

# # ==================================================================================
# distrM1 = "triangSP"
# distrM2 = "uniformSP"
# paramM1 = [1, 5, 3]
# paramM2 = [1, 5]
#
# distr_dict = {
#     "M1": [distrM1, paramM1],
#     "M2": [distrM2, paramM2]
# }
# distr_table = pd.DataFrame(distr_dict)
# distr_table = None

# print(distr_table)
#
# with open(path_IN + 'Static_model.json') as f:
#     in_data = json.load(f)
#
# initWIP = [2, 2, 2, 1, 1, 1]
#
# exec_model = DigitalModel(in_data, 1)
# for i, a in enumerate(exec_model.ObjectList):
#     print(a.id)
# a = None
# if distr_table is not None:
#     print(distr_table)
# else:
#     print("ciao")
# a = [0]
# print(a[0])
# results = exec_model.runStochSimulation(distr_table, 100, 1, initWIP)
# print(results)
# results = exec_model.runStochSimulation(distr_table, 100, 1, initWIP)
# print(results)
# database.writeData("util_sync", "digital_perf_mean", results)
# print(results['elementList'][0]['results']['working_ratio'][0])
# intdep_list = results['elementList'][0]['results']['interarrival_trace']
# intarr_list_mean = Globals.extract_mean_val(intdep_list, 2)
# th_mean = [1/x for x in intarr_list_mean]
# int_conf = Globals.confidence_interval(th_mean, 0.95)
# print(int_conf[2] - int_conf[0])
# print(int_conf[1] - int_conf[0])

# ========================================================
# a = [1, 2, 3, 4, 5, 6, 7, 8, 11]
# for i, p in enumerate(a):
#     # print(i)
#     print(i)
