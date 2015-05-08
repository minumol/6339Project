import json
import os
import re
import pandas as pd
file_name="State_Model.csv"
f=open(file_name,"r")
f_result=open("Final_State_Model_Value.csv","w")
dict_values={}
order_list=[53,30,16,38,27,23,26,55,41,46,33,50,36,56,19,31,25,17,42,9,44,6,49,32,39,18,34,8,54,29,20,10,24,51,21,11,4,40,35,47,37,48,5,45,1,13,28,22,12,15,2,72,78]
dict_state_convert={"AL":"1","AK":"2","AZ":"4","AR":"5","CA":"6","CO":"8","CT":"9","DE":"11","FL":"12","GA":"13","HI":"15","ID":"16","IL":"17","IN":"18","IA":"19","KS":"20","KY":"21","LA":"22","ME":"23","MD":"24","MA":"25","MI":"26","MN":"27","MS":"28","MO":"29","MT":"30","NE":"31","NV":"32","NH":"33","NJ":"34","NM":"35","NY":"36","NC":"37","ND":"38","OH":"39","OK":"40","OR":"41","PA":"42","RI":"44","SC":"45","SD":"46","TN":"47","TX":"48","UT":"49","VT":"50","VA":"51","WA":"53","WV":"54","WI":"55","WY":"56"}
'''
with open(file_name,"r") as data_file:
	while True:
		data=data_file.readline()
		print data
		if(data ==""):
			break
		if(data!="\n"):
			'''
for line in f:
	#print line
	datas=re.split("\t",line)
	state=datas[0]
	state_value=dict_state_convert[state]
	dict_values[state_value]=str(datas[0])+","+str(datas[1])+","+str(datas[2])

#print dict_values
for s in order_list:
	print s
	if str(s) in dict_values:
		result1=dict_values[str(s)];
		results=re.split(",",result1)
		result=str(results[0])+","+str(results[1])+","+str(results[2])
	else:
		result="NULL"+","+"NULL"+","+"0"+"\n";
	f_result.write(str(s)+","+result)
