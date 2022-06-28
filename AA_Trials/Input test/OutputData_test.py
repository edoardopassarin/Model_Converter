import json

with open('test_systime_CS_Output.json') as f:
    in_data = json.load(f)

print(type(in_data))
print(in_data['elementList'][0]['results']['system_time_trace'])
print(in_data['elementList'][0]['results']['interarrival_trace'])
# list = []
# b = [1, 2, 3]
# c = [4, 5, 6]
# list.append(b)
# list.append(c)
# print(list)
