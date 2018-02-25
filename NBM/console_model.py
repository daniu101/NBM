#!/usr/bin/env python
# -*- coding: utf-8 

from NBM.pre_data import *
from NBM.conditional_probability import *
from NBM.probability_classification import *

FILE_PATH =  "D:/5/"

# 加载每句话 和属性标签 label
listOPosts,listClasses = loadDataSet()
# 形成字典
myVocabList = createVocabList(listOPosts)

trainMat=[]
for postinDoc in listOPosts:
    myVocabListFeature = setOfWords2Vec(myVocabList, postinDoc) # 所有语句特征
    trainMat.append(myVocabListFeature) # 转List

# 把转好的所有语句特征List 和 属性标签Label 进行条件概率计算
p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
print(p0V)
print(p1V)
print(pAb)
# 需要判断的语句
testEntry = ['大量', '代开']
thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
