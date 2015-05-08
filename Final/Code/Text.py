import json
import os
path = r'./tweets'  # remove the trailing '\'
count=1
rec_count=0
text_count=0
f1=open("tweet_text/tweet_"+str(count)+".json","w")
for file_name in os.listdir(path):
	print file_name
	file_name_path = os.path.join(path, file_name)
	if os.path.isfile(file_name_path):
		with open(file_name_path,"r") as data_file:
			text_count=0
			while True:
				data=data_file.readline()
				if(data ==""):
					break
				if(data!="\n"):
					text_count=text_count+1
					#print(file_name_path)
					#print(text_count)
					#print(data)
					result=json.loads(data,encoding="utf-8")
					#result1=data.json()
					try: 
						coordinates = None
						#print(result)
						#print(file_name_path)
						#print(text_count)
						#print json.dumps(result,sort_keys=True,indent=4)
						if( result.get('coordinates')):
							#print result;
							coordinates = result['coordinates']
						location= str(unicode(result['user']['location']).encode('utf-8'))
						location1=result['user']["location"]	
						#print location;
						#print unicode(location).encode('utf-8')
						#if coordinates is not None or (location is not None and str(unicode(location).encode('utf-8'))):
						if coordinates is not None or location1 is not None :
							rec_count=rec_count+1
							date = result['created_at']
							text = result['text']
							retweet_count=result['retweet_count']
							if coordinates is not None:
								coordinates=result['coordinates']['coordinates']
							if (rec_count==2500):
								f1.close();
								count=count+1
								rec_count=1
								f1=open("tweet_text/tweet_"+str(count)+".json","w")
							f1.write(str(unicode(coordinates).encode('utf-8'))+"\t"+unicode(text.replace("\n"," ")).encode('utf-8')+"\t"+str(unicode(date).encode('utf-8'))+"\t"+unicode(location).encode('utf-8')+"\t"+str(retweet_count)+"\n")
					except Exception as ex:
						i = 0
						#print("invalid JSON")
						#print ex
f1.close();
print("done")
