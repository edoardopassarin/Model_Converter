from AA_Trials.Tool_Codes.ModelConverter import ModelConverter
import json
from AA_Trials.Tool_Codes.DigitalModel import DigitalModel

# Files directories
dir_mod = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Conversion/Generated Models/"

# Names of the different configurations
models_list = ['Flowline', 'MM1K', 'Simple Open', 'Parallel']
model = models_list[3]
print(f'Analysing model named: {model}\n')

# Load the generated graph model
with open(dir_mod + model + '/' + model + '_generated.json') as f:
    graph_model_temp = json.load(f)

# Convert the model
graph_model_draft = ModelConverter(graph_model_temp)
exec_model_draft = graph_model_draft.convertModel()

# Create the json file with the executable model draft
flag = input('Save the converted model DRAFT? \n')
if flag:
    with open(dir_mod + model + '/' + model + '_executable_draft.json', 'w') as f:
        json.dump(exec_model_draft, f, indent=4)

exec_model = DigitalModel(exec_model_draft)
print(exec_model)
for obj in exec_model.ObjectList:
    print(obj)
    print(obj.freq_parallel)

# ===========================================================================================
# Configuration dictionary

# FLOWLINE
# config_conv = {
#                 'queueCap': {
#                             'Q1': 8,
#                             'Q2': 7,
#                             'Q3': 12,
#                             'Q4': 13,
#                             'Q5': 10,
#                             'QS1': 15,
#                             }
#                 }

# PARALLEL
config_conv = {
                'queueCap': {
                            'Q1': 1000,
                            'Q2': 1000,
                            'Q3': 1000,
                            'Q4': 1000,
                            'Q5': 1000,
                            'Q6': 1000,
                            'QS1': 1000,
                            }
                }

# Convert the model with correct queues and interarrivals
graph_model = ModelConverter(graph_model_temp, config_conv)
exec_model = graph_model.convertModel()

# # FLOWLINE
# interarr_dist = {
#     'UniformSP': {
#         'locSP': 20,
#         'scaleSP': 2
#     }
# }

# PARALLEL
interarr_dist = {
    'UniformSP': {
        'locSP': 28,
        'scaleSP': 5
    }
}

exec_model['graph']['node']['S1']['interArrivalTime'] = interarr_dist

# Create the json file with the executable model final
flag = input('Save the converted model FINAL? \n')
if flag:
    with open(dir_mod + model + '/' + model + '_executable_final.json', 'w') as f:
        json.dump(exec_model, f, indent=4)
