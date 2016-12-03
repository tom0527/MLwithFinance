import threading
from getdatafromyahoo import *
from pprint import pprint
import os.path

interval=60
def mainjob():
    print('outputting')
    currlist,ask,bid,rate,rateid,created =getrate()
    for i in range(0, len(currlist)):
        filename='./'+currlist[i]+'.dat'
        if os.path.isfile(filename):
            f1=open('./'+currlist[i]+'.dat', 'a')
            f1.write(ask[i]+'\t'+bid[i]+'\t'+rate[i]+'\t'+created[i]+'\n' )
        else :
            f1=open('./'+currlist[i]+'.dat', 'w+')
            f1.write('#ask\tbid \trate \tdate \n')
            f1.write(ask[i]+'\t'+bid[i]+'\t'+rate[i]+'\t'+created[i]+'\n')
        f1.close()
    ask = list(map(float, ask))
    bid = list(map(float, bid))
    rate = list(map(float, rate))
    
    threading.Timer(interval,mainjob).start()

mainjob()
