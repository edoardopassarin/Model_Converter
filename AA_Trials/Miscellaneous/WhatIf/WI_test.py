from broker_c import broker
import json
from time import sleep

with open('ims_config.json', 'r') as f:
    json_str = f.read()
    ims_config = json.loads(json_str)

brok = broker("192.168.0.50", 1883, 60, "RTSimulatorDB")
print(ims_config)
# ims_config['failure_prob'] = 1
# ims_config['f_distribution_par'] = 60
#
# print(ims_config)
# brok.feedback(ims_config, "topic/config")
#
# sleep(15)

ims_config['failure_prob'] = 0
ims_config['w_distribution_par'] = [2, 5, 3]
brok.feedback(ims_config, "topic/config")
