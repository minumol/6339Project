import os
import re
count=0
loc_rec_count=0
co_rec_count=0
loc_count=1
co_count=1
#limit1 = sys.argv[1]
f1=open("tweets_coordinates/coordinate_"+str(co_count)+".txt","w")
f2=open("tweets_locations/location_"+str(loc_count)+".txt","w")
path = r'./tweet_text/' 
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
					#print text
					if len(tweet)> 4:
						text=tweet[1]
						if coordinates == "None":
							loc_rec_count =loc_rec_count +1
							if (loc_rec_count ==2500):
								loc_rec_count =0
								loc_count=loc_count+1
								f2.close();
								f2=open("tweets_locations/location_"+str(loc_count)+".txt","w")
								#f1.write(text.decode('utf-8'))
							print("None")
							f2.write(str(tweet[3])+"\t"+text+"\t"+str(unicode(tweet[2]).encode('utf-8'))+"\t"+str(tweet[4]))
						else:
							co_rec_count =co_rec_count +1
							if (co_rec_count ==2500):
								co_rec_count =0
								co_count=co_count+1
								f1.close();
								f1=open("tweets_coordinates/coordinate_"+str(co_count)+".txt","w")
							print("Not None")
							#f2.write(unicode(text.replace("\n"," ")).encode('utf-8'))
							f1.write(str(tweet[0])+"\t"+text+"\t"+str(unicode(tweet[2]).encode('utf-8'))+"\t"+str(tweet[4]))
							
print("done")
