# PythonChallenge
Personal solutions for pythonchallenge.com

# Level 0: 0.html
http://www.pythonchallenge.com/pc/def/0.html

The title is "warming up".
The hint is "try to change the URL address".
From the source code of the web page, we can see that the name of the picture is "calc.jpg".The content of the picture is 2^38.
Based on the above information, it can be concluded that let us calculate 2 to the 38th power.

```python
# print(2**38)
print(pow(2, 38))
```

You will get 274877906944.

The address of the next level is at http://www.pythonchallenge.com/pc/def/274877906944.html

# Level 1: map.html
http://www.pythonchallenge.com/pc/def/map.html

The title of the page is "What about making trans?" Tells us that we are doing some kind of conversion. As you can see from the picture, K to M, O to Q, E to G is like an encryption method. The passage below the picture looks like cipher text. In alphabetical order KLM, OPQ, EFG, you can find that the rule is to shift each letter two places in the alphabetical order table.

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