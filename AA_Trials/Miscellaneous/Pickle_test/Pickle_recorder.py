import json
import pickle
import json

directory = 'C:/Users/edoar/OneDrive - Politecnico di Milano/EDO&FRA_tesi/Test bench/Validation/Recordings/Scenario0/'

with open(directory + 'msg_list_scen0.pickle', 'rb') as f:
    list_p = pickle.load(f)

test = list_p[0]
test_p = json.dumps(test)

print(json.dumps(test['payload']))
print(test['topic'])
for i in range(20):
        print(list_p[i])
