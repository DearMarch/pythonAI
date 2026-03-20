import json

d = {
    "name": "haha",
    "age": 18,
    "gender" : "男",
}
print(str(d))

s = json.dumps(d, ensure_ascii=False)
print(s)

res_str = '{"name": "haha", "age": 18}'
res_dict = json.loads(res_str)
print(res_dict)