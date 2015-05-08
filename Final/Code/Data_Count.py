import json
import os
import re
#import pandas as pd
path = "tweets_alchemy/"  
count=1
f1=open("tweet_output/tweet_"+str(count)+".csv","w")
f1.write("state"+","+"model"+","+"polarity"+"\n")
for file_name in os.listdir(path):
	print file_name
	file_name_path = os.path.join(path, file_name)
	if os.path.isfile(file_name_path):
		with open(file_name_path,"r") as data_file:
			while True:
				data=data_file.readline()
				if(data ==""):
					break
				if(data!="\n"):
					datas=re.split("\t",data)
					f1.write(str(datas[0])+","+str(datas[2])+","+str(datas[4])+"\n")
print ("done")


