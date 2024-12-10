# -*- coding: utf-8 -*-
import time
import requests
import redis
import json






class ProxyPool:
    def __init__(self):
        self.api_url_xx = "https://api.xiaoxiangdaili.com/ip/get"
        self.xx_config = {
            'app_key': '1183579271252561920',
            'app_secret': 'IWherJl8',
        }
        self.api_url_kdl = "https://dps.kdlapi.com/api/getdps/?secret_id=o13mayjko964i93b7flb&signature=fhgfs05ulevygxyq0ufckotwqgf9ebxe&num=35&pt=1&sep=1"
        self.kdl_config = {
            'username': 'd3806958776',
            'password': 'ko5c7bvx',
        }
        self.db = redis.StrictRedis(host='localhost', port=6379, password='123456', db=2, decode_responses=True)
        self.count = 0

    # def get_proxy(self):
    #     '''
    #     小象代理
    #     :param app_key:
    #     :param app_secret:
    #     :return:
    #     '''
    #     while True:
    #         # 每10s才能获取一次
    #         resp = requests.get(api_url_xx, params={'appKey': self.xx_config['app_key'], 'appSecret': self.xx_config['app_secret'], 'wt': 'text', 'cnt': 1})  # 提取ip数：1
    #         resp.encoding = 'utf-8'
    #         text = resp.text
    #         if '请求过于频繁' in str(text):
    #             time.sleep(1)
    #             return self.get_proxy(app_key, app_secret)
    #         else:
    #             proxy_meta = f"http://{app_key}:{app_secret}@{text}"
    #             proxies = {
    #                 "http": proxy_meta,
    #                 "https": proxy_meta,
    #             }
    #             # print('代理获取成功')
    #             self.db.set(str(int(time.time())), json.dumps(proxies), ex=60)
    #             time.sleep(9)
    #             # return proxies

    def get_proxy(self):
        '''
        快代理,集中提取，每次提取35个
        :return:
        '''
        proxy_ips = requests.get(self.api_url_kdl).text.split('\r\n')
        for proxy_ip in proxy_ips:
            proxies = {
                    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": proxy_ip},
                    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": proxy_ip}
                }
            self.count += 1
            self.db.set('ip'+str(self.count), json.dumps(proxies), ex=7200)


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
            # time.sleep(5)
            # return self.load_proxy()
            self.get_proxy()
            return self.load_proxy()

    def get_all(self):
        return self.db.keys()


if __name__ == '__main__':
    pool = ProxyPool()
    pool.get_proxy()
    # proxy = pool.load_proxy()
    # print(proxy)
