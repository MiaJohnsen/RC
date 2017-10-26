# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:04:00 2017

@author: mkj
"""

#Directions to folders containing .pic files / folder containing results / folder containing program
imageDir = "C:\\users\\mkj\\Desktop\\Relativecontrast\\Pic\\"
destDir = "C:\\users\\mkj\\Desktop\\Relativecontrast\\Data\\" 
folderDir = "C:\\users\\mkj\\Desktop\\Relativecontrast\\"
evalglareDir = "C:\\Radiance\\bin\\"
glareDir="C:\\users\\mkj\\Desktop\\Relativecontrast\\GS\\"
averageDir="C:\\users\\mkj\\Desktop\\Relativecontrast\\AV\\"

#Printing filenames inside .pic folder
import os
os.system("dir "+imageDir+"*.pic /b > "+destDir+"imageFiles.txt")

from time import sleep 
sleep(0.25) 

f=open(destDir+"imageFiles.txt","r")
imageFiles = f.read().splitlines()
f.close()

#Deleting old files
os.system("del "+destDir+"*.txt > nul")
sleep(1.0)

#Looping through files in image folder
for index in range (0,len(imageFiles)):
    os.system(evalglareDir+"evalglare.exe -d "+imageDir+imageFiles[index]+" > "+destDir+imageFiles[index]+".EV_DataResult.txt 2>nul")
    print(imageFiles[index]+" done")
    print("----")

os.system("dir "+destDir+"*.txt /b > "+folderDir+"txtFiles.txt")

from time import sleep
sleep(0.3)

 
f= open(folderDir +"txtFiles.txt","r")
txtFiles= f.read().splitlines()
f.close()


for index in range(0,len(txtFiles)): 
 g= open(destDir+txtFiles[index],"r")
 linesg= g.read().splitlines()
 g.close()
 k= open(averageDir+txtFiles[index]+".avg.txt","w")
 lineLast= linesg[len(linesg)-1]
 items= lineLast.split(" ")
 headLine= items[0].replace(","," ")
 headLine= headLine.replace(":","")
 k.write(headLine+'\n')
 items= lineLast.split(":") 
 data= items[1].replace(" ","",1)
 k.write(data+"\n")

 k.close()
 m= open(glareDir+txtFiles[index]+".glare.txt","w")
 for index2 in range(1,len(linesg)-1):
  m.write(linesg[index2]+"\n")
 m.close()
print('færdig')
