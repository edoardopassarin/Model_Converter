# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:14:15 2021

@author: franc
"""
# import paho.mqtt.client as mqtt
import json
import pandas as pd
import pickle

#import datetime
import time
import datetime
from time import sleep
import numpy as np

# ADDED to query
# from influx import InfluxDB
from influxdb import InfluxDBClient
from influxdb import DataFrameClient


class interface_DB():

    def __init__(self,ip,DB_name,port):
        self.ip=ip
        self.DB_name=DB_name
        self.port=port
        self.client = InfluxDBClient(host=self.ip, port=self.port)
        self.client_df=DataFrameClient(host=self.ip, port=self.port)

    # def writeData(self,measurement_name,measures_name,data):

    #     if measurement_name=='real_perf':


    #         if measures_name=='processing_times_real':



    def queryData(self,measures_name=None,measurement_name=None,t_query=None):


        self.client.switch_database(self.DB_name)

        if measurement_name=='eventlog':

                eventlog= self.client.query('SELECT * FROM eventlog WHERE time >now()-'+str(t_query),epoch='s')
                data=eventlog.raw


                df=pd.DataFrame(data['series'][0]['values'],columns=['time','activity','id','type']) #Dataframe

                #Filtering
                df['activity'] = df['activity'].astype(int)  #conversion of activity column from string to integer
                df['id'] = df['id'].astype(int)               #conversion of id column from string to integer
                df_c=df.drop_duplicates(subset=['activity','id','type'],keep='first')   #elimination of duplicates for column 'type' ovvero le letture doppie di start e finish, OCCHIO CHE é UNA COSA MOLTO GREZZA

                return df_c



        if measurement_name =='real_perf':
            if measures_name=='processing_time_real':

                p_timereal=self.client.query('SELECT * FROM real_perf WHERE time >now()-'+str(t_query),epoch='s')


                p_timereal=pd.DataFrame(p_timereal.raw['series'][0]['values'],columns=['time','activity','measures','part_id','value'])

                p_timereal.loc[(p_timereal['measures']=="processing_time_real")]
                p_timereal=p_timereal.drop('time', axis='columns')
                p_timereal=p_timereal.drop('measures', axis='columns')
                p_timereal['activity']=pd.to_numeric(p_timereal['activity']).astype(int)
                p_timereal['part_id']=pd.to_numeric(p_timereal['part_id']).astype(int)
                p_timereal['value']=pd.to_numeric(p_timereal['value']).astype(int)

                return p_timereal

         # Read Graph model from the database (ModelConverter)
        if measurement_name == 'model':
            if measures_name == 'graph_model':
                 # query the last graph model
                 graph_model = self.client.query("SELECT * FROM model WHERE type = '"
                                                 + measures_name + "' GROUP BY * ORDER BY DESC LIMIT 1")
                 # extract the string with the last graph model
                 graph_model = graph_model.raw['series'][0]['values'][0][1]
                 # transform the string into a dict
                 graph_model = json.loads(graph_model.replace("\'", "\""))

                 return graph_model


                # Read Executable model from the database (DigitalModel)

            if measures_name == 'executable_model':
                # query the last executable model
                exec_model = self.client.query("SELECT * FROM model WHERE type = '"
                                               + measures_name + "' GROUP BY * ORDER BY DESC LIMIT 1")
                # extract the string with the last executable model
                exec_model = exec_model.raw['series'][0]['values'][0][1]
                # transform the string into a dict
                exec_model = json.loads(exec_model.replace("\'", "\""))

                return exec_model

                # Read Processing Times from the database (DigitalModel)

                # Read WIP position list from database (DigitalModel)

                # Read Correlated Processing Times from the database (DigitalModel)

        if measurement_name == "distributions":
            # query the last distribution
            dist_temp = self.client.query("SELECT * FROM distributions GROUP BY * ORDER BY DESC LIMIT " + str(t_query))
            #
            dist_temp = dist_temp.raw['series']
            distr_dict = {}
            for dist in dist_temp:
                mach = "M" + dist['tags']['measures'][-2]
                dist_name = dist['values'][0][1]
                param = json.loads(dist['values'][0][2])
                distr_dict.update({mach: [dist_name, param]})

            distribution = pd.DataFrame(distr_dict)
            return distribution

        if measurement_name == "history_validation":
            if measures_name == "input":
                validation_hist = self.client.query("SELECT * FROM history_validation WHERE type = 'input' GROUP BY * ORDER BY DESC LIMIT 1")
                validation_bool = bool(validation_hist.raw['series'][0]['values'][0][3])
                return validation_bool

        if measurement_name == "digital_perf_mean":
            if measures_name == "th_eval":
                th_val = self.client.query("SELECT * FROM digital_perf_mean WHERE measures = 'th_eval' GROUP BY * ORDER BY DESC LIMIT 1")
                th_val = th_val.raw['series'][0]['values'][0][2]
                return json.loads(th_val)

        if measurement_name == "initialization":
            if measures_name == "final_position_eval":
                final_pos = self.client.query("SELECT * FROM initialization WHERE measures = 'final_position' GROUP BY * ORDER BY DESC LIMIT 1")
                final_pos = final_pos.raw['series'][0]['values'][0][2]
                return json.loads(final_pos)

    def writeData(self,measures_name,measurement_name,data):
        self.client.switch_database(self.DB_name)
        data=data

        if measurement_name =='initialisation':

            init_pos=data
            json_init_pos=[{"measurement":"initialization","tags":{"measures":"initial_position"},"fields":{"list":str(init_pos['location'].tolist())}}]
            self.client.write_points(json_init_pos)

        if measurement_name == "real_perf":
            if measures_name=="processing_time_real":

                for i in range(0,len(data)):

                    json_p_timereal=[{"measurement":"real_perf",
                                      "tags":{"measures":"processing_time_real",
                                              "activity":str(data.iloc[i]['activity']),
                                              "part_id":str(data.iloc[i]['part_id'])
                                              },
                                      "fields":{"value":float(data.iloc[i]['value'])
                                                }
                                      }]

                    self.client.write_points(json_p_timereal)


        if measurement_name=="digital_perf":

            if measures_name=="system_time_digital":




                insert_time=datetime.datetime.now()

                for i in range(0,data.shape[0]):

                    json_p_timereal=[{"measurement":"digital_perf",
                                      "tags":{"measures":"System_Time_Digital",
                                              "part_id":float(i),
                                              "replication":float(0),
                                              "simulator_id":"Arena",
                                              },
                                      "time": str(insert_time),
                                      "fields":{"value":float(data.iloc[i]['System Time Digital']),
                                                 "timelog":float(0)

                                                }
                                      }]

                    #self.client_df.write_points(data[i], "digital_perf", tags={"measures": "system_time_digital"},field_columns={'value'})
                    self.client.write_points(json_p_timereal)


            if measures_name=="system_time_digital_Manpy":
                results = data
                datalist = results['elementList'][0]['results']['system_time_trace'][0]
                # initialize the lists for the columns in the dataframe
                timelog_list = []
                ID_list = []
                systime_list = []

                # populate the lists
                for i in range(len(datalist)):
                    timelog_list.append(datalist[i][0])
                    ID_list.append(datalist[i][1])
                    systime_list.append(datalist[i][2])

                # create the dict to transform into a DataFrame
                systime_dict = {
                    "activity": 1,  # TO FIX, INSERT THE ACTIVITY IN THE INPUT DICT result
                    "part_id": pd.Series(ID_list),
                    "replication": 1,  # TO FIX, INSERT THE REPLICATION IN THE INPUT DICT result
                    "simulator_id": 1,  # TO FIX, INSERT THE SIMULATOR ID IN THE INPUT DICT result
                    "timelog": pd.Series(timelog_list),
                    "value": pd.Series(systime_list),
                }

                # create the Dataframe
                systime_DF = pd.DataFrame(systime_dict)
                # systime_DF.set_index('part_id', inplace=True)

                insert_time = datetime.datetime.now()

                for i in range(0, systime_DF.shape[0]):
                    json_p_timereal = [{"measurement": "digital_perf",
                                        "tags": {"measures": "System_Time_Digital",
                                                 "part_id": float(systime_DF.iloc[i]['part_id']),
                                                 "replication": float(systime_DF.iloc[i]['replication']),
                                                 "simulator_id": "Manpy"+str(systime_DF.iloc[i]['simulator_id']),
                                                 },
                                        "time": str(insert_time),
                                        "fields": {"value": float(systime_DF.iloc[i]['value']),
                                                   "timelog": float(systime_DF.iloc[i]['timelog'])

                                                   }
                                        }]

                    # self.client_df.write_points(data[i], "digital_perf", tags={"measures": "system_time_digital"},field_columns={'value'})
                    self.client.write_points(json_p_timereal)

            if measures_name == "interdeparture_time_digital":
                results = data
                datalist = results['elementList'][0]['results']['interarrival_trace'][0]
                # initialize the lists for the columns in the dataframe
                timelog_list = []
                ID_list = []
                intarr_list = []

                # populate the lists
                for i in range(len(datalist)):
                    timelog_list.append(datalist[i][0])
                    ID_list.append(datalist[i][1])
                    intarr_list.append(datalist[i][2])

                # create the dict to transform into a DataFrame
                intarr_dict = {
                    "activity": 1,  # TO FIX, INSERT THE ACTIVITY IN THE INPUT DICT result
                    "part_id": pd.Series(ID_list),
                    "replication": 1,  # TO FIX, INSERT THE REPLICATION IN THE INPUT DICT result
                    "simulator_id": 1,  # TO FIX, INSERT THE SIMULATOR ID IN THE INPUT DICT result
                    "timelog": pd.Series(timelog_list),
                    "value": pd.Series(intarr_list),
                }

                # create the Dataframe
                intarr_DF = pd.DataFrame(intarr_dict)


                insert_time = datetime.datetime.now()

                for i in range(0, intarr_DF.shape[0]):
                    json_p_timereal = [{"measurement": "digital_perf",
                                        "tags": {"measures": "System_Time_Digital",
                                                 "part_id": float(intarr_DF.iloc[i]['part_id']),
                                                 "replication": float(intarr_DF.iloc[i]['replication']),
                                                 "simulator_id": "Manpy"+str(intarr_DF.iloc[i]['simulator_id']),
                                                 },
                                        "time": str(insert_time),
                                        "fields": {"value": float(intarr_DF.iloc[i]['value']),
                                                   "timelog": float(intarr_DF.iloc[i]['timelog'])

                                                   }
                                        }]

                    # self.client_df.write_points(data[i], "digital_perf", tags={"measures": "system_time_digital"},field_columns={'value'})
                    self.client.write_points(json_p_timereal)









        if measurement_name == "digital_perf_mean":
            if measures_name == "th_eval":
                insert_time = datetime.datetime.now()
                json_th = [{
                    "measurement": "digital_perf_mean",
                    "tags": {"measures": measures_name},
                    "time": insert_time,
                    "fields": {
                        "activity": 1.0,
                        "interval": str(data)
                    }
                }]
                self.client.write_points(json_th)

            if measures_name == "util_sync":
                for i in range(2):
                    util_value = data['elementList'][i]['results']['working_ratio'][0]
                    insert_time = datetime.datetime.now()
                    json_th = [{
                        "measurement": "digital_perf_mean",
                        "tags": {"measures": measures_name},
                        "time": insert_time,
                        "fields": {
                            "activity": float(i+1),
                            "value": util_value
                        }
                    }]
                    self.client.write_points(json_th)



        if measurement_name=="eventlog":

            for i in range(0,data.shape[0]):

                json_p_timereal=[{"measurement":"eventlog",
                                  "tags":{"activity":data.iloc[i]['activity'],
                                          },
                                  "time": data.iloc[i]['time'],
                                  "fields":{"id":float(data.iloc[i]['id']),
                                             "type":str(data.iloc[i]['type'])

                                            }
                                  }]

                #self.client_df.write_points(data[i], "digital_perf", tags={"measures": "system_time_digital"},field_columns={'value'})
                self.client.write_points(json_p_timereal)



        # Upload executable model to the database (ModelConverter)
        if measurement_name == "model":
            if measures_name == "executable_model":
                exec_model = data
                json_exec_model = [{"measurement": "model", "tags": {"type": "executable_model"},
                                    "fields": {"file": str(exec_model)}}]
                self.client.write_points(json_exec_model)

        # Upload the digital eventlog
        if measurement_name == "digital_eventlog":

            insert_time = datetime.datetime.now()

            for i in range(len(data["eventlog"][0])):
                json_dig_eventlog = [{"measurement": "digital_eventlog",
                                      "tags": {"activity": data[1][i]},
                                      "time": insert_time,
                                      "fields": {"id": data[2][i],
                                                 "type": data[3][i],
                                                 "timelog": data[0][i]
                                               }
                                    }]
                self.client.write_points(json_dig_eventlog)





    def queryDataSpecial(self,measures_name,measurement_name,t_query):

        if measurement_name =='real_perf':
            if measures_name=='processing_time_real':




                p_timereal=self.queryData(measures_name, measurement_name, t_query)

                p_timesimul_input= pd.DataFrame(index = range(0,len(p_timereal)),
                                                columns=[i for i in range(1,max(p_timereal['activity'])+1)]+['part_id'])

                for actx in range(1,int(max(p_timereal['activity']))+1):

                    p_timesimul_column_candidate=p_timereal.loc[(p_timereal['activity']==actx)]
                    p_timesimul_column_candidate.reset_index(drop=True)

                    for i in range(0,len(p_timesimul_column_candidate)):

                        p_timesimul_input[actx][i]=p_timesimul_column_candidate.iloc[i]['value']
                        p_timesimul_input['part_id'][i]=p_timesimul_column_candidate.iloc[i]['part_id']


                p_timesimul_input=p_timesimul_input.dropna(how="all")

                p_timereal_Nan_count=[]
                for actx in range(1,p_timesimul_input.shape[1]):

                    for i in range(0,p_timesimul_input.shape[0]):

                        if pd.isna(p_timesimul_input[actx][i])==True:
                            p_timereal_Nan_count.append([actx,p_timesimul_input['part_id'][i]])

                if len(p_timereal_Nan_count)!=0:

                    print('Processing Times Incomplete ATM:[Activity, Part_id] :')
                    print(p_timereal_Nan_count)
                    print('-----------------------------------')

                return  p_timesimul_input

            if measures_name=='processing_time_real_Manpy':

                p_timereal=self.queryData('processing_time_real', measurement_name, t_query)

                p_timesimul_input= pd.DataFrame(index = range(0,len(p_timereal)),
                                                columns=[i for i in range(1,max(p_timereal['activity'])+1)]+['part_id'])

                for actx in range(1,int(max(p_timereal['activity']))+1):

                    p_timesimul_column_candidate=p_timereal.loc[(p_timereal['activity']==actx)]
                    p_timesimul_column_candidate.reset_index(drop=True)

                    for i in range(0,len(p_timesimul_column_candidate)):

                        p_timesimul_input[actx][i]=p_timesimul_column_candidate.iloc[i]['value']
                        p_timesimul_input['part_id'][i]=p_timesimul_column_candidate.iloc[i]['part_id']


                p_timesimul_input=p_timesimul_input.dropna(how="all")

                p_timereal_Nan_count=[]
                for actx in range(1,p_timesimul_input.shape[1]):

                    for i in range(0,p_timesimul_input.shape[0]):

                        if pd.isna(p_timesimul_input[actx][i])==True:
                            p_timereal_Nan_count.append([actx,p_timesimul_input['part_id'][i]])

                if len(p_timereal_Nan_count)!=0:

                    print('Processing Times Incomplete ATM:[Activity, Part_id] :')
                    print(p_timereal_Nan_count)
                    print('-----------------------------------')

                for actx in range(1,p_timesimul_input.shape[1]+1):
                    p_timesimul_input =  p_timesimul_input.rename(columns={str(actx): 'M'+str(actx)})





                return  p_timesimul_input











