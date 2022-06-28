# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:14:15 2021

@author: franc
"""
import json
import pandas as pd
import pickle

#import datetime
import time
import datetime
from time import sleep
import numpy as np

# ADDED to query
from influxdb import InfluxDBClient
from influxdb import DataFrameClient


class interface_DB():

    def __init__(self,ip,DB_name,port):
        self.ip=ip
        self.DB_name=DB_name
        self.port=port
        self.client = InfluxDBClient(host=self.ip, port=self.port)

    # def writeData(self,measurement_name,measures_name,data):



    #     if measurement_name=='real_perf':


    #         if measures_name=='processing_times_real':



    def queryData(self,measures_name,measurement_name,t_query):


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


                p_timereal=pd.DataFrame(p_timereal.raw['series'][0]['values'],columns=['time','activity','measures','part_id','timelog','value'])
                p_timereal.loc[(p_timereal['measures']=="processing_time_real")]
                p_timereal=p_timereal.drop('time', axis='columns')
                p_timereal=p_timereal.drop('timelog', axis='columns')
                p_timereal=p_timereal.drop('measures', axis='columns')
                p_timereal['activity']=pd.to_numeric(p_timereal['activity']).astype(int)
                p_timereal['part_id']=pd.to_numeric(p_timereal['part_id']).astype(int)
                p_timereal['value']=pd.to_numeric(p_timereal['value']).astype(int)

                return p_timereal




    def writeData(self,measures_name,measurement_name,data):

        if measurement_name =='initialisation':

            init_pos=data
            json_init_pos=[{"measurement":"initialization","tags":{"measures":"initial_position"},"fields":{"list":str(init_pos['location'].tolist())}}]
            self.client.write_points(json_init_pos)

        if measurement_name == "real_perf":
            if measures_name=="processing_time_real":
                p_timereal=data
                json_p_timereal=[{"measurement":"real_perf","tags":{"measures":"processing_time_real"},"fields":{"list":str(init_pos['location'].tolist())}}]
                self.client.write_points(json_p_timereal)







