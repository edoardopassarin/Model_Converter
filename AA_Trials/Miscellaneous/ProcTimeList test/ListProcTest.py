my_file = open("M1_proclist.txt", "r")
content = my_file.read()
my_file.close()
content_list = content.split("\n")
# res = int((''.join(content_list).rindex(' NaN'))/4 + 1)
# print((res))
# content_list = content_list[21:]
for i in range(0, len(content_list)):
    content_list[i] = int(content_list[i])
content_list.append(1000000)
print(type(content_list[-1]))
# import pandas as pd
# data_t = pd.read_csv('Processing_time_S1.txt', header=None)
# data = data_t.iloc[:,0]
# print(type(data))

# from manpy.simulation.ProcessingTimeList import ProcessingTimeList
# ciao = ProcessingTimeList("Processing_time_S1")
# a = ciao.obtainNumber()
# b = ciao.obtainNumber()
# print(a)
# print(b)
