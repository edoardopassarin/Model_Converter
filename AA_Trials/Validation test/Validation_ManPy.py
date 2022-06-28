from AA_Trials.Tool_Codes.DigitalModel import DigitalModel
import json
import pandas as pd
import matplotlib.pyplot as plt

directory_in = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Validation test/Arena/LEGO Model/Files/"
directory_out = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Validation test/Arena/LEGO Model/Output/"

with open("exec_model_validation.json") as f:
    in_data = json.load(f)

# with open("exec_model_validation_priority.json") as f:
#     in_data = json.load(f)

with open(directory_in + "Processing_time_S1.txt", 'r') as f:
    p1 = f.read()

Proc1 = p1.split("\n")
for i in range(len(Proc1)):
    Proc1[i] = float(Proc1[i])
print(len(Proc1))

with open(directory_in + "Processing_time_S2.txt", 'r') as f:
    p2 = f.read()

Proc2 = p2.split("\n")
for i in range(len(Proc2)):
    Proc2[i] = float(Proc2[i])
print(len(Proc2))

processing_dict = {
    "M1": pd.Series(Proc1),
    "M2": pd.Series(Proc2),
}

# processing_dict = {
#     "M1": pd.Series([5]),
#     "M2": pd.Series([6, 6, 6]),
# }

processing = pd.DataFrame(processing_dict)
print(processing)

# initWIP = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# initWIP = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
initWIP = []
init_1 = 9
init_2 = 3
for i in range(init_1):
    initWIP.append(1)
for i in range(init_2):
    initWIP.append(2)
print(initWIP)
n_pallet = len(initWIP)

model = DigitalModel(in_data)
# print(model.ObjectList[-3])
# for obj in model.ObjectList:
#     print(obj)
# print(model)

results = model.runTraceSimulation(processing, initWIP)
# print(model.ObjectList[-2].WipStat)
print(results['final_position'])
# systime_list = results['elementList'][0]['results']['system_time_trace'][0]
# print(results['eventlog'])
# syst = []
# for time in systime_list:
#     syst.append(round(time[2], 2))
# print(len(syst))
# out_data = pd.read_csv(directory_out + 'Validation_System_Time.txt', sep=" ", header=None)
# print(out_data)
# print(out_data)
# del out_data[1]
# del out_data[2]
# out_data = out_data.iloc[n_pallet:, :]
# out_data['Manpy'] = syst
# print(out_data)
# ax = plt.gca()
# out_data.plot(ax=ax)
# plt.show()

# print(out_data)
# print(model.ObjectList[-4].WipStat)

# print(results['final_position'])
#
# out_data = pd.read_csv('Validation_System_Time.txt', sep=" ", header=None)
# print(out_data)
# del out_data[1]
# del out_data[2]
# out_data = out_data.iloc[12:-1, :]
# out_data['Manpy'] = syst
# print(out_data)
# exc = bool(input('Save excel file?'))
# if exc:
#     out_data.to_excel('comparison.xlsx')

# with open('Validation_System_Time.txt', 'r') as f:
#     out_data = f.read()
#
# out_data.split()
# print(out_data)


