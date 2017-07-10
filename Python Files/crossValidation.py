import pandas as pd
import numpy as np
from nltk.stem.snowball import SnowballStemmer
import xlwt
from heapq import *
import matplotlib.pyplot as plt
import csv

from EM import *


def extractsMostFrequentWords(dfTranspose, B):
    wordOccurrences =  dfTranspose.sum(0)
    wordOccurrences = wordOccurrences.nlargest(B)
    usedWords = list(wordOccurrences.index.values)
    data = dfTranspose.ix[:, usedWords]
    return data

def nullArticlesIndexes(Df):
    indexes = []  
    for i in range(len(Df)):
        #print sum(Df.ix[i,])
        if sum(Df.ix[i,]) == 0:
            #print "Null row"
            print (i)
            indexes.append(i)
    return indexes

def perc(row):
    lenDoc = sum(row)
    #print lenDoc
    if lenDoc == 0:
        print ("Warning: this document is inexistant")
    return [(u + (1/n))/ (float(lenDoc)+  B/n) for u in row]



B = 300
thresholdConvergence = 1
epsilonForInitialization = .01
deltaInit = 0
percentageTrain = .6



df = pd.read_csv("NIPS_1987-2015.csv", sep=',', index_col = 0)
dfTranspose = df.transpose()
data = extractsMostFrequentWords(dfTranspose, B)
n = float(data.sum().sum())
indexes = nullArticlesIndexes(data)
data.drop(data.index[indexes], inplace = True)

sizeTrain = int(percentageTrain * len(data))




testLL = []
csvfile = "logLikelihoodTest.csv"

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for k in range(1,100, 5):
        print ("New number of clusters ! ")
        testLLk = []
        for i in range(10):
            print ("New running of EM with ", str(k), " clusters")
            trainIndexes = random.sample(range(len(data)), sizeTrain)
            dataTrain = data.ix[trainIndexes]
            
            testIndexes = [i for i in range(len(data)) if i not in trainIndexes]
            dataTest = data.ix[testIndexes]
            
            P,Pi,Rpost,logScore,logScores = expectationMaximisation2(dataTrain.values, k, len(dataTrain), B, thresholdConvergence,epsilonForInitialization, 200)
            llTestk_At_i = logLikelihood(k, len(dataTest), B, P, Pi, dataTest.values)
            testLLk.append(llTestk_At_i)
            
        testLL.append(np.mean([value for value in testLLk if not np.isnan(value)]))


        
        writer.writerow([k, testLL[(len(testLL) - 1)]])








