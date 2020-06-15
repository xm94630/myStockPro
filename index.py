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
cookie="s=dv17rhnbyu; __utmz=1.1583681158.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); u=651583681158535; device_id=50e744ebdafb4469ce4d5b0ab65539ba; aliyungf_tc=AQAAAMsVElikXQAArgr9cp45FRiy5LuS; acw_tc=2760822715921972580353678eaffe8592bce0223d199eb81503212cddf802; xq_a_token=ea139be840cf88ff8c30e6943cf26aba8ad77358; xq_r_token=863970f9d67d944596be27965d13c6929b5264fe; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5NDAwMjgwOCwiY3RtIjoxNTkyMTk3MjI3OTgyLCJjaWQiOiJkOWQwbjRBWnVwIn0.VyD31ij6_nJtSBTuCGE00S76WKVySkVLIWpDBnPWypeHNt7kiZeYmFzdoz9yKtj8EzeR6RqgalpeqeNlIC3dhhiUJZRLJn6_Lg_4aKQUvduK8S0P0zsNVbX4VMzrOEWmxKVoSAWmym2jTCEVFGFXzyfp4tY3-6kQZq1xy6vtbkKxLx-dgGkzu21erZYcK-FvSCqRlImLox8FwHNaPDCecVlEQJxx_8n1Scqn4IVsP9Li_mSKVMZE7W8-MJrrjQ9eS41i0bLBfzxXnlJXbVD_5Vy1n7q9X_7_61W-s0cIHqxscRnrbOjBGi9AnKwKmLlWnER2wnmBL8np2B4YOuKSnA; __utma=1.1591397118.1583681158.1583681158.1592197259.2; __utmc=1; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1592197264; __utmb=1.2.10.1592197259; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1592197342"
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












