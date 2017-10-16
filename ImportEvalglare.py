# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:32:45 2017

@author: mkj
"""
#Starting evalglare and saves output to txt file
import os
os.system("C:\\Radiance\\bin\\evalglare.exe -d C:\\users\\mkj\\Dropbox\\GH\\RC\\1_BC_F1_S4_K8_9.clsky122116.pic > C:\\users\\mkj\\Dropbox\\GH\\RC\\RCvalues.txt")

#f=open("C:\\users\\mkj\\Dropbox\\GH\\RC\\RCvalues.txt","r")
#print(f.read())
#f.close()

GI=[]  #Glare impact
Ldata=[] #Luminance and illuminance values
VC=[] #visual comfort metrics 


#with open ("C:\\users\\mkj\\Dropbox\\GH\\RC\\RCvalues.txt", "r") as f :
#    for line in f :
#        GI.append(line)
#        line=GI[0]
#        for word in line.split():
#            print(word)

#Isolates one line from txt file and replaces blank space with comma
from itertools import islice
with open("C:\\users\\mkj\\Dropbox\\GH\\RC\\RCvalues.txt") as data:
    GS = list(islice(data,1,2))
GsD=[]
for i in GS: 
    j=str(i).replace(" ",(","))
    GsD.append(j)
    print(GsD)

