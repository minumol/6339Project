import json
import os
import re
import pandas as pd
path = "tweet_output/"  
count=1
dict_state_perc={}
dict_state_pos_model={}
dict_state_neg_model={}
dict_state_pos_value={}
f_pos=open("State_Pos_Top5.tsv","w")
f_neg=open("State_Neg_Top5.tsv","w")
f_model_value=open("State_Model_value.csv","w")
f_model=open("State_Model.csv","w")
f_model_top=open("Model_state_Top5.tsv","w")
#f1=open("tweet_output/tweet_"+str(count)+".csv","w")
for file_name in os.listdir(path):
	print file_name
	file_name_path = os.path.join(path, file_name)
	if os.path.isfile(file_name_path):
		# Total tweets count
		df= pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['positive','neutral','negative'])]
		Count_DF=df.shape[0]
		total_tweet=Count_DF
		print "Count:" +str (total_tweet)
		#tweet count in each state
		df = pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['positive','neutral','negative'])]
		Count_DF=pd.DataFrame(df.groupby(['state']).polarity.count())
		Count_DF.columns = ['Count']
		Count_DF=Count_DF.reset_index().sort(columns=['state','Count'],ascending=False).set_index(Count_DF.index.names)
		for s in Count_DF.index:
			state=s
    			state_tweet=Count_DF.loc[s][0]
    			#print state_tweet
   			#print state_tweet+1
    			percentage=float(state_tweet*100)/total_tweet
    			#print s, percentage
    			dict_state_perc[s]=percentage;


    	#positive tweets of each model in each state
		df= pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['positive','neutral'])]
		Count_DF_pos=pd.DataFrame(df.groupby(['state','model']).polarity.count())
		Count_DF_pos.columns = ['Count']
		Count_DF_pos=Count_DF_pos.reset_index().sort(columns=['state','model','Count'],ascending=False).set_index(Count_DF_pos.index.names)
		for s in Count_DF_pos.index.levels[0]:
			model=Count_DF_pos.loc[s];
			#print model
    			for x in model.index:
    				#print x
    				count=Count_DF_pos.loc[s].loc[x]['Count']
    				state=s
    				model=x
        			dict_state_pos_model[s+","+x]=count

        #negative tweets of each model in each state
		df= pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['negative'])]
		Count_DF_neg=pd.DataFrame(df.groupby(['state','model']).polarity.count())
		Count_DF_neg.columns = ['Count']
		Count_DF_neg=Count_DF_neg.reset_index().sort(columns=['state','model','Count'],ascending=False).set_index(Count_DF_neg.index.names)		
		
		for s in Count_DF_neg.index.levels[0]:
			model=Count_DF_neg.loc[s]
    			#print model
    			for x in model.index:
    				count=Count_DF_neg.loc[s].loc[x]['Count']
    				state=s
    				model=x
        			#print s,x,model.loc[x]['Count']
        			dict_state_neg_model[s+","+x]=count



#Top 5 positive in each state
		df = pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['positive','neutral'])]
		Count_DF=pd.DataFrame(df.groupby(['state','model']).polarity.count())
		Count_DF.columns = ['Count']
		Count_DF=Count_DF.reset_index().sort(columns=['state','Count'],ascending=False).set_index(Count_DF.index.names)
		for s in Count_DF.index.levels[0]:
			top5Model=Count_DF.loc[s][:5]
			for x in top5Model.index:
				f_pos.write(str(s)+"\t"+str(x)+"\t"+str(top5Model.loc[x]['Count'])+"\n")


#Top 5 negative in each state
		df = pd.read_csv(file_name_path, low_memory=False)
		df=df[df.polarity.isin(['negative'])]
		Count_DF=pd.DataFrame(df.groupby(['state','model']).polarity.count())
		Count_DF.columns = ['Count']
		Count_DF=Count_DF.reset_index().sort(columns=['state','Count'],ascending=False).set_index(Count_DF.index.names)
		for s in Count_DF.index.levels[0]:
   			top5Model=Count_DF.loc[s][:5]
    			for x in top5Model.index:
        			#print s,x,top5Model.loc[x]['Count']
        			f_neg.write(str(s)+"\t"+str(x)+"\t"+str(top5Model.loc[x]['Count'])+"\n")


f_model_value.write("state"+","+"model"+","+"value"+"\n")
for state in dict_state_perc:
	percentage=dict_state_perc[state]
	for key in dict_state_pos_model:
		state_model=key
		pos_keys=re.split(",",key)
		if(state==pos_keys[0]):
			model=pos_keys[1]
			pos_count=dict_state_pos_model[key]
			if key in dict_state_neg_model:
				neg_count=dict_state_neg_model[key]
			else:
				neg_count=0
			value=pos_count-neg_count
			f_model_value.write(str(state)+","+str(model)+","+str(value)+"\n")

f_model_value.close()
#dict_state_perc={}
#dict_state_pos_model={}
#dict_state_neg_model={}

df = pd.read_csv("State_Model_value.csv", low_memory=False)
Count_DF=pd.DataFrame(df.groupby(['state','model']).value.sum().order(ascending=False))
for s in Count_DF.index.levels[0]:
    top5Model=Count_DF.loc[s][:1]
    for x in top5Model.index:
        f_model.write(str(s)+"\t"+str(x)+"\t"+str(top5Model.loc[x]['value'])+"\n")
f_model.close()

'''
df = pd.read_csv(file_name_path, low_memory=False)
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