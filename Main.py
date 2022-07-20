"""This file is meant to show how the model converter and simulator works"""

import json
import os
import sys
import pandas as pd

from Tool_Codes.ModelConverter import ModelConverter
from Tool_Codes.DigitalModel import DigitalModel

# First we read a json file containing the graph model obtained with process mining
# There are examples of these files in the directory "Test Files"

with open(os.path.join(sys.path[0], "Generated_model_closed.json"), "r") as f:
    graph_dict = json.load(f)      # We assign the JSON file to a dictionary

# Before initializing the object we can use a configuration dictionary to specify some
# conversion parameters manually
config_dict = {
    'start': 'M1',      # only for closed-loop model, to specify the start of the loop
    'unloadTime': 3.2,  # unload time of the machine
    'transportationTime': 15,   # transportation time if there are conveyors
    'transportationCap': 2,     # capacity of the conveyors
    'queueCap': {       # to override the capacity of the queues
        'Q1': 8,
        'Q2': 7,
    }
}

# We create an object from the ModelConverter class, and give as input the config file
graph_model = ModelConverter(graph_dict, config_dict)

# We convert the model and obtain a dictionary containing the simulation model data
simulation_dict = graph_model.convertModel()
# This dictionary can then be either used to create a simulation model, but it can also
# be saved and then imported and used in other occasions

# We create a simulation model object from the DigitalModel class
simulation_model = DigitalModel(simulation_dict)

# To see the element of the simulation object just use the print funciton
# print(simulation_model)

# To see the parameters of the objects inside the model
# for obj in simulation_model.ObjectList:
#     print(obj)


"""The simulation model can run stochastic simulations (that use distributions) or 
trace-driven simulation, in both cases some inputs are necessary
"""

# TRACE-DRIVEN SIMULATIONS

# First input is a pandas dataframe containing the values of the processing times
processing_dict = {
    "M1": pd.Series([6.0, 6.0, 6.0, 7.0, 8.0, 10.0, 9.0]),
    "M2": pd.Series([8.0, 8.0, 8.0, 9.0, 8.0, 7.0, 10.0]),
}
proc_time_df = pd.DataFrame(processing_dict)

# Second input is a list with the initial position of the WIPs on the line
initWIP = [2, 2, 2, 1, 1, 1]

# Run the trace driven simulation
results_td = simulation_model.runTraceSimulation(proc_time_df, initWIP)


# STOCHASTIC SIMULATIONS

# First input is a dictionary with the distributions of the machines
distrM1 = "normalSP"
distrM2 = "gammaSP"
paramM1 = [5, 4]
paramM2 = [1, 3, 20]
distr_dict = {
    "M1": [distrM1, paramM1],
    "M2": [distrM2, paramM2]
}
distr_df = pd.DataFrame(distr_dict)

# Then we need the initial positioning of the WIPs (like in trace-driven simulations)
initWIP = [2, 2, 2, 1, 1, 1]

# Finally the length of the simulation, the number of replications and the seed
n_replications = 5
sim_length = 500
seed = 386

# Finally we run the stochastic simulation
results_s = simulation_model.runStochSimulation(
    distr_df,
    sim_length,
    n_replications,
    initWIP,
    seed
)

# To see the results regarding the first object of the model
# print(results_s['elementList'][0])

# To see the trace of the system time values (gathered on M1)
# each entry is timestamp - part_ID - systime_value
# For more replications (only in stoch simulation) there are multiple lists, one fore
# each replication
print(results_s['elementList'][0]['results']['system_time_trace'][0]) # first rep
