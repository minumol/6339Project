import json
import os
import re
import pandas as pd
file_name="Model_state_Top5.tsv"
f=open(file_name,"r")
f_result=open("Model_State_Top5.csv","w")
f_model_top=open("Final_Model_State_Top5.csv","w")
dict_state_convert={"AL":"1","AK":"2","AZ":"4","AR":"5","CA":"6","CO":"8","CT":"9","DE":"11","FL":"12","GA":"13","HI":"15","ID":"16","IL":"17","IN":"18","IA":"19","KS":"20","KY":"21","LA":"22","ME":"23","MD":"24","MA":"25","MI":"26","MN":"27","MS":"28","MO":"29","MT":"30","NE":"31","NV":"32","NH":"33","NJ":"34","NM":"35","NY":"36","NC":"37","ND":"38","OH":"39","OK":"40","OR":"41","PA":"42","RI":"44","SC":"45","SD":"46","TN":"47","TX":"48","UT":"49","VT":"50","VA":"51","WA":"53","WV":"54","WI":"55","WY":"56"}
car_models=["LAMBORGHINI","CHRYSLER","GEO","APTERA","CHEVROLET","MASERATI","JEEP","KIA","HONDA","MERCURY","RAMBLER","HOLDEN","SATURN","MORGAN","LINCOLN","DODGE","CITROEN","LEXUS","MERCEDES-BENZ","DAIHATSU","VOLKSWAGEN","LAND ROVER","STUDEBAKER","TOYOTA","NISSAN","ACURA","BMW","ASTON MARTIN","HUMMER","FIAT","GMC","MITSUBISHI","LOTUS","FERRARI","EAGLE","TESLA","BENTLEY","INFINITI","FOOSE","PONTIAC","VOLVO","FILLMORE","ISUZU","SMART","BUGATTI","OLDSMOBILE","MAZDA","SAAB","SUZUKI","DAEWOO","MAYBACH","ALFA ROMEO","RAM","JENSEN","FORD","PLYMOUTH","AUSTIN","BUICK","ROLLS-ROYCE","SUBARU","JAGUAR","MCLAREN","P ORSCHE","MINI","SHELBY","SPYKER","PANOZ","HYUNDAI","SPYKER CARS","CADILLAC","AUDI","SCION"]
f_result.write("state"+","+"model"+","+"polarity"+"\n")
path = "tweet_output/"  
#f1=open("tweet_output/tweet_"+str(count)+".csv","w")
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
					datas=re.split(",",data)
					model=datas[1]
					model_s=re.split(" ",model)
					for s in model_s:
						if s in car_models:
							f_result.write(str(datas[0])+","+str(s)+","+str(datas[2]))
							break;
f_result.close()

df = pd.read_csv("Model_State_Top5.csv", low_memory=False)
df=df[df.polarity.isin(['positive','neutral'])]
Count_DF_pos=pd.DataFrame(df.groupby(['model','state']).polarity.count())
Count_DF_pos.columns = ['Count']
Count_DF_pos=Count_DF_pos.reset_index().sort(columns=['model','Count'],ascending=False).set_index(Count_DF_pos.index.names)
#print(Count_DF_pos)
for s in Count_DF_pos.index.levels[0]:
    #print Count_DF_pos.loc[s]
    top5Model=Count_DF_pos.loc[s][:5]
    for x in top5Model.index:
        f_model_top.write(str(s)+"\t"+str(x)+"\t"+str(top5Model.loc[x]['Count'])+"\n")

f_model_top.close();

'''
for line in f:
	#print line
	datas=re.split("\t",line)
	model=datas[0]
	state=datas[1]
	state_code=dict_state_convert[state]
	model_s=re.split(" ",model)
	for s in model_s:
		if s in car_models:
			f_result.write(str(s)+","+str(state_code)+","+str(state)+","+str(datas[2]))
			break;
f_result.close();
'''

