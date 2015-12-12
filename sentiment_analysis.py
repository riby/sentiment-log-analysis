# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:05:45 2015

@author: riby
"""

# import urllib
# data = urllib.urlencode({"text": "SERVICE ALERT: 4032-1-21;Fans;CRITICAL;SOFT;1;Couln't parse entry envMonFanStatusEntry.4.11  <type 'str'> 13107 "})
# u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
# the_page = u.read()
# print the_page

from textblob import TextBlob

#
# folder='upload'
#
fname='nagios-08-16-2015-00.log'
content=[]
with open(fname) as f:
    content = f.readlines()
d=[]
count =0
service_notification=[]
service_alert=[]
warning=[]

def printlist(lst):
    f=open("file.csv","a+")

    for l in lst:
        f.write(l+"\n")
        print l
for line in content:
    st=line.split(']')
    st2=st[1].strip().replace(';',',')
    st3=st2.replace(':',',')
    #print st
    st4=st3.split(',')
    if(st4[0]=="SERVICE NOTIFICATION"):
        service_notification.append(st3)
    elif(st4[0]=="SERVICE ALERT"):
        service_alert.append(st3)
    elif(st4[0]=="Warning"):
        warning.append(st3)



        # if count>2:
        #     break;
        # count+=count+1
        # # if(d.has_key("SERVICE NOTIFICATION")):
        #     d["SERVICE NOTIFICATION"]=d["SERVICE NOTIFICATION"]+st[3:]
        # else:
        #     d["SERVICE NOTIFICATION"]=st[3:]
        #print d
printlist(service_alert)
printlist(service_notification)
printlist(warning)





# def getSentimentBasedLogs(content):
#     final_content=[]
#     for line in content:
#         #if
#     testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")

# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# wiki.tags
#testimonial = TextBlob("SERVICE ALERT: 4032-1-21;Fans;CRITICAL;SOFT;1;Couln't parse entry envMonFanStatusEntry.4.11  <type 'str'> 13107")
#print testimonial.sentiment