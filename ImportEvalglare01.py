# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:32:45 2017

@author: mkj
"""
#Directions to folders containing .pic files / folder containing results / folder containing program
imageDir = "C:\\users\\mkj\\Desktop\\pic\\Pic\\"
destDir = "C:\\users\\mkj\\Desktop\\pic\\Data\\" 
glareDir = "C:\\Radiance\\bin\\"

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
    os.system(glareDir+"evalglare.exe -d "+imageDir+imageFiles[index]+" > "+destDir+imageFiles[index]+".EV_DataResult.txt 2>nul")
    print(imageFiles[index]+" done")
    print("----")



