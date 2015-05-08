import json
import os
import re
import pandas as pd
file_name="State_Pos_Top5.tsv"
f=open(file_name,"r")
file_name_neg="State_Pos_Top5.tsv"
f_neg=open(file_name_neg,"r")
f_result=open("Final_State_Top5_Pos.csv","w")
f_result_neg=open("Final_State_Top5_Neg.csv","w")
dict_state_convert={"AL":"1","AK":"2","AZ":"4","AR":"5","CA":"6","CO":"8","CT":"9","DE":"11","FL":"12","GA":"13","HI":"15","ID":"16","IL":"17","IN":"18","IA":"19","KS":"20","KY":"21","LA":"22","ME":"23","MD":"24","MA":"25","MI":"26","MN":"27","MS":"28","MO":"29","MT":"30","NE":"31","NV":"32","NH":"33","NJ":"34","NM":"35","NY":"36","NC":"37","ND":"38","OH":"39","OK":"40","OR":"41","PA":"42","RI":"44","SC":"45","SD":"46","TN":"47","TX":"48","UT":"49","VT":"50","VA":"51","WA":"53","WV":"54","WI":"55","WY":"56"}

for line in f:
	#print line
	datas=re.split("\t",line)
	state=datas[0]
	state_value=dict_state_convert[state]
	f_result.write(str(state_value)+","+str(state)+","+str(datas[1])+","+datas[2])
f_result.close()

for line in f_neg:
	#print line
	datas=re.split("\t",line)
	state=datas[0]
	state_value=dict_state_convert[state]
	f_result_neg.write(str(state_value)+","+str(state)+","+str(datas[1])+","+datas[2])
f_result_neg.close()

