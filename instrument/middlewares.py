# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import asyncio
import scrapy
from twisted.internet import defer
from twisted.internet.threads import deferToThread
from scrapy import signals
import requests
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
from instrument.Pdf_url_request import PdfUrlRequest, PdfDownloadRequest
from instrument.get_proxy import ProxyPool

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# proxy = {
#     'http': '127.0.0.1:7899',
#     'https': '127.0.0.1:7899',
# }

class InstrumentSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class InstrumentDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class request_middleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        self.session = requests.Session()  # 创建一个请求会话
        # 获取pdf链接用到以下配置
        self.url = "https://www.instrument.com.cn/netshow/combo/paper/getAttachmentUrl"
        self.pdf_download_headers = {
                                      'Accept': '*/*',
                                      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                      'Cache-Control': 'no-cache',
                                      'Connection': 'keep-alive',
                                      'DNT': '1',
                                      'Pragma': 'no-cache',
                                      'Sec-Fetch-Dest': 'document',
                                      'Sec-Fetch-Mode': 'navigate',
                                      'Sec-Fetch-Site': 'none',
                                      'Sec-Fetch-User': '?1',
                                      'Upgrade-Insecure-Requests': '1',
                                      'User-Agent': UserAgent().random,
                                      'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                                      'sec-ch-ua-mobile': '?0',
                                      'sec-ch-ua-platform': '"Windows"'
                                    }

        self.pdf_headers = {
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
        self.headers = {'User-Agent': UserAgent().random}
        self.pool = ProxyPool()
        # self.proxy = self.pool.load_proxy(from_clash=False)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        处理每个请求，将其传递给 `requests.Session` 进行同步处理
        """

        # 使用 requests 会话发送请求
        def send_request():
            self.proxy_key, self.proxy = self.pool.load_proxy(from_clash=False)
            self.pdf_headers['User-Agent'] = UserAgent().random
            self.pdf_download_headers['User-Agent'] = UserAgent().random
            self.headers['User-Agent'] = UserAgent().random
            self.session = requests.Session()
            try:
                if isinstance(request, PdfUrlRequest):
                    payload = {'paperId': f'{request.meta["pdf_serial"]}',
                               'pType': '1',
                               'device': 'PC'}
                    files = [

                    ]
                    response = requests.request("POST", self.url, headers=self.pdf_headers, data=payload, files=files, proxies=self.proxy)
                elif isinstance(request, PdfDownloadRequest):
                    response = self.session.get(request.url, headers=self.pdf_download_headers, proxies=self.proxy)
                else:
                    # 发送同步请求
                    response = self.session.get(request.url, headers=self.headers, proxies=self.proxy)
            except:
                self.proxy_key, self.proxy = self.pool.load_proxy(from_clash=False)
                self.pdf_headers['User-Agent'] = UserAgent().random
                self.headers['User-Agent'] = UserAgent().random
                self.session = requests.Session()
                request_retry = request.replace(dont_filter=True)
                return request_retry
            # 创建 Scrapy 的 HtmlResponse 对象
            # 如果请求失败，重新生成请求
            if '访问行为存在异常' in response.text:
                self.pool.delete_proxy(self.proxy_key)
                request_retry = request.replace(dont_filter=True)
                return request_retry
            if ('seccaptcha.haplat.net/css/captcha.css' or '访问行为存在异常') in response.text:
                # print(response.request.url)
                # print(response.request.body)
                # print(response.text)
                # print("重试")
                # request_retry = request.replace(dont_filter=True, headers=self.headers, meta=meta_)
                request_retry = request.replace(dont_filter=True)
                return request_retry
            return HtmlResponse(url=request.url, body=response.content, encoding='utf-8', request=request)

        # 返回一个Deferred对象，异步执行 send_request
        return deferToThread(send_request)


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
