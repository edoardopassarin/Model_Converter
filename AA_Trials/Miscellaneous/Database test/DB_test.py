import json
from AA_Trials.Tool_Codes.interface_DB import interface_DB
from AA_Trials.Tool_Codes.DigitalModel import DigitalModel

# path_IN = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Input Files/"
# IP = "localhost"
# DB_name = "RTSimulatorDB"
# port = 8086
IP = "192.168.0.50"
DB_name = "RTSimulatorDB"
port = 8086
database = interface_DB(IP, DB_name, port)
#
# with open(path_IN + 'Static_model.json') as f:
#     in_data = json.load(f)
#
# str(in_data)
# print(in_data)
# data = [1.5, 1, 2]
# n_produced = [30, 45]
# best_scen = n_produced.index(max(n_produced))
# data_scen1 = [1, n_produced[0], int(best_scen == 0)]
# data_scen2 = [2, n_produced[1], int(best_scen == 1)]
# print(data_scen1)
# print(data_scen2)
# database.writeData("scenario", "feedback_info", data_scen1)
# database.writeData("scenario", "feedback_info", data_scen2)
# test = database.queryData("final_position_eval", "initialization")
# # test = test.replace("\'", "\"")
# print(test)
# print(type(test))

# a = 'M1'
# print(a[-1])

# ===============================================================
graph_model_temp = database.queryData('graph_model', 'model')
print(type(graph_model_temp))
# exec_model = DigitalModel(exec_model_temp)
# print(exec_model)
# for obj in exec_model.ObjectList:
#     print(obj)

# with open('exec_model_final.json', 'r') as f:
#     in_data = json.load(f)

with open('graph_model_final.json', 'w') as f:
    json.dump(graph_model_temp, f, indent=4)
#
# database.writeData('executable_model', 'model', in_data)


# model = database.queryData()
