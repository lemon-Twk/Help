# _*_ coding: utf-8 _*_
"""
Time:     2022/11/1 12:49
Author:   Wang TianYu(Twklemon)
Version:  V 0.1
File:     数据批量拟合.py
Describe: Written during Fudan University, Github link: https://github.com/lemon-Twk/Help
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_excel("E:\HLEP\Surong\\0905-1.xls",sheet_name="Sheet3")#导入数据，自己改路径

'''flag=0
#如果是一行一列可以改用这部分的代码
time=len(data)/7
for i in range(time):
    start=flag*i
    end=flag*i+7'''

biaoxian=data.iloc[0:7]
times=biaoxian.shape[1]
X=biaoxian["浓度/峰面积"].to_numpy()
X_train=X[:,np.newaxis]
Result=[]
for i in range(1,times):
    result=[]
    Y=biaoxian.iloc[:,i].to_numpy()
    Y_train = Y[:, np.newaxis]
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    Y_pred = regr.predict(X_train)
    result.append(regr.coef_[0][0])
    result.append(regr.intercept_[0])
    result.append(r2_score(Y_train,Y_pred))
    Result.append(result)

Re=pd.DataFrame(data=Result,columns=["coef","intercept","r2"],index=biaoxian.columns.to_list()[1:])
Re.to_excel("标线计算结果.xlsx")
