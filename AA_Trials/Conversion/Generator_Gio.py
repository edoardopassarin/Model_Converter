import json

import pandas as pd
from MSM.msmlib import gen_model_init

# Files directories
dir_in = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Conversion/Output/"
dir_out = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Conversion/Generated Models/"

# Names of the different configurations
models_list = ['Flowline', 'MM1K', 'Simple Open', 'Parallel']
model = models_list[3]
print(f'Analysing model named: {model}\n')

# Open the eventlog file
col_ev = ['time', 'activity', 'tag', 'id', 'temp']
eventlog_in = pd.read_csv(dir_in + model + '/eventlog.txt', sep=" ", header=None, names=col_ev)
del eventlog_in['temp']

# Generate model return graph_dict
config = {"batching": {"threshold_arcs": 1, "threshold_nodes": 1}}

data = eventlog_in
data['ts'] = eventlog_in['time'].apply(lambda x: x)
data['tag'] = eventlog_in['tag'].apply(lambda x: x)
data['id'] = eventlog_in['id'].apply(lambda x: x)

graph_dict, unique_list, tracetoremove, id_trace_record = gen_model_init(data, config, tag=True)

for node in graph_dict["nodes"]:
    node["stats"] = 'temp'

with open(dir_out + model + '/' + model + '_generated.json', 'w') as f:
    json.dump(graph_dict, f, indent=4)
