# _*_ coding: utf-8 _*_
"""
Time:     2022/11/2 19:11
Author:   Wang TianYu(Twklemon)
Version:  V 0.1
File:     e_to_E.py
Describe: Written during Fudan University, Github link: https://github.com/lemon-Twk/Help
"""
import os



path="E:\HLEP\\字母替换\\"
filename="man_aer(1).inp"
newpath="E:\HLEP\\字母替换\\"
newfilename="man_aer_1.inp"
inpfile=open(path+filename)
lines=inpfile.readlines()
inpfile.close()

for i in range(36,66):
    lines[i]=lines[i].replace("e","E")
for i in range(107,138):
    lines[i]=lines[i].replace("e","E")

newfile=open(path+newfilename,"w")
for newline in lines:
    newfile.write(newline)
newfile.close()
