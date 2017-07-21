#!usr/bin/python
#coding=utf-8
import sys,random
import redis
import time
from excelio import *

#config set stop-writes-on-bgsave-error no
pool = redis.ConnectionPool()
rdb = None
#rdb = redis.Redis(host='localhost',port=6379,connection_pool = pool,db=0)

def main(fun,param):
    if fun == 'test':
        test(int(param[0]))
    elif fun == 'importExcel':
        importExcel(param[0],int(param[1]),int(param[2]))
    elif fun == 'sisMember':
        sisMember(param[0],int(param[1]),int(param[2]))

def importExcel(fileName,sheetIndex = 0,dbIndex = 0):
    rdb = redis.Redis(host='localhost',port=6379,db=dbIndex)
    data = open_excel(fileName)
    table = data.sheets()[sheetIndex]
    rows = table.nrows
    for r in range(1,rows):
        row = table.row_values(r)
        if row:
            v = str(int(row[0]))
            rdb.set(v,0)
    rdb.save()
    print dbIndex

def sisMember(fileName,sheetIndex = 0,db = 0):
    rdb = redis.Redis(host='localhost',port=6379,db=db)
    data = open_excel(fileName)
    table = data.sheets()[sheetIndex]
    rows = table.nrows
    dict = {}
    hasCount = 0
    for r in range(1,rows):
        row = table.row_values(r)
        if row:
            v = str(int(row[0]))
            if rdb.get(v) != None:
                hasCount += 1
    print 'hasCount:' + str(hasCount)

def test(count):
    rdb = redis.Redis()
    time1 = time.time()
    print count
    lst = ['139','188','185','136','155','135','158','151','152','153']
    s = '0123456789'
    for i in range(count):
        mobile = random.choice(lst) + ''.join(random.choice(s) for i in range(8))
        rdb.set(mobile,0)
        if i % 1000 == 0:
            subtime = time.time() - time1 #从开始到现在的时间秒数
            needCount = subtime *1000
            if i > needCount:
                count = i-needCount
                time.sleep(count/1000)
            print i
    print time.time()-time1



if __name__ == '__main__':
    if(len(sys.argv) > 2):# main.py importExcel a,b,c,d,e
        fun = sys.argv[1]
        param = sys.argv[2:]
        main(fun,param)
    else:
        pass
