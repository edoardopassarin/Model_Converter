from AA_Trials.Tool_Codes.DigitalModel import DigitalModel
import json
import pandas as pd

path_IN = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Input Files/"
path_OUT = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Output Files/"

with open(path_IN + 'PT_S1_Val.txt') as f:
    content = f.read()
    PT_S1 = content.split("\n")

with open(path_IN + 'PT_S2_Val.txt') as f:
    content = f.read()
    PT_S2 = content.split("\n")

min_len = min(len(PT_S1), len(PT_S2))

for ii, a in enumerate(PT_S1):
    PT_S1[ii] = int(PT_S1[ii])

for ii, a in enumerate(PT_S2):
    PT_S2[ii] = int(PT_S2[ii])

processing_dict = {
    "M1": pd.Series(PT_S1),
    "M2": pd.Series(PT_S2),
}
processing = pd.DataFrame(processing_dict)

# =========================================

with open(path_IN + 'Routing_val.txt') as f:
    content = f.read()
    initWIP = content.split("\n")

for ii, a in enumerate(initWIP):
    initWIP[ii] = int(initWIP[ii])

numWIP = len(initWIP)

# =========================================

with open(path_IN + 'Static_model.json') as f:
    in_data = json.load(f)

exec_model = DigitalModel(in_data, 1)
results = exec_model.runTraceSimulation(processing, initWIP)

# sys_time_list = results['elementList'][0]['results']['system_time_trace'][0][numWIP:]
# sys_time = []
# for ii, a in enumerate(sys_time_list):
#     sys_time.append(round(sys_time_list[ii][2], 2))

# print(sys_time)

interarr_list = results['elementList'][0]['results']['interarrival_trace']
print(len(PT_S1))

# ========================================
# with open(path_IN + 'Sys_Time_Val.txt') as f:
#     content = f.read()
#     sys_time_Arena = content.split("\n")
#
# for ii, a in enumerate(sys_time_Arena):
#     sys_time_Arena[ii] = float(sys_time_Arena[ii])
#
# print(sys_time_Arena)
