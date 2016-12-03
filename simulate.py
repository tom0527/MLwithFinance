from sklearn import tree
import numpy as np
import scipy
import matplotlib.pyplot as mpl

currlist = ["USDJPY","USDEUR","USDGBP","EURJPY","EURGBP","GBPJPY"]
sample_num = 20
max_sample_range=500
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
            exec('data[k] = dataset'+str(k)+'[i+j,2]')
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

p_ask = tree.DecisionTreeClassifier()
p_ask = p_ask.fit(dataset, labels)

labels = np.zeros(max_sample_range,dtype=np.int)
for i in sample_range:
    future_ask_val = dataset1[sample_num+i+min_later,0]
    current_bid_val = dataset1[sample_num+i,1]
    percent = float ((future_ask_val-current_bid_val)/current_bid_val)*100.
    if percent==0:
        labels[i] = 5
    elif percent > 0:
        if percent < 0.025:
            labels[i] = 4
        elif percent < 0.05:
            labels[i] = 3
        elif percent < 0.075:
            labels[i] = 2
        else:
            labels[i] = 1
    else :
        if percent > -0.025:
            labels[i] = 6
        elif percent > - 0.05:
            labels[i] = 7
        elif percent > -0.075:
            labels[i] = 8
        else:
            labels[i] = 9

p_bid = tree.DecisionTreeClassifier()
p_bid = p_bid.fit(dataset, labels)

money = 0 #yen

bet = 100
rev = 10.0

moneyrev = bet*rev

inittime = 550
endtime = 700


countwins = 0
counter = 0
for i in np.arange(inittime,endtime,5):
    currdata = []
    for j in np.arange(sample_num,0,-1):
        data = np.zeros((len(currlist)), dtype=np.float)
        for k in range(0,len(currlist)):
            exec('data[k] = dataset'+str(k)+'[i-j,2]')
        currdata.append(data)
    currdata = np.reshape(currdata,(sample_num*len(currlist)))
    currdata = currdata.reshape(1,-1)
    pred_ask = p_ask.predict(currdata)
    pred_bid = p_bid.predict(currdata)
    if pred_ask>5:
        mbefore = money
        money += moneyrev*dataset1[i+min_later,1]-moneyrev*dataset2[i,0]
    elif pred_bid>5:
        mbefore = money
        money += -(moneyrev*dataset1[i,0]-moneyrev*dataset2[i+min_later,1])
    if mbefore < money:
        countwins = countwins+1
    counter = counter+1
print(money)
print(countwins)
print(countwins/counter)
