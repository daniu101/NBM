#!/usr/bin/env python
# -*- coding: utf-8 

from numpy import * 

##得到每个特征的条件概率
def trainNB0(trainMatrix,trainCategory):###输入的文档信息和标签
    numTrainDocs = len(trainMatrix) # 所有语句list 长度
    numWords = len(trainMatrix[0]) # 第 0 个矩阵长度
    pAbusive = sum(trainCategory)/float(numTrainDocs) #屏蔽语句个数个数 / 总语句个数
    p0Num = ones(numWords)
    p1Num = ones(numWords)      
    p0Denom = 2.0
    p1Denom = 2.0                     
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          
    p0Vect = log(p0Num/p0Denom)   
    return p0Vect,p1Vect,pAbusive
