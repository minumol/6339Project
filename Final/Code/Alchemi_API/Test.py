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

#connector = db.connect()
count=1
#limit1 = sys.argv[1]
coordinate_file_name = "/tweets_coordinates/coordinate_"+str(count)+".tsv"
location_file_name = "/tweets_locations/location_"+str(count)+".tsv"

f1=open("tweets_coordinates/coordinate_"+str(count)+".txt","w")
f2=open("tweets_locations/location_"+str(count)+".txt","w")
alchemyapi = AlchemyAPI()
car_models=["Lamborghini","Chrysler","Geo","Aptera","Chevrolet","Maserati","Jeep","Kia","Honda","Mercury","Rambler","Holden","Saturn","Morgan","Lincoln","Dodge","Citroen","Lexus","Mercedes-Benz","Daihatsu","Volkswagen","Land Rover","Studebaker","Toyota","Nissan","Acura","BMW","Aston Martin","HUMMER","Hummer","FIAT","GMC","Mitsubishi","Lotus","Ferrari","Eagle","Tesla","Bentley","Infiniti","Foose","Pontiac","Volvo","Fillmore","Isuzu","Smart","Bugatti","Oldsmobile","Mazda","Saab","Suzuki","Daewoo","Maybach","Alfa Romeo","Ram","Jensen","Ford","Plymouth","Austin","Buick","Rolls-Royce","Subaru","Jaguar","McLaren","Porsche","MINI","Shelby","Spyker","Panoz","Hyundai","Spyker Cars","Cadillac","Audi","Scion"]
entity_type=["Automobile","Company"]

def get_calls_left():
	URL = "http://access.alchemyapi.com/calls/info/GetAPIKeyInfo?apikey={}&outputMode=json".format(alchemyapi.apikey)
	response = requests.get(URL)
	call_info = json.loads(response.text)
	print call_info['dailyTransactionLimit']
	print call_info['consumedDailyTransactions']
	return int(call_info['dailyTransactionLimit'])-int(call_info['consumedDailyTransactions'])
#calls_left = get_calls_left()
#print calls_left

#car_models=["Lamborghini","Chrysler","Geo","Aptera","Chevrolet","Maserati","Jeep","Kia","Honda","Mercury","Rambler","Holden","Saturn","Morgan","Lincoln","Dodge","Citroen","Lexus","Mercedes-Benz","Daihatsu","Volkswagen","Land Rover","Studebaker","Toyota","Nissan","Acura","BMW","Aston Martin","HUMMER","Hummer","FIAT","GMC","Mitsubishi","Lotus","Ferrari","Eagle","Tesla","Bentley","Infiniti","Foose","Pontiac","Volvo","Fillmore","Isuzu","Smart","Bugatti","Oldsmobile","Mazda","Saab","Suzuki","Daewoo","Maybach","Alfa Romeo","Ram","Jensen","Ford","Plymouth","Austin","Buick","Rolls-Royce","Subaru","Jaguar","McLaren","Porsche","MINI","Shelby","Spyker","Panoz","Hyundai","Spyker Cars","Cadillac","Audi","Scion"]
path = r'./tweets_text/' 
for file_name in os.listdir(path):
	#print file_name
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
					coordinates=tweet[0]
					text=tweet[1]
					print text
					f2.write(text+"\t"+str(tweet[0])+"\t"+str(tweet[2]))
print("Done")
