# _*_ coding: utf-8 _*_
"""
Time:     2022/11/6 15:35
Author:   Wang TianYu(Twklemon)
Version:  V 0.1
File:     mpi文件替换.py
Describe: Written during Fudan University, Github link: https://github.com/lemon-Twk/Help
"""
import pandas as pd
import numpy as np
import os

def read_dat():
    filename="E:\HLEP\思雨\数据替换\mon01lat35n.mpi"

    f_read1 = open(filename, 'r')
    f_read2 = f_read1.readlines()
    f_read3 = [line.strip('\n').split() for line in f_read2]
    ftot_t = []
    for i in range(len(f_read3)):
        ftot_t.append(f_read3[i])
    p=pd.DataFrame(data=ftot_t[1:],columns=ftot_t[0])
    #re=p[["Date","Time","HCHO_VCD(molec/cm^2)","err_HCHO_VCD"]]
    re=p
    return re
    '''except:
        print("this tning is none")'''
filename="E:\HLEP\思雨\数据替换\mon01lat35n.mpi"

f_read1 = open(filename, 'r')
f_read2 = f_read1.readlines()
f_read_uesful=f_read2[2:]
f_read3 = [line.strip('\n').split() for line in f_read_uesful]
ftot_t = []
for i in range(len(f_read3)):
    ftot_t.append(f_read3[i])
p=pd.DataFrame(data=ftot_t[1:],columns=ftot_t[0])
#re=p[["Date","Time","HCHO_VCD(molec/cm^2)","err_HCHO_VCD"]]

desired_data=np.loadtxt("E:\HLEP\思雨\数据替换\LL.txt")

for i in range(len(desired_data)):
    p.iloc[-i,5]=desired_data[-i,0]

re=p.to_numpy().tolist()
re_p=[]
for i in re:
    re_p.append(" ".join(i))


result=[line.strip('\n') for line in f_read2[:3]]+re_p

str='\n'
f=open("hesiyu.mpi","w")
f.write(str.join(result))
f.close()
