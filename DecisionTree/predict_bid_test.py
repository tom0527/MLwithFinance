from sklearn import tree
import numpy as np
import scipy

currlist = ["USDJPY","USDEUR","USDGBP","EURJPY","EURGBP","GBPJPY"]
sample_num = 100
max_sample_range=300
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
    if dataset1[sample_num+i+min_later,1] < dataset1[sample_num+i,0]:
        labels[i] = 1
    else:
        labels[i] = 0
clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataset, labels)

maxeval = 350
predict = []

for i in range(0,maxeval):
    sample = []
    for j in range(0,sample_num):
        data = np.zeros((len(currlist)), dtype=np.float)
        for k in range(0,len(currlist)):
            exec('data[k] = dataset'+str(k)+'[i+j,2]')
        sample.append(data)
    sample = np.reshape(sample,(sample_num*len(currlist)))
    sample = sample.reshape(1,-1)
    #sample = np.squeeze(sample)
    result = clf.predict(sample)
    predict.append(result[0])

labels = np.zeros(maxeval,dtype=np.int)
for i in range(0,maxeval):
    if dataset1[sample_num+i+min_later,1] < dataset1[sample_num+i,0]:
        labels[i] = 1
    else:
        labels[i] = 0

predict = list(map(int, predict))
print(np.count_nonzero(predict-labels))
