import threading
from getdatafromyahoo import *
from pprint import pprint

interval=60
current_money = 10000
init_bid = 10000
askorbid = 1 #(ask=0 bid=1)

def mainjob():
    ask,bid,rate,rateid,created =getrate()
    ask = list(map(float, ask))
    bid = list(map(float, bid))
    rate = list(map(float, rate))

    threading.Timer(interval,mainjob).start()

mainjob()
