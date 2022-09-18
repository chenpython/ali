#!user/bin/python2.7
# coding:utf-8
import requests
import json
import ctypes
from ctypes import *
from parse import search


headers = {
    "authority": "gateway.jiangongdata.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "origin": "https://www.jiangongdata.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.jiangongdata.com/",
    "accept-language": "zh-CN,zh;q=0.9"
}

dll = windll.LoadLibrary('aliyun')
url = ctypes.c_char_p("http://njia.co/")
id = ctypes.c_char_p("FFFF0N0000000000A971")
response = ctypes.c_char_p(dll.aliyun(url, id))


token = search(";|{token}')", str(response))["token"]
token = token.split(":")[0] + ": register:"+token.split(":")[1] + ":" + token.split(":")[2]
print token
sign = search('"value":"{sign}"}', str(response))["sign"]
sessionId = search('csessionid":"{sessionId}",', str(response))["sessionId"]
url = "http://gateway.jiangongdata.com/jian-butler-member-biz/login/loginByUsername"
data = {
    "mobile": "18580848142",
    "password": "18580848142",
    "loginName": "18580848142",
    "params": {
        "sig": sign,
        "sessionId": sessionId,
        "token": token,
        "sign":sign
    }
}
data = json.dumps(data)
print data
response = requests.post(url, headers=headers,  data=data)

print(response.text)
print(response)
