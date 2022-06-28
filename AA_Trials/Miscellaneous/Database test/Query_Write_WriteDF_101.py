# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:08:00 2021

@author: franc
"""

client = InfluxDBClient(host=self.ip, port=self.port)
client.switch_database(self.DB_name)

#QUERY
eventlog= client.query('SELECT * FROM eventlog WHERE time >now()-10h',epoch='s')          
data=eventlog.raw                           
df=pd.DataFrame(data['series'][0]['values'],columns=['time','activity','id','type']) #Dataframe


#WRITE
init_pos=data
json_init_pos=[{"measurement":"initialization","tags":{"measures":"initial_position"},"fields":{"list":str(init_pos['location'].tolist())}}]
client.write_points(json_init_pos)


#WRITE DF
client = DataFrameClient(host="localhost", port=8086)
client.switch_database(NOME_DATABASE)

processing_time_test.set_index('TimeStamp', inplace = True)             

client.write_points(processing_time_test, "real_perf", tags={"measures": "processing_time_real"},tag_columns={'activity','part_id'},field_columns={'value'})

