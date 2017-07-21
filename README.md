# ZJMobileStorage
手机号数据存储比对功能 excel redis python
命令名称 sheetIndex 数据库ID（0-9)
importExcel 导入Excel数据信息到数据库 sheetIndex第几个sheet
sisMember 数据比较 不导入
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py importExcel info/1.xlsx 0 1
1
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py importExcel info/2.xlsx 0 2
2
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py importExcel info/3.xlsx 0 3
3
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py sisMember info/zonghe.xlsx 0 1
hasCount:199999
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py sisMember info/zonghe.xlsx 0 2
hasCount:388887
zhouj@ubuntu:~/Desktop/ZJMobileStorage$ python main.py sisMember info/zonghe.xlsx 0 3
hasCount:350209

