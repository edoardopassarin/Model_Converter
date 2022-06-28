import json
from AA_Trials.Simulator.ModelConverter import ModelConverter

path_IN = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Input Files/"
path_OUT = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Test Files/Output Files/"

with open(path_IN + 'original_model.json') as f:
    in_data = json.load(f)              # Save the content of the JSON file into a dict variable
#
graph_model = ModelConverter(in_data, 1)
exec_model = graph_model.convertModel()
print(exec_model)

# num_of_machines = len(in_data['nodes'])     # Find the number of machines in the system
# num_of_queues = len(in_data['arcs'])        # Find the number of queues in the system
#
# num_connections = 2 * num_of_queues         # the number of connections is always two times the number of queues
#
# sim_length = 1440           # simulation length, MAYBE add input functionality
# num_rep = 1                 # number of replications, MAYBE add input functionality
# out_data = {                # output dict variable, that will be transformed into a JSON file
#     "general": {            # key "general", containing the simulation parameters
#         "maxSimTime": sim_length,
#         "numberOfReplications": num_rep,
#         "Trace": "No",
#         "seed": 1
#     },
#     "graph": {              # key "graph", containing "edge" and "node"
#         "edge": {},         # key "edge", containing all the connections between objects
#         "node": {}          # key "node", containing all the objects of the system
#     }
# }
#
# for m in range(num_of_machines):        # cycle for writing the machines with all their parameters
#     machine_capacity = in_data['nodes'][m]['capacity']
#     if machine_capacity == 1:       # if the capacity of the machine is 1, we create only 1 machine
#         out_data["graph"]["node"].update({
#             "M" + str(m+1): {               # ID of the single machine
#                 "_class": "manpy.Machine",  # specify that the object is a machine
#                 "name": "Machine",
#                 "processingTime": {         # processing time of the machine with its distribution
#                     "Exp": {
#                         "mean": 1.0
#                     }
#                 }
#             }
#         })
#     else:       # if the capacity of the machine is greater than one, create parallel machines equal to capacity
#         for c in range(machine_capacity):       # for cycle for machines with capacity greater than one
#             out_data["graph"]["node"].update({
#                 "M" + str(m+1) + "_" + str(c+1): {      # if M1 has capacity 3, we create M1_1, M1_2, M1_3
#                     "_class": "manpy.Machine",
#                     "name": "Machine",
#                     "processingTime": {
#                         "Exp": {
#                             "mean": 1.0
#                         }
#                     }
#                 }
#             })
#
# for q in range(num_of_queues):          # cycle for writing the queues with all their parameters
#     out_data["graph"]["node"].update({
#         "Q" + str(q+1): {               # ID of the single queue
#             "class": "manpy.Queue",     # specify that the object is a queue
#             "capacity": in_data['arcs'][q]['capacity'],     # obtain the capacity of the queue from the input file
#             "name": "Queue",
#             "wip": []
#         }
#     })
#
# for e in range(0, 2*num_of_queues, 2):          # cycle for writing all the edges, we have two edges for every queue
#     prec_mach_id = in_data['arcs'][int(e/2)]['arc'][0]      # id of the predecessor machine
#     succ_mach_id = in_data['arcs'][int(e/2)]['arc'][1]      # id of the successor machine
#     prec_mach_cap = in_data["nodes"][prec_mach_id-1]["capacity"]    # capacity of the predecessor machine
#     succ_mach_cap = in_data["nodes"][succ_mach_id-1]["capacity"]    # capacity of the successor machine
#     if prec_mach_cap == 1:      # if the predecessor machine has capacity equal to 1, we create only one arc
#         out_data["graph"]["edge"].update({          # for every queue we have an incoming edge
#             str(e + 1): {
#                 "class": "manpy.Edge",
#                 "destination": "Q" + str(int(e/2) + 1),                         # picks the current queue
#                 "source": "M" + str(prec_mach_id)        # picks the incoming machine
#             }
#         })
#     else:       # if the predecessor machine has capacity greater than 1, we create as many edges as capacity
#         for c in range(prec_mach_cap):
#             out_data["graph"]["edge"].update({
#                 str(e + 1) + "_" + str(c + 1): {
#                     "class": "manpy.Edge",
#                     "destination": "Q" + str(int(e/2) + 1),
#                     "source": "M" + str(prec_mach_id) + "_" + str(c + 1)
#                 }
#             })
#
#     if succ_mach_cap == 1:
#         out_data["graph"]["edge"].update({          # for every queue we have an outgoing edge
#             str(e + 2): {
#                 "class": "manpy.Edge",
#                 "destination": "M" + str(succ_mach_id),  # picks the outgoing machine
#                 "source": "Q" + str(int(e/2) + 1)                               # picks the current queue
#             }
#         })
#     else:
#         for c in range(succ_mach_cap):
#             out_data["graph"]["edge"].update({
#                 str(e+2) + "_" + str(c+1): {
#                     "class": "manpy.Edge",
#                     "destination": "M" + str(succ_mach_id) + "_" + str(c+1),
#                     "source": "Q" + str(int(e/2) + 1)
#                 }
#             })
#
# to_file = json.dumps(out_data, indent=2)      # create a JSON variable that will be written into a .json file
# print(to_file)
#
# with open(path_OUT + 'conversion_output.json', 'w') as f:
#     json.dump(out_data, f, indent=2)            # convert the dict into JSON and write it to a .json file
