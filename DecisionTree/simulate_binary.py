from sklearn import tree
import numpy as np
import scipy

currlist = ["USDJPY","USDEUR","USDGBP","EURJPY","EURGBP","GBPJPY"]
sample_num = 20
max_sample_range=550
min_later = 5

inittime = 600
endtime = 750



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
    if dataset1[sample_num+i+min_later,2] > dataset1[sample_num+i,2]:
        labels[i] = 1
    else:
        labels[i] = 0
pred_binary = tree.DecisionTreeClassifier()
pred_binary = pred_binary.fit(dataset, labels)

maxeval = 700

money = 0
bet = 20


countwins = 0
counter = 0
for i in np.arange(inittime,endtime,min_later):
    currdata = []
    for j in np.arange(sample_num,0,-1):
        data = np.zeros((len(currlist)), dtype=np.float)
        for k in range(0,len(currlist)):
            exec('data[k] = dataset'+str(k)+'[i-j,2]')
        currdata.append(data)
    currdata = np.reshape(currdata,(sample_num*len(currlist)))
    currdata = currdata.reshape(1,-1)
    prediction = pred_binary.predict(currdata)
    if dataset1[i+min_later,2] > dataset1[i,2]:
        reality = 1
    else:
        reality = 0
    if prediction == reality:
        countwins +=1
        money += bet*1.5
    else:
        money -= bet
    counter = counter+1

#print(money)
#print(countwins)
print(countwins/counter)
#print('tottiem =',endtime-inittime)
