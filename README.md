# ZJMobileStorage


手机号数据存储比对功能 excel redis python


命令名称 数据库ID（0-9)


importExcel 导入Excel数据信息到数据库 


sisMember 数据比较

#导入excel 文件位置在 info/1.xlsx  导入到数据库序号为0
python main.py importExcel info/1.xlsx 0

#比较excel数据 文件位置 info/zonghe.xlsx 被比较数据库为1
python main.py sisMember info/zonghe.xlsx 1

