from alchemyapi import AlchemyAPI
import json
import time
import requests
import sys
import os
import re
#import database as db
from time import gmtime, strftime

print("\n\nPROCESS STARTS AT: "+strftime("%Y-%m-%d %H:%M:%S")+"\n\n")


count=21

f1=open("tweets_alchemy/coordinate_"+str(count)+".txt","w")
#f2=open("../../../tweets_locations/location_"+str(count)+".txt","w")
alchemyapi = AlchemyAPI()
car_models=["LAMBORGHINI","CHRYSLER","GEO","APTERA","CHEVROLET","MASERATI","JEEP","KIA","HONDA","MERCURY","RAMBLER","HOLDEN","SATURN","MORGAN","LINCOLN","DODGE","CITROEN","LEXUS","MERCEDES-BENZ","DAIHATSU","VOLKSWAGEN","LAND ROVER","STUDEBAKER","TOYOTA","NISSAN","ACURA","BMW","ASTON MARTIN","HUMMER","FIAT","GMC","MITSUBISHI","LOTUS","FERRARI","EAGLE","TESLA","BENTLEY","INFINITI","FOOSE","PONTIAC","VOLVO","FILLMORE","ISUZU","SMART","BUGATTI","OLDSMOBILE","MAZDA","SAAB","SUZUKI","DAEWOO","MAYBACH","ALFA ROMEO","RAM","JENSEN","FORD","PLYMOUTH","AUSTIN","BUICK","ROLLS-ROYCE","SUBARU","JAGUAR","MCLAREN","P ORSCHE","MINI","SHELBY","SPYKER","PANOZ","HYUNDAI","SPYKER CARS","CADILLAC","AUDI","SCION"]
entity_type=["Automobile","Company"]
car_names=["NSX","A3 E-Tron","Q7","R8 V10","TT","X5 EDrive","CASCADA","TANG","CT6","CHEVY VOLT","CAMARO","CRUZE","MALIBU","SPARK","VOLT","500X","MUSTANG GT350","CIVIC CONCEPT","HR-V","PILOT","TUCSONT","Q60 COUPE CONCEPT","XF","OPTIMA","SORENTO","GS F","RX","MKX","CX-3","MX-5 MIATA","MAYBACH S600","GLE COUPE","METRIS","OUTLANDER","MAXIMA","TITAN","BOXSTER SPYDER","CONCEPT_ONE","IA","IM","FORTWO","MODEL X","MIRAI","RAV4","TACOMA","XC90","S60","XC90","PASSAT"]
#dict_model_make={"NSX" : "Acura","A3 e-Tron" : "Audi"};
dict_model_make={"NSX" : "Acura","A3 E-TRON" : "Audi","Q7" : "Audi","R8 V10" : "Audi","TT" : "Audi","X5 EDRIVE" : "BMW","CASCADA" : "Buick","TANG" : "BYD","CT6" : "Cadillac","CHEVY VOLT" : "Chevorlet","CAMARO" : "Chevrolet","CRUZE" : "Chevrolet","MALIBU" : "Chevrolet","SPARK" : "Chevrolet","VOLT " : "Chevrolet","500X" : "Fiat","MUSTANG GT350" : "Ford","CIVIC CONCEPT" : "Honda","HR-V" : "Honda","PILOT" : "Honda","TUCSONT" : "Hyundai","Q60 COUPE CONCEPT" : "Infiniti","XF" : "Jaguar","OPTIMA" : "Kia","SORENTO" : "Kia","GS F" : "Lexus","RX" : "Lexus","MKX" : "Lincoln","CX-3" : "Mazda","MX-5 MIATA" : "Mazda","MAYBACH S600" : "Mercedes","GLE COUPE" : "Mercedes","METRIS" : "Mercedes","OUTLANDER" : "Mitsubishi","MAXIMA" : "Nissan","TITAN" : "Nissan","BOXSTER SPYDER" : "Porsche","CONCEPT_ONE" : "Rimac","IA" : "Scion","IM" : "Scion","FORTWO" : "Smart","MODEL X" : "Tesla","MIRAI" : "Toyota","RAV4" : "Toyota","TACOMA" : "Toyota","XC90" : "Volvo","S60" : "Volvo","S60" : "Volvo","PASSAT" : "Volkswagen"};

