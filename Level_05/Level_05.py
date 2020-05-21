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