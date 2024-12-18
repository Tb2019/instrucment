# -*- coding: utf-8 -*-
import time
import requests
import redis
import json


class ProxyPool:
    count = 105
    def __init__(self):
        self.api_url_xx = "https://api.xiaoxiangdaili.com/ip/get"
        self.xx_config = {
            'app_key': '1183579271252561920',
            'app_secret': '77cu51xd',
        }
        self.api_url_kdl = "https://dps.kdlapi.com/api/getdps/?secret_id=opzzs67scgogfm6cztnp&signature=ugxfv96ylbleo7e8mc77pa5wqv15tgw7&num=35&pt=1&sep=1"
        self.kdl_config = {
            'username': 't13448766863841',
            'password': '77cu51xd',
        }
        self.db = redis.StrictRedis(host='localhost', port=6379, password='123456', db=2, decode_responses=True)


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

    # def get_proxy(self):
    #     '''
    #     快代理,集中提取，每次提取35个
    #     :return:
    #     '''
    #     proxy_ips = requests.get(self.api_url_kdl).text.split('\r\n')
    #     for proxy_ip in proxy_ips:
    #         proxies = {
    #                 "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": proxy_ip},
    #                 "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": proxy_ip}
    #             }
    #         self.count += 1
    #         self.db.set('ip'+str(self.count), json.dumps(proxies), ex=2*60*60)
    #     proxy_num = self.proxy_count()
    #     if proxy_num < 100:
    #         self.get_proxy()

    def get_proxy(self):
        '''
        快代理,隧道代理
        :return:
        '''
        tunnel = "i230.kdltpspro.com:15818"
        proxies = {
                            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": tunnel},
                            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.kdl_config['username'], "pwd": self.kdl_config['password'], "proxy": tunnel}
                        }
        self.db.set('tunnel', json.dumps(proxies))


    def load_proxy(self, from_clash=False):
        if from_clash:
            return None, {
                "http": "http://127.0.0.1:7899",
                "https": "http://127.0.0.1:7899"
            }

        # proxy_num = self.proxy_count()
        # if proxy_num < 100:
        #     self.get_proxy()

        key = self.db.randomkey()
        if key:
            return key, json.loads(self.db.get(key))
        else:
            # time.sleep(5)
            # return self.load_proxy()
            print('代理池已空，重新获取')
            self.get_proxy()
            return self.load_proxy()

    def delete_proxy(self, key):
        self.db.delete(key)
        print('删除了代理：', key)
        num_proxy = self.proxy_count()
        if num_proxy < 100:
            self.get_proxy()

    def proxy_count(self):
        count = self.db.dbsize()
        return count

    def get_all(self):
        return self.db.keys()


if __name__ == '__main__':
    pool = ProxyPool()
    pool.get_proxy()
    # proxy = pool.load_proxy()
    # print(proxy)
    num = pool.proxy_count()
    print(num)
