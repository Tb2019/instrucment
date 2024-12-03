# -*- coding: utf-8 -*-
import requests

url = "https://www.instrument.com.cn/netshow/combo/paper/getAttachmentUrl"

payload = "paperId=1014897&pType=1&device=PC"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'mobileValid=85de113a163b97513476bd80075ed6e2; imtoken=07b7c6774861c7907d078cef54eeb88c; CheckValid=25277ff477881fe3d333edfb77b70dbb; imstep=1733191848; passwordValid=b7be5bfb0e9daf2c24663eddcdd96b59; useid=6825953; mobile=b47ebe9bea209181829fecc5b23a29ff; nickname=Ins%255f98d68598; username_guestbook=6825953; userType=0; privacyVersion=62; username=Ins_98d68598; ; HMF_CI=cc1a1861b124063fca0360db7e848979eaea11c11c84c575f36e003b25acad310a800fe79db6c55ffcc7a734f262fe4aa8c8e1957d4ebaa31acb6fd9a4270f04dc',
  'DNT': '1',
  'Origin': 'https://www.instrument.com.cn',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
print(response)

# with open('test.pdf', 'wb') as f:
#     f.write(requests.get(response['data']).content)


