def gentable(start, end):
    str_tmp = ''
    for i in range(start, end +1):
        str_tmp += chr(i)
        
    return str_tmp
intable1 = gentable(97, 122)
outable1 = gentable(99, 122) + 'ab'
print(intable1)
print(outable1)
intable2 = gentable(65, 90)
outable2 = gentable(67, 90) + 'AB'
print(intable2)
print(outable2)
trantab = str.maketrans(intable1, outable1)
print(str0.translate(trantab))
str1 = "map"
print(str1.translate(trantab))
str7 = "iqeylatu"
print(str7.translate(trantab))
