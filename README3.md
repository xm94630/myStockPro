# python 知识

## python 字典
相当于js中的对象字面量
data = {
    'id' : 1,
    'name' : 'xm'
}
print ("输出：", repr(data))
### 读取
使用 data['id']
不能用 data.id

## JSON
json_str = json.dumps(data)
print ("输出：", json_str)

## list
相当于js的数组

## repr() 
函数将对象转化为供解释器读取的形式。
