import json

data = [{"a": "aaa", "b": "bbb", "c": [1, 2, 3, (4, 5, 6)]}, 33, 'tantengvip', True]
data2 = json.dumps(data)


data3 = json.loads('{"lat":444, "lon":555}')
for key, value in data3.items():
    print (key)
    print (value)
# for j in data3:
#     print(j)
#     print(data3[j])
