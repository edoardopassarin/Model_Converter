import json
from time import sleep
from broker import broker

brok = broker("192.168.0.50", 1883, 60, "RTSimulatorDB")
topic = "topic/config"

ttr = 2 * 60

# READ EXTERNAL JSON WITH CONFIG
path_in_config = "C:/Users/edoar/repos/Model_Generator/AA_Trials/Miscellaneous/WhatIf/"
with open(path_in_config + "ims_config.json", "r") as f:
    json_str = f.read()
    config = json.loads(json_str)

config["failure_prob"] = 1
config["f_distribution_par"] = ttr
brok.feedback(config, topic)

sleep(30)

config["failure_prob"] = 0

brok.feedback(config, topic)
