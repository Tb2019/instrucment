import requests
from fake_useragent import UserAgent
from instrument.get_proxy import ProxyPool

pool = ProxyPool()
url = "https://www.instrument.com.cn/netshow/combo/paper/getAttachmentUrl"

payload = {'paperId': '994448',
'pType': '1',
'device': 'PC'}
files=[

]
headers = {
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'sajssdk_2015_cross_new_user=1; 3i=2024120610080925; isnotice=2; isfirstin=false; mobileValid=85de113a163b97513476bd80075ed6e2; imtoken=957c715e107be62039d81a6caa09af1a; CheckValid=25277ff477881fe3d333edfb77b70dbb; imstep=1733450951; passwordValid=b7be5bfb0e9daf2c24663eddcdd96b59; useid=6825953; mobile=b47ebe9bea209181829fecc5b23a29ff; nickname=Ins%255f98d68598; username_guestbook=6825953; userType=0; privacyVersion=62; username=Ins_98d68598; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22Ins_98d68598%22%2C%22first_id%22%3A%2219399b9799116e5-0eaebd7d39cd4a8-4c657b58-1821369-19399b9799214c4%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzOTliOTc5OTExNmU1LTBlYWViZDdkMzljZDRhOC00YzY1N2I1OC0xODIxMzY5LTE5Mzk5Yjk3OTkyMTRjNCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ikluc185OGQ2ODU5OCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22Ins_98d68598%22%7D%2C%22%24device_id%22%3A%2219399b9799116e5-0eaebd7d39cd4a8-4c657b58-1821369-19399b9799214c4%22%7D; sensorsKey=Ins_98d68598; HMF_CI=;',
  'DNT': '1',
  'Origin': 'https://www.instrument.com.cn',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': UserAgent().random,
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, proxies=pool.load_proxy(from_clash=True))

print(response.text)
