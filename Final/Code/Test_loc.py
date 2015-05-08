import re
import os
count=1
rec_count=0
path = r'./tweets_locations'  # remove the trailing '\'
f1=open("tweets_loc_state/State_loc"+str(count)+".txt","w")
f2=open("tweets_loc_state_error/State_loc"+str(count)+".txt","w")
state_list=["alabama","alaska" ,"arizona", "arkansas", "california", "colorado","connecticut", "delaware","florida","georgia","hawaii","idaho","illinois", "indiana","iowa","kansas", "kentucky", "louisiana", "maine","maryland", "massachusetts", "michigan","minnesota", "mississippi", "missouri","montana","nebraska", "nevada","new hampshire", "new jersey","new mexico","new york","north carolina", "north dakota","ohio","oklahoma", "oregon","pennsylvania","rhode island","south carolina", "south dakota","tennessee","texas","utah","vermont", "virginia", "washington","west Virginia", "wisconsin", "wyoming"]
dict_state_code={"alabama" : "AL","alaska" : "AK","arizona" : "AZ","arkansas" : "AR","california" : "CA", "colorado" : "CO","connecticut" : "CT", "delaware" : "DE", "florida" : "FL", "georgia" : "GA","hawaii" : "HI","idaho" : "ID", "illinois" : "IL", "indiana" : "IN", "iowa" : "IA", "kansas" : "KS", "kentucky" : "KY", "louisiana" : "LA","maine" : "ME","maryland" : "MD", "massachusetts" : "MA", "michigan" : "MI","minnesota" : "MN","mississippi" : "MS", "missouri" : "MO","montana" : "MT","nebraska" : "NE","nevada" : "NV", "new hampshire" : "NH", "new jersey" : "NJ", "new mexico" : "NM","new york" : "NY","north carolina" : "NC", "north dakota" : "ND","ohio" : "OH","oklahoma" : "OK","oregon" : "OR","pennsylvania" : "PA", "rhode island" : "RI","south carolina" : "SC", "south dakota" : "SD","tennessee" : "TN", "texas" : "TX", "utah" : "UT", "vermont" : "VT", "virginia" : "VA", "washington" : "WA", "west Virginia" : "WV", "wisconsin" : "WI", "wyoming" : "WY"}
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
					i=0;
					#print(data)
					tweets=re.split("\t",data)
					if len(tweets) > 3:
						location=tweets[0]
						loc=location.lower()
						if loc in state_list:
							rec_count=rec_count+1
							if (rec_count==2500):
								count=count+1
								rec_count=0
								f1.close()
								f1=open("tweets_loc_state/State_loc"+str(count)+".txt","w")
							state_code=dict_state_code[loc]
							f1.write(str(state_code)+"\t"+str(tweets[1])+"\t"+str(tweets[2])+"\t"+str(tweets[3]));
						else:
							if location =="\n" or location.strip() == "":
								i=0
							else:
								f2.write(str(location.lower())+"\n");
f1.close()
f2.close()
print ("Done")
					
