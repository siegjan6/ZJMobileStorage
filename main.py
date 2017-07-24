#!usr/bin/python
#coding=utf-8
import sys,random
import redis
import time
from excelio import *

#1048575 *.xlsx 最大表格行数
#config set stop-writes-on-bgsave-error no 关闭自动快照
pool = redis.ConnectionPool()
rcon = None
#rcon = redis.Redis(host='localhost',port=6379,connection_pool = pool,db=0)

def main(fun,param):
    if fun == 'test':
        test(int(param[0]))
    elif fun == 'importExcel':
        importExcel(param[0],int(param[1]),int(param[2]))
    elif fun == 'sisMember':
        sisMember(param[0],int(param[1]),int(param[2]))

def importExcel(fileName,dbIndex = 0):
    sheetIndex = 0
    startTime = time.time()
    print startTime

    rcon = redis.Redis(host='localhost',port=6379,db=dbIndex)
    pipe = rcon.pipeline()
    print '读取excel表格，请把数据放置第一个sheet的第0列位置,并删除其他sheet'
    data = open_excel(fileName)
    table = data.sheets()[sheetIndex]
    rows = table.nrows
    print 'excel读取完毕，正在缓存数据到redis管道'
    for r in range(0,rows):
        row = table.row_values(r)
        if row:
            v = str(int(row[0]))
            print v
            pipe.set(v,0)
        if r != 0 and r % 300000 == 0:
            print '缓存到,第:' + str(r) + '条数据'
            pipe.execute()
    print '缓存结束，写入到redis内存数据库'
    pipe.execute()
    print 'redis数据库保存到硬盘'
    rcon.save()
    print '成功操作完毕'

def sisMember(fileName,db = 0):
    sheetIndex = 0
    rcon = redis.Redis(host='localhost',port=6379,db=db)
    print '读取excel表格，请把数据放置第一个sheet的第0列位置,并删除其他sheet'
    data = open_excel(fileName)
    table = data.sheets()[sheetIndex]
    rows = table.nrows
    dict = {}
    hasCount = 0
    print '开始比对'
    for r in range(0,rows):
        row = table.row_values(r)
        if row:
            v = str(int(row[0]))
            if rcon.get(v) != None:
                hasCount += 1
                print '重复个数:' + str(hasCount)
    print '比对完成'

def test(count):
    rcon = redis.Redis()
    time1 = time.time()
    print count
    lst = ['139','188','185','136','155','135','158','151','152','153']
    s = '0123456789'
    for i in range(count):
        mobile = random.choice(lst) + ''.join(random.choice(s) for i in range(8))
        rcon.set(mobile,0)
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
