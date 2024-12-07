# Scrapy settings for instrument project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 启动参数
BI_CATEGORY_1 = '化学分析仪器'
BI_CATEGORY_2 = '色谱仪器'
START_URLS = ['https://www.instrument.com.cn/show/sort-1/']

# 连接数据库
MYSQL_HOST = '192.168.2.12'
MYSQL_PORT = 3306
MYSQL_DB = 'alpha_search_update'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Shufang_@919'
MYSQL_TABLE = 'search_instrument_selection'
TABLE_FIELDS = ['bi_category_1',
                'bi_category_2',
                'bi_category_3',
                'instru_link',
                'bi_brand',
                'bi_origin_category',
                'bi_origin',
                'bi_manufacturer_type',
                'bi_instrument_name',
                'bi_model_number',
                'bi_manufacturer_name',
                'bi_manufacturer_logo',
                'bi_business_license_status',
                'bi_rating',
                'bi_reference_price',
                'bi_sample_src',
                'bi_instrument_image',
                'core_parameters',
                'product_description',
                'after_sale_service',
                # 'sub_links_num',
                # 'finish_link_count',
                # 'user_evaluation_finished',
                'relevant_solutions',
                'relevant_article',
                'user_evaluation',
                # 'evaluation_finished',
                'bi_application_field']

BOT_NAME = "instrument"

FILES_STORE = './instrument/pdfs'

SPIDER_MODULES = ["instrument.spiders"]
NEWSPIDER_MODULE = "instrument.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "instrument (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = "WARNING"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "instrument.middlewares.InstrumentSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # "instrument.middlewares.InstrumentDownloaderMiddleware": 543,
    "instrument.middlewares.request_middleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "instrument.pipelines.InstrumentPipeline": 300,
   "instrument.pipelines.InstruPdfDownloadPipeline": 301,
   "instrument.pipelines.Save2MysqlPipeline": 302
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
