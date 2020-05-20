#!/usr/bin/env python
# coding: utf-8
# http://www.pythonchallenge.com/pc/def/map.html
def  Caesar(str0):
    str1 = []
    for i in str0:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
            j = ord(i) +2
            if (90 < j < 97) or (122 < j <= 124):
                j = j - 26
            str1.append(chr(j))
        else :
            str1.append(i)
    return str1
str0 = "g fmnc wms bgblr rpylqjyrc "\
"gr zw fylb. rfyrq ufyr amknsrcpq "\
"ypc dmp. bmgle gr gl zw fylb gq "\
"glcddgagclr ylb rfyr'q ufw rfgq "\
"rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() "\
"gq pcamkkclbcb. lmu ynnjw ml rfc spj."
notes = Caesar(str0)
print(str0)
str2 = "".join(notes)
print(str2)

print(''.join(Caesar('map')))

# You will get ocr. The address of the next level is
# http: //www.pythonchallenge.com/pc/def/ocr.html
