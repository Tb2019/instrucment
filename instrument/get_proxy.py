# -*- coding: utf-8 -*-
import time
import requests
import redis
import json

api_url = "https://api.xiaoxiangdaili.com/ip/get"


class ProxyPool:
    def __init__(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, password='123456', db=2, decode_responses=True)

    def get_proxy(self, app_key='1182498304798642176', app_secret='zy7lMpl0'):
        while True:
            # 每10s才能获取一次
            resp = requests.get(api_url, params={'appKey': app_key, 'appSecret': app_secret, 'wt': 'text', 'cnt': 1})  # 提取ip数：1
            resp.encoding = 'utf-8'
            text = resp.text
            if '请求过于频繁' in str(text):
                time.sleep(1)
                return self.get_proxy(app_key, app_secret)
            else:
                proxy_meta = f"http://{app_key}:{app_secret}@{text}"
                proxies = {
                    "http": proxy_meta,
                    "https": proxy_meta,
                }
                # print('代理获取成功')
                self.db.set(str(int(time.time())), json.dumps(proxies), ex=60)
                time.sleep(14)
                # return proxies

    def load_proxy(self, from_clash=False):
        if from_clash:
            return {
                "http": "http://127.0.0.1:7899",
                "https": "http://127.0.0.1:7899"
            }

        key = self.db.randomkey()
        if key:
            return json.loads(self.db.get(key))
        else:
            time.sleep(5)
            return self.load_proxy()

    def get_all(self):
        return self.db.keys()


if __name__ == '__main__':
    pool = ProxyPool()
    pool.get_proxy()
    # proxy = pool.load_proxy()
    # print(proxy)
