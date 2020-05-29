# PythonChallenge
Personal solutions for http://www.pythonchallenge.com.

Some ideas are found through search engines, and some are my own ideas. The code is mostly written by myself, it is a bit messy, if you find any problems, please point it out, thank you!

# Level 0: 0.html
http://www.pythonchallenge.com/pc/def/0.html

The title of the page is "warming up". 
The hint is "try to change the URL address". 
From the source code of the web page, we can see that the name of the picture is "calc.jpg".
The content of the picture is 2^38.
Based on the above information, we can know to calculate 2 to the 38th power.

```python
# print(2**38)
print(pow(2, 38))
```

We will get 274877906944.

The address of the next level is at http://www.pythonchallenge.com/pc/def/274877906944.html

# Level 1: map.html
http://www.pythonchallenge.com/pc/def/map.html

The title of the page is "What about making trans?". Tells us that we are doing some kind of conversion. As we can see from the picture, K to M, O to Q, E to G is like an encryption method. The passage below the picture looks like cipher text. In alphabetical order KLM, OPQ, EFG, we can find that the rule is to shift each letter two places in the alphabetical order table.

```python
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

```
Decrypt the ciphertext to get the following paragraph "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.". It told us to use string.maketrans() and apply on the url.

We can get "ocr" by converting the "map" in the URL.
```python
print(''.join(Caesar('map')))
```
The address of the next level is at http://www.pythonchallenge.com/pc/def/ocr.html

# Level 2: ocr.html
http://www.pythonchallenge.com/pc/def/ocr.html

The title of the page is "ocr", which may allow us to recognize the text in the picture. However, the hint below the picture tells us that they should be located in the webpage source file.

We found such a sentence in the comments of the webpage source file: "find rare characters in the mess below", and found a large section of irregular character strings in the following comments.

Therefore, We need find the rare characters in the second comments.

```python
# 1. Find the number of appearance for each character. 
# 2. You'll find only "t q e u a y i l" appeared once.
with open('ocr.txt', 'r') as f:
    str3 = f.read()
# print(str3)
str4 = list(set(str3))
print(str4)
str5 = ''.join(str4)
print(str5)
str_counts = []
for i in str5:
    str_counts.append(str3.count(i))
print(str_counts)
for key, value in zip(str5, str_counts):
    print(key, value, end = '|')
print('\n')
# 3. Sort these letters according to their position 
# in the string to get the word "equality".
str6 = ''
for i in str5:
    num = str3.count(i)
    if num == 1:
        str6 += i
print(str6)
dict0 = {}
for i in str6 :
    print(i, str3.find(i))
    dict0[i] = str3.find(i)
dict1 = sorted(dict0.items(), key=lambda dict0:dict0[1], reverse = 0)
print(dict1)
```
The address of the next level is at http://www.pythonchallenge.com/pc/def/equality.html

# Level 3: equality.html
http://www.pythonchallenge.com/pc/def/equality.html

The title of the page is "re", which tells us to use regular expressions. The pictures and pictures below tell us a rule: AAAaAAA, of course, A can be replaced with any letter. For this rule to be true, we can know that the beginning and end of the string must also be lowercase letters.

In the webpage source file, we found a very long comment, some of the strings in line with the above rules.

```python
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
```

We will get linkedlist.
When we visit http://www.pythonchallenge.com/pc/def/linkedlist.html, the webpage prompts that we should visit http://www.pythonchallenge.com/pc/def/linkedlist.php

# Level 4: linkedlist.php
http://www.pythonchallenge.com/pc/def/linkedlist.php

The title of the page is "follow the chain". When we observe the source files of the webpage, we can find that the comment tells us to use "urllib" and it takes more than four hundred attempts. There is a link "linkedlist.php? Nothing = 12345" on the picture. After clicking, "and the next nothing is 44827" appears. It tells us that the value of the next thing is "44827", replace "12345" in the link with "44827" to get the value of the next thing, and repeat to get the result.

We use the requests module to replace the urllib module.

At the 85th time, the prompt was "Yes. Divide by two and keep going." There are two methods here. The first is to divide the result 16044 of the 84th by 2 according to the prompt, and get 8022 to use it as the value of nothing to continue the loop. The second is to continue to loop with "going." as the value of nothing. Both methods will have the same result, the only difference is the number of times. In here we use the second methods.
```python
import requests
import re
import time

def geturl(url, payload):
    ry = requests.Session()
    
    headers = {'Accept' : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding' : "gzip, deflate",
            'Accept-Language' : "zh-CN,zh;q=0.9",
            'Connection' : "keep-alive",
            'Host' : "www.pythonchallenge.com",
            'Referer' : "http://www.pythonchallenge.com/pc/def/linkedlist.php",
            'Upgrade-Insecure-Requests' : "1",
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'"
            }
    
    status = ry.get(url, params=payload, headers=headers).text
    return status
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
payload = {'nothing': '12345'}
i = 0
while payload['nothing'] != 'peak.html' :
    try :
        str0 = geturl(url, payload)
        print(i, payload['nothing'], str0)
        payload['nothing'] = str0.split(' ')[-1]
    except Exception as e:
        print(i, 'NetWork ERR, retry!')
    #         print(repr(e))
    #         time.sleep(1)
    i += 1
```

The address of the next level is at http://www.pythonchallenge.com/pc/def/peak.html

# Level 5: peak.html
http://www.pythonchallenge.com/pc/def/peak.html

The title of the page is "peak hell", and the content of the page is a picture of a mountain and a sentence "pronounce it". In the source code of the webpage, we found a hidden link ```<peakhell src =" banner.p "/>``` and a comment ```<!-Peak hell sounds familiar?->```. Some garbled text appears after the link is opened. The comment tells us to find something pronounce similar to "peak hell". I got stuck here. After searching on the Internet, I learned that PYTHON has a module for serialization and deserialization called pickle and it has a similar pronunciation. This level is let us use the pickle module to deserialize the content of "banner.p".
```python
import requests
import pickle

# text = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").content
# print("1", text)
with open('banner.p', 'rb') as f:
    banner = f.readlines()
# print(type(banner), type(banner[0]))
texts = b''
for i in banner:
    texts += i
#     print(texts)
# print('2', texts)
data = pickle.loads(texts)
print(data)
for i in data :
    print("".join(j[0] * j[1] for j in i))
```
The resualt is "channel".
```python
                                                                                               
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
                                                                                               
```
The address of the next level is at http://www.pythonchallenge.com/pc/def/channel.html