def get_calls_left():
	URL = "http://access.alchemyapi.com/calls/info/GetAPIKeyInfo?apikey={}&outputMode=json".format(alchemyapi.apikey)
	response = requests.get(URL)
	call_info = json.loads(response.text)
	print call_info['dailyTransactionLimit']
	print call_info['consumedDailyTransactions']
	return int(call_info['dailyTransactionLimit'])-int(call_info['consumedDailyTransactions'])
calls_left = get_calls_left()
print calls_left

#car_models=["Lamborghini","Chrysler","Geo","Aptera","Chevrolet","Maserati","Jeep","Kia","Honda","Mercury","Rambler","Holden","Saturn","Morgan","Lincoln","Dodge","Citroen","Lexus","Mercedes-Benz","Daihatsu","Volkswagen","Land Rover","Studebaker","Toyota","Nissan","Acura","BMW","Aston Martin","HUMMER","Hummer","FIAT","GMC","Mitsubishi","Lotus","Ferrari","Eagle","Tesla","Bentley","Infiniti","Foose","Pontiac","Volvo","Fillmore","Isuzu","Smart","Bugatti","Oldsmobile","Mazda","Saab","Suzuki","Daewoo","Maybach","Alfa Romeo","Ram","Jensen","Ford","Plymouth","Austin","Buick","Rolls-Royce","Subaru","Jaguar","McLaren","Porsche","MINI","Shelby","Spyker","Panoz","Hyundai","Spyker Cars","Cadillac","Audi","Scion"]
path = r'./tweets_input/' 
for file_name in os.listdir(path):
	print file_name
	file_name_path = os.path.join(path, file_name)
	#print file_name_path
	if os.path.isfile(file_name_path):
		with open(file_name_path,"r") as data_file:
			while True:
				data=data_file.readline()
				if(data ==""):
					break
				if(data!="\n"):
					tweet=re.split("\t",data)
					state=tweet[0]
					text=tweet[1]
					#print text
					response_comb= alchemyapi.combined('text', text, {'sentiment': 1})
					if(response_comb['status'] == 'OK'):
						if('entities' in response_comb.keys()):
							#print "entities"
							flag=0
							for entity in response_comb['entities']:
								#print entity
								name = entity['text']
								type_ = entity['type']
								polarity= entity['sentiment']['type']
								name_words=re.split(" ",name)
								entity_count=entity['count']
								entity_relevance=entity['relevance']
								if('score' in entity['sentiment']):
									entity_sentiment = entity['sentiment']['score']
								else:
									entity_sentiment = '0.0'
								for x in name_words:
									if x.upper() in car_models:
										if type_ in entity_type:
											flag=1
											#print name
											#print type_
											f1.write(str(state)+"\t"+text+"\t"+str(name.upper())+"\t"+str(type_)+"\t"+str(polarity)+"\t"+str(entity_count)+"\t"+str(entity_sentiment)+"\t"+str(entity_relevance)+"\t"+str(tweet[2])+"\t"+str(tweet[3]))
											break																			
								if (flag == 0):
									if type_ in entity_type:
										for x in name_words:
											if(flag ==2):
												break;
											for s in car_names:
												if (x.upper() in s):
													flag=2;
													car_name=s.upper()
													#print car_name
													try:
														car_model=dict_model_make[car_name]
														#print ("S:" + car_name +"\t"+ car_model)
														f1 .write(str(state)+"\t"+text+"\t"+str(car_model.upper())+"\t"+str(type_)+"\t"+str(polarity)+"\t"+str(entity_count)+"\t"+str(entity_sentiment)+"\t"+str(entity_relevance)+"\t"+str(tweet[2])+"\t"+str(tweet[3]))
														break;	
													except:
														i=0;
														print car_name								

calls_left = get_calls_left()
print calls_left

print("done")


		
				
			
