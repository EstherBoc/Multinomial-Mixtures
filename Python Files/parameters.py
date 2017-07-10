import pandas as pd
import numpy as np
from nltk.stem.snowball import SnowballStemmer
import xlwt
from heapq import *
import matplotlib.pyplot as plt
import time


from EM import *
from cleaningData import *


B = 300
thresholdConvergence = 1
epsilonForInitialization = .01


df = pd.read_csv("NIPS_1987-2015.csv", sep=',', index_col = 0)
dfTranspose = df.transpose()
#print(dfTranspose)

data = extractSubDictionaryBasedOnProportions(dfTranspose, B)
n = float(data.sum().sum())
print(n)

indexes = nullArticlesIndexes(data)
data.drop(data.index[indexes], inplace = True)
dataClean = data.values


dateActuelle = time.localtime()
dateActuelle = time.strftime("%d %b %Y %H-%M-%S", dateActuelle)


style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()


for k in range(41,80,5):


    print ("NEW NUMBER OF CLUSTERS : " ,k)
    P,Pi,Rpost,logScore,logScores = expectationMaximisation2(dataClean, k, len(data), B, thresholdConvergence,epsilonForInitialization, 200)
    K, P, Pi, Rpost,logScore,logScores = readjustEM(dataClean, len(data), B, P, Pi,Rpost, logScore, logScores, thresholdConvergence, epsilonForInitialization, 200)
    

    if K == 31:
        wsPi = wb.add_sheet('Pi estimate')
        wsP = wb.add_sheet('P estimate')
        wsR = wb.add_sheet('R estimate')
        wslogScore = wb.add_sheet('logScore')


        Rt = R.transpose()
        wslogScore.write(0,0,logScore)
        wb.save("Parameters K="+str(K)+".xls")

        for k in range(len(P)):
            for j, b in enumerate(P[k]):
                wsP.write(j,k,float(b))
            #print(j,k,b)
        wb.save("Parameters K="+str(K)+".xls")

        for i,pi in enumerate(Pi):
            wsPi.write(i,0,float(pi))
        wb.save("Parameters K="+str(K)+".xls")


        for k in range(len(Rt)):
            for j, r in enumerate(Rt[k]):
                #print(j,k,float(r))
                wsR.write(j,k,float(r))
        wb.save("Parameters K="+str(K)+".xls")
        break




