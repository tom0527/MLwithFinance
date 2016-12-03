from sklearn import tree
import numpy as np
import scipy
import matplotlib.pyplot as mpl

currlist = ["USDJPY","USDEUR","USDGBP","EURJPY","EURGBP","GBPJPY"]
sample_num = 60
max_sample_range=400
min_later = 5


sample_range = range(0,max_sample_range)

for i in range(0, len(currlist)):
    filename='./'+currlist[i]+'.dat'
    exec('dataset'+str(i)+' = np.loadtxt(filename,skiprows=1,usecols=range(0,3))')

dataset = []
for i in sample_range:
    sample = []
    for j in range(0,sample_num):
        data = np.zeros((len(currlist)), dtype=np.float)
        for k in range(0,len(currlist)):
            exec('data[k] = dataset'+str(k)+'[i,2]')
        sample.append(data)
    sample = np.reshape(sample,(sample_num*len(currlist)))
    dataset.append([sample])
dataset = np.squeeze(dataset)

labels = np.zeros(max_sample_range,dtype=np.int)
for i in sample_range:
    future_sell_val = dataset1[sample_num+i+min_later,0]
    current_ask_val = dataset1[sample_num+i,1]
    percent = float ((future_sell_val-current_ask_val)/current_ask_val)*100.
    if percent==0:
        labels[i] = 5
    elif percent > 0:
        if percent < 0.025:
            labels[i] = 6
        elif percent < 0.05:
            labels[i] = 7
        elif percent < 0.075:
            labels[i] = 8
        else:
            labels[i] = 9
    else :
        if percent > -0.025:
            labels[i] = 4
        elif percent > - 0.05:
            labels[i] = 3
        elif percent > -0.075:
            labels[i] = 2
        else:
            labels[i] = 1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataset, labels)

maxeval = 500
predict = np.zeros(maxeval,dtype=np.int)

for i in range(0,maxeval):
    sample = []
    for j in range(0,sample_num):
        data = np.zeros((len(currlist)), dtype=np.float)
        for k in range(0,len(currlist)):
            exec('data[k] = dataset'+str(k)+'[i,2]')
        sample.append(data)
    sample = np.reshape(sample,(sample_num*len(currlist)))
    sample = sample.reshape(1,-1)
    #sample = np.squeeze(sample)
    result = clf.predict(sample)
    predict[i]=result[0]

labels = np.zeros(maxeval,dtype=np.int)
for i in range(0,maxeval):
    future_sell_val = dataset1[sample_num+i+min_later,0]
    current_ask_val = dataset1[sample_num+i,1]
    percent = float ((future_sell_val-current_ask_val)/current_ask_val)*100.
    if percent==0:
        labels[i] = 5
    elif percent > 0:
        if percent < 0.025:
            labels[i] = 6
        elif percent < 0.05:
            labels[i] = 7
        elif percent < 0.075:
            labels[i] = 8
        else:
            labels[i] = 9
    else :
        if percent > -0.025:
            labels[i] = 4
        elif percent > -0.05:
            labels[i] = 3
        elif percent > -0.075:
            labels[i] = 2
        else:
            labels[i] = 1

#predict = np.array(map(int, predict))

labels = (labels-5)*0.025
predict = (predict-5)*0.025

print(np.std(predict-labels))
#mpl.plot(np.arange(0,len(predict)),labels,'r*')
#mpl.plot(np.arange(0,len(predict)),predict,'ko')
#mpl.show()
