import json

with open('original_model.json') as f:
    data = json.load(f)

for nodes in data['nodes']:
    print(nodes['predecessors'], nodes['successors'])

for nodes in data['nodes']:
    del nodes['frequency']

with open('original_model_nofreq.json', 'w') as f:
    json.dump(data, f, indent=2)
