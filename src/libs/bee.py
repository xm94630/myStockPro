import json
import sys

# 读取json数据
# 返回dict类型数据
def loadJson(path):
    with open(path) as jsonFile:
        try:
            #正常读取
            return json.load(jsonFile)
        except:
            #发生异常
            print('读取的JSON格式有误')
            print('退出程序')
            sys.exit(0) 
