# %% IMPORTS
from time import sleep
import json
import paho.mqtt.client as mqtt


# %% MQTT RELATED

def on_connect(client, userdata, flags, rc):
    print("CONNECTED: result code " + str(rc))
    client.subscribe("topic/config")


def on_message(client, userdata, msg):
    # print(msg.payload.decode())

    ######################
    # TO BE ADDED IN THE IMS FILE - START
    global ims_config

    if msg.topic == "topic/config":
        ims_config = json.loads(msg.payload.decode())
        change_params_online(ims_config)
    # TO BE ADDED IN THE IMS FILE - END
    ######################

    if msg.payload.decode() == "stop":
        print("STOPPING AS REQUESTED")
        cond_while = False
        client.loop_stop()


######################
# TO BE ADDED IN THE IMS FILE - START
def change_params_online(ims_config):
    global Product_A, station, next_station, failure_prob, conveyor_speed, pusher_speed, station_speed
    global pos_wait, pos_pass, pos_push, pos_init
    global pusher_pass_time, unload_time, station_timeout
    global w_distribution_type, f_distribution_type
    global w_distribution_par, f_distribution_par
    #
    global Tw_Amin, Tf_Amin, deg_param, joint_maintenance
    global seed
    global timeout_restart
    global refresh_main, refresh_support
    global threshold_low, threshold_high, max_samples_blocking

    Product_A = ims_config['Product_A']  # Types of Product definition
    station = ims_config['station']  # STATION NUMBER
    next_station = ims_config['next_station']  # FOLLOWING STATION (FOR BLOCKING!)
    failure_prob = ims_config['failure_prob']  # FAILURE PROBABILITY

    # MOTORS SPEED
    conveyor_speed = ims_config['conveyor_speed']
    pusher_speed = ims_config['pusher_speed']
    station_speed = ims_config['station_speed']

    # PUSHER POSITIONS
    pos_wait = ims_config['pos_wait']
    pos_pass = ims_config['pos_pass']
    pos_push = ims_config['pos_push']
    pos_init = 0

    # WAITING TIMES
    pusher_pass_time = ims_config['pusher_pass_time']
    unload_time = ims_config['unload_time']
    station_timeout = ims_config['station_timeout']

    # PROCESSING AND FAILURE TIMES DISTRIBUTIONS
    w_distribution_type = ims_config['w_distribution_type']
    f_distribution_type = ims_config['f_distribution_type']

    w_distribution_par = ims_config['w_distribution_par']
    f_distribution_par = ims_config['f_distribution_par']

    Tw_Amin = ims_config['w_minimum_time']  # minimum processing time
    Tf_Amin = ims_config['f_minimum_time']  # minimum failure time

    deg_param = ims_config['deg_param']  # parameter for degradation

    joint_maintenance = ims_config['joint_maintenance']  # list of stations with which to do joint maintenance

    # RANDOM NUMBER GENERATION
    seed = ims_config['seed']

    # TIMEOUTS
    timeout_restart = ims_config['timeout_restart']

    # REFRESH INTERVALS
    refresh_main = ims_config['refresh_main']  # MAIN PROGRAM REFRESH INTERVAL (STANDARD IS 0.1 s)
    refresh_support = ims_config['refresh_support']  # SUPPORT OPERATIONS REFRESH INTERVAL (STANDARD IS 1 s)

    # PART SEEN THRESHOLDS (COL-REFLECT MODE)
    threshold_low = ims_config['threshold_low']  # DEFAULT 10
    threshold_high = ims_config['threshold_high']  # DEFAULT 20

    # MAX SAMPLES FOR BLOCKING (DEFAULT 10)
    max_samples_blocking = ims_config['max_samples_blocking']


# TO BE ADDED IN THE IMS FILE - END
#######################

client = mqtt.Client()
client.connect("192.168.0.50", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_start()

# %% MAIN

# READ EXTERNAL JSON WITH CONFIG
with open('ims_config.json', 'r') as f:
    json_str = f.read()
    ims_config = json.loads(json_str)

# TEST -  CHECK PUSHER SPEED BEFORE MODIFICATION
print(ims_config['w_distribution_par'])

# TEST - MODIFY THE VALUE OF PUSHER SPEED
ims_config['w_distribution_par'] = 1
ims_config['station_speed'] = 200
ims_config['failure_prob'] = 0

# TO BE TRIED
# {"station": 1, "parameter": "w_distribution_par", "value" 123}

print(ims_config['w_distribution_par'])

# SEND THE CONFIG FILE VIA MQTT
data_out = json.dumps(ims_config, indent=4)
client.publish("topic/config", data_out)

# TEST -  CHECK PUSHER SPEED AFTER MODIFICATION (THIS IS HAPPENING ON SYSTEM)
# print(pusher_speed)

# CLOSE MQTT LOOP
client.loop_stop()
