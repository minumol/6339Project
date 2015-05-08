import json
import os
import re
import math
path=r"./tweets_coordinates/"
count=1
rec_count=0
f1=open("tweets_co_state/state"+str(count)+".tsv","w")
f2=open("tweets_co_state_error/state"+str(count)+".tsv","w")
dict_geo_code={'HI':'{19,25,-155,-168}','FL':'{25,31,-80,-87}','TX':'{26,36,-94,-107}','LA':'{29,33,-89,-94}','AL':'{30,35,-85,-88}','AR':'{30,36,-90,-98}','MS':'{30,35,-88,-91}','AZ':'{31,37,-109,-115}','GA':'{31,35,-81,-86}','TN':'{31,37,-84,-90}','NM':'{32,37,-103,-109}','SC':'{32,35,-79,-83}','CA':'{33,42,-114,-124}','NC':'{34,37,-75,-84}','OK':'{34,37,-94,-103}','NV':'{35,42,-114,-120}','CO':'{37,41,-102,-109}','IL':'{37,42,-88,-91}','KS':'{37,40,-95,-102}','KY':'{37,39,-82,-90}','WV':'{37,41,-78,-83}','MO':'{37,41,-89,-96}','UT':'{37,42,-109,-114}','VA':'{37,39,-75,-83}','DE':'{38,40,-75,76}','MD':'{38,40,-75,-79}','OH':'{38,42,-81,-85}','NJ':'{39,41,-74,-76}','IA':'{40,43,-90,-97}','NE':'{40,43,-95,-104}','PA':'{40,42,-75,-81}','CT':'{41,42,-72,-74}','MA':'{41,43,-70,-73}','WY':'{41,45,-104,-111}','NY':'{41,45,-72,-80}','RI':'{41,42,-71,-72}','ID':'{42,49,-111,-117}','MI':'{42,47,-82,-90}','OR':'{42,46,-117,-125}','VT':'{42,45,-72,-73}','ME':'{43,47,-67,-71}','WI':'{43,47,-87,-93}','NH':'{43,45,-71,-73}','SD':'{43,48,-96,-104}','MN':'{44,49,-90,-97}','MT':'{45,49,-104,-116}','WA':'{46,49,-117,-125}','ND':'{46,49,-97,-104}','AK':'{52,71,-130,-177}','IN':'{85,88,38,42}'}
for file_name in os.listdir(path):
	file_name_path = os.path.join(path, file_name)
	if os.path.isfile(file_name_path):
		with open(file_name_path,"r") as data_file:
			while True:
				data=data_file.readline()
				if(data ==""):
					break
				if(data!="\n"):
					m=re.split("\t",data)
					if m[0] is not None:
						geocode=re.split(",",m[0])
						lattitude= int(math.floor(float(geocode[1].replace(']',''))))
						longitude= int(math.floor(float(geocode[0].replace('[',''))))
						#print(str(lattitude)+" "+str(longitude))
						if len(m) > 3:
							for key, value in dict_geo_code.items():
								geo_range_val=(value.replace('{',"")).replace('}',"")
								geo_range=re.split(",",geo_range_val)
								low_lat=int(geo_range[0])
								high_lat=int(geo_range[1])
								low_lon=int(geo_range[3])
								high_lon=int(geo_range[2])
								#print (str(low_lat)+" "+str(high_lat)+" "+str(low_lon)+" "+str(high_lon));
								flag=0
								if(lattitude >= low_lat and lattitude <= high_lat and longitude >=low_lon and longitude <=high_lat):
									rec_count =rec_count +1
									flag=1
									if (rec_count ==2500):
										rec_count =0
										count=count+1
										f1.close();
										f1=open("tweets_co_state/state"+str(count)+".tsv","w")
									state=key
									f1.write(str(state)+"\t"+ str(m[1])+"\t"+ str(m[2])+"\t"+ str(m[3]));
									break								
						else:
							print("length less:")
						if flag ==0:
							f2.write(data);
f1.close();
f2.close();							
print("done")
