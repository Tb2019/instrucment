# -*- coding: utf-8 -*-
import time
import tls_client
import requests
from fake_useragent import UserAgent
import pyhttpx
from instrument.get_proxy import ProxyPool


# session = tls_client.Session(
#     ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0",
#     h2_settings={
#         "HEADER_TABLE_SIZE": 65536,
#         "MAX_CONCURRENT_STREAMS": 1000,
#         "INITIAL_WINDOW_SIZE": 6291456,
#         "MAX_HEADER_LIST_SIZE": 262144
#     },
#     h2_settings_order=[
#         "HEADER_TABLE_SIZE",
#         "MAX_CONCURRENT_STREAMS",
#         "INITIAL_WINDOW_SIZE",
#         "MAX_HEADER_LIST_SIZE"
#     ],
#     supported_signature_algorithms=[
#         "ECDSAWithP256AndSHA256",
#         "PSSWithSHA256",
#         "PKCS1WithSHA256",
#         "ECDSAWithP384AndSHA384",
#         "PSSWithSHA384",
#         "PKCS1WithSHA384",
#         "PSSWithSHA512",
#         "PKCS1WithSHA512",
#     ],
#     supported_versions=["GREASE", "1.3", "1.2"],
#     key_share_curves=["GREASE", "X25519"],
#     cert_compression_algo="brotli",
#     pseudo_header_order=[
#         ":method",
#         ":authority",
#         ":scheme",
#         ":path"
#     ],
#     connection_flow=15663105
# )

sess = pyhttpx.HttpSession()
session = requests.session()
# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#   'Cache-Control': 'no-cache',
#   'Connection': 'keep-alive',
#   'DNT': '1',
#   'Pragma': 'no-cache',
#   'Sec-Fetch-Dest': 'document',
#   'Sec-Fetch-Mode': 'navigate',
#   'Sec-Fetch-Site': 'same-origin',
#   'Sec-Fetch-User': '?1',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
#   'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"'
# }

urls = [
# 'https://www.instrument.com.cn',
# 'https://www.instrument.com.cn/application/Solution-940521.html',
'https://www.instrument.com.cn/application/Solution-236403.html',
# 'https://www.instrument.com.cn/application/Solution-519664.html',
# 'https://www.instrument.com.cn/application/Solution-335415.html',
# 'https://www.instrument.com.cn/application/Solution-913422.html',
# 'https://www.instrument.com.cn/show/category-323/',
# 'https://www.instrument.com.cn/show/category-26/',
# 'https://www.instrument.com.cn/show/category-635/',
# 'https://www.instrument.com.cn/show/category-1747/',
# 'https://www.instrument.com.cn/show/category-632/',
]
pool = ProxyPool()
proxy = pool.load_proxy(from_clash=True)
count = 0
for url in urls:
    resp = session.get(url, headers={'User-Agent': UserAgent().random}, proxies=proxy, timeout=10)
    if 'seccaptcha.haplat.net/css/captcha.css' not in resp.text and '访问行为存在异常' not in resp.text and resp.status_code == 200:
        # count += 1
        print(url, '成功')
        # if count % 10 == 0:
        print(resp.text)
    else:
        print('***失败')
        print(resp.status_code)
        print(resp)
        print(resp.text)
