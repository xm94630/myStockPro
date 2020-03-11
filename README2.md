# 核心接口

## 老版接口
### 筛选接口
https://xueqiu.com/stock/screener/screen.json?category=SH&order=desc&orderby=follow7d&size=10

## 新版接口
### 筛选接口
https://xueqiu.com/service/screener/screen?category=CN&exchange=sh_sz&order_by=pb&order=asc&page=1&size=100&only_count=0&pettm=5_10&pb=0_1&_=1583909007398
该接口有一定的弹性，只有你需要查询的字段会在接口中添加上。所以内容比较精简。
#### 返回数据格式
{
    "data":{
        "count":802,
        "list":[
            {
                "pct":-0.38,
                "symbol":"SZ201872",
                "pettm":5.083,
                "current":7.87,
                "pb":0.385,
                "name":"招港B",
                "exchange":"sh_sz",
                "type":11,
                "tick_size":0.01,
                "has_follow":false
            }
        ]
    },
    "error_code":0,
    "error_description":""
}
#### 关心的数据格式
{
    "data":{      
        "count":1,                     // 总记录条数（符合条件的，不等同于返回的条数size）
        "list":[
            {
                "symbol":"SZ201872",   // 证券号码
                "pettm":5.083,         // TTM
                "current":7.87,        // 当前价格
                "pb":0.385,            // PB
                "name":"招港B",         // 证券名称
            }
        ]
    }
}

