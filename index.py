print('============= 小工具 =============');

import requests

import json

import src.libs.bee as bee


# 导入配置
screenerConfig    = bee.loadJson('config/screener.json')["screener"]
resoultKeysConfig = bee.loadJson('config/screener.json')["resoultKeys"]
industryConfig    = bee.loadJson('config/industryConfig.json')


timeout = 5000
url = "https://xueqiu.com/service/screener/screen"
cookie="_ga=GA1.2.1238256306.1553262607; device_id=fa8d269f088e08efef34f81cc48e9809; s=f714bdu2gg; bid=14761af1b15c70d493f9806c0cb1e0d8_jtk4kgj7; __utma=1.1238256306.1553262607.1553262802.1557328661.2; aliyungf_tc=AQAAAGH68xlEWgkA5GFI32hQdtFPGdoA; acw_tc=2760823f15836771946297920ef00e33eb53deb2cd89ab696578c61b59bc0a; xq_a_token=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xqat=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xq_r_token=01d9e7361ed17caf0fa5eff6465d1c90dbde9ae2; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4NTM2MjYwNywiY3RtIjoxNTgzNjc3MTM1ODMxLCJjaWQiOiJkOWQwbjRBWnVwIn0.lKRn8f-2k1lE2yyEne0zx5XbuZNiJBg4-YubeVyDLDi6NLHrSYq7dgLPUzccAhARnUaK9NYu0Qb5xLR2Sd4zFFH6fWLula5ioyZdfsyuvQf_vzUf_1fuA6op0HjVEZS_VVhmiJo_QNpcPtHj-P5kR9znBlkUplzd9w0ncZRcEVl4eR9EOetefG4yPEhzEZiqTtMOskBWUuKgpcPsZe4xEVmfKn1PXbHg-1rgxXtY1Rn9MvU8VHaQnvp0DghFgL99k_huc1QauT1pJRNdLR8RQxxIuH_iUtNKgHwkAm-QgKnyE7tvX1Jn7lH3e8bLZhFAUkuMdAR-veLoUORarFFQ2Q; u=441583677194637; cookiesu=731583677195569; Hm_lvt_1db88642e346389874251b5a1eded6e3=1583677196; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1583677196"
userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

def tranferParam(json):
    arr = [];
    for key in json:
        if(json[key]['active']):
            arr.append(key + '=' + str(json[key]['value']))
    return "&".join(arr);

param = tranferParam(screenerConfig)
print(param)

def getScreenerData(url,param):
    _headers = {
        "User-Agent":userAgent,
        "Cookie":cookie
    }
    _params = param;

    def myGet():
        res = requests.get(url=url,params=_params,headers=_headers,timeout=timeout)
        return res
    
    return myGet().text;

# 转化为 dict
data = json.loads(getScreenerData(url,param))



myList = data['data']['list']

for one in myList:
    for key in list(one):
        if key not in resoultKeysConfig['keys']:
            del one[key]

    # 追加数据
    if one['symbol'] in industryConfig:
        #print('键存在')
        one['industry'] =industryConfig[one['symbol']]['industry']
        one['industryId'] =industryConfig[one['symbol']]['id']
    else:
        #print('键不存在')
        one['industry'] = '未分类'
        one['industryId'] = 999

#print(json.dumps(myList))
print('符合数据条目')
print(data['data']['count'])
print('实际获取数据条目')
print(len(myList))

newList = sorted(myList, key=lambda x : x['industryId'])  
#print(json.dumps(newList))

# print(json.dumps(data['data']['list'][0]))


newDict = {};
for one in newList:
    if(one['industryId'] in newDict):
        newDict[one['industryId']].append(one)
    else:
        newDict[one['industryId']]=[];

#print(json.dumps(newDict[999]))
print(json.dumps(newDict))












