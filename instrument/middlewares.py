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
from instrument.Pdf_url_request import PdfUrlRequest

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


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
        self.headers = {
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
            if isinstance(request, PdfUrlRequest):
                payload = 'paperId={}&pType=1&device=PC'.format(request.meta['pdf_serial'])
                response = requests.request("POST", self.url, headers=self.headers, data=payload)
            else:
                # 发送同步请求
                response = self.session.get(request.url, headers={'User-Agent': UserAgent().random})
            # 创建 Scrapy 的 HtmlResponse 对象
            # todo：如果请求失败，重新生成请求
            if 'seccaptcha.haplat.net/css/captcha.css' in response.text:
                print("重试")
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
