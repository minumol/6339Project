# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:52:33 2015

@author: Tijo
"""

from pygeocoder import Geocoder
import re
import time
file_name=r"..\data\Tweet.tsv"
out_file=r"..\data\Tweet_loc.tsv"
f=open(out_file,"w")
with open(file_name, 'r') as my_file:
    while True:
        f=open(out_file,"a")
        line = my_file.readline()
        m=re.split("\t",line)
        if len(m) > 3:
            geocode=m[0]
            state1="None"
            country1="None"
            state="None"
            country="None"
            location = "test"
            if geocode != "None":
                geo=re.split(",",geocode)
                if len(geo) == 2:
                    geo1=geo[0].replace('[','')
                    geo2=geo[1].replace(']','')
                    geo_co1=float(geo1)
                    geo_co2=float(geo2)
                #geo_co2=float(geo2)
                    try:
                        result=Geocoder.reverse_geocode(geo_co1, geo_co2)
                        state=str(unicode(result.state).encode('utf-8'))
                        country=str(unicode(result.country).encode('utf-8'))                    
                    except Exception, e:
                        print "Failed Error: " + str(e)
                        state="None"
                        country="None"
            
            #print len(m)
            location=m[3]
            try:
                result1=Geocoder.geocode(location)
                state1=str(unicode(result1.state).encode('utf-8'))
                country1=str(unicode(result1.country).encode('utf-8'))
            except Exception, e:
                print "Failed Error: " + str(e)
                state1="None"
                country1="None"
            print state + " " + country + " " + state1 + " " + country1 + " Location: " + location
            if country != "None":
                f.write(state+"\t"+m[1]+"\t"+m[2]+"\t"+country+"\n")
            else:
                f.write(state1+"\t"+m[1]+"\t"+m[2]+"\t"+country1+"\n")
            f.close()
            time.sleep(1)

         
