import re
with open('str_re.txt', 'r') as f:
    str_re = f.read()
# print(str3)
rx = re.compile(r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
result = rx.findall(str_re)
print(result)
str8 = ''
for i in result:
    tmp = i[4]
#     print(tmp)
    str8 += tmp
print(str8)    