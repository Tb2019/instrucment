# Scrapy settings for instrument project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 启动参数
# BI_CATEGORY_1 = '化学分析仪器'
# BI_CATEGORY_1 = '光学仪器及设备'
# BI_CATEGORY_1 = '物性测试仪器及设备'
# BI_CATEGORY_1 = '实验室常用设备'
# BI_CATEGORY_1 = '生命科学仪器及设备'
# BI_CATEGORY_1 = '环境监测仪器'
# BI_CATEGORY_1 = '行业专用仪器'
# BI_CATEGORY_1 = '测量仪器'
# BI_CATEGORY_1 = '半导体行业专用仪器设备'
# BI_CATEGORY_1 = '工业在线及过程控制仪器'
# BI_CATEGORY_1 = '实验室服务'
# BI_CATEGORY_1 = '二手仪器'
# BI_CATEGORY_1 = '电子测量仪器'
# BI_CATEGORY_1 = '医学仪器'
BI_CATEGORY_1 = '相关仪表'

# BI_CATEGORY_2 = '色谱仪器'
# BI_CATEGORY_2 = '光谱仪器'
# BI_CATEGORY_2 = '质谱仪器'
# BI_CATEGORY_2 = 'X射线仪器'
# BI_CATEGORY_2 = '电化学仪器'
# BI_CATEGORY_2 = '元素分析仪'
# BI_CATEGORY_2 = '波谱仪器'
# BI_CATEGORY_2 = '水分测定仪'
# BI_CATEGORY_2 = '其它通用分析仪器'
# BI_CATEGORY_2 = '色谱配套设备'
# BI_CATEGORY_2 = '光谱配套设备'
# BI_CATEGORY_2 = '质谱配套设备'
# BI_CATEGORY_2 = '能谱仪器'
# BI_CATEGORY_2 = '电子显微镜'
# BI_CATEGORY_2 = '光学显微镜'
# BI_CATEGORY_2 = '光学测量仪'
# BI_CATEGORY_2 = '光学实验设备'
# BI_CATEGORY_2 = '光学成像设备'
# BI_CATEGORY_2 = '粒度/颗粒/粉末分析仪器'
# BI_CATEGORY_2 = '热分析仪器'
# BI_CATEGORY_2 = '流变仪/粘度计'
# BI_CATEGORY_2 = '试验机'
# BI_CATEGORY_2 = '表界面物性测试'
# BI_CATEGORY_2 = '环境试验箱'
# BI_CATEGORY_2 = '无损检测仪器/设备'
# BI_CATEGORY_2 = '测厚仪'
# BI_CATEGORY_2 = '燃烧测定仪'
# BI_CATEGORY_2 = '磁学测量仪器'
# BI_CATEGORY_2 = '其它物性测试仪器'
# BI_CATEGORY_2 = '清洗/消毒设备'
# BI_CATEGORY_2 = '制样/消解设备'
# BI_CATEGORY_2 = '3D打印机'
# BI_CATEGORY_2 = '分离/萃取设备'
# BI_CATEGORY_2 = '纯化设备'
# BI_CATEGORY_2 = '混合/分散设备'
# BI_CATEGORY_2 = '恒温/加热/干燥设备'
# BI_CATEGORY_2 = '粉碎设备'
# BI_CATEGORY_2 = '合成/反应设备'
# BI_CATEGORY_2 = '制冷设备'
# BI_CATEGORY_2 = '泵'
# BI_CATEGORY_2 = '液体处理设备'
# BI_CATEGORY_2 = '气体发生器/气体处理'
# BI_CATEGORY_2 = '实验室家具'
# BI_CATEGORY_2 = '其它实验室常用设备'
# BI_CATEGORY_2 = 'PCR/测序/核酸分析'
# BI_CATEGORY_2 = '酶标仪/微孔板仪器'
# BI_CATEGORY_2 = '蛋白分析'
# BI_CATEGORY_2 = '细胞分析'
# BI_CATEGORY_2 = '电泳/凝胶成像/紫外检测'
# BI_CATEGORY_2 = '生物显微镜/活体成像'
# BI_CATEGORY_2 = '病理实验仪器'
# BI_CATEGORY_2 = '微生物检测仪器'
# BI_CATEGORY_2 = '芯片系统/配套'
# BI_CATEGORY_2 = '生物工程设备'
# BI_CATEGORY_2 = '培养箱设备'
# BI_CATEGORY_2 = '实验室低温存储'
# BI_CATEGORY_2 = '实验室自动化'
# BI_CATEGORY_2 = '转染/细胞融合'
# BI_CATEGORY_2 = '合成仪'
# BI_CATEGORY_2 = '植物生理生态仪器'
# BI_CATEGORY_2 = '动物实验仪器'
# BI_CATEGORY_2 = '电生理仪'
# BI_CATEGORY_2 = '水质分析'
# BI_CATEGORY_2 = '气体检测仪'
# BI_CATEGORY_2 = '应急/便携/车载'
# BI_CATEGORY_2 = '辐射测量仪器'
# BI_CATEGORY_2 = '海洋监测仪器'
# BI_CATEGORY_2 = '其它环境监测仪器'
# BI_CATEGORY_2 = '药物检测专用仪器'
# BI_CATEGORY_2 = '石油专用分析仪器'
# BI_CATEGORY_2 = '农业和食品专用仪器'
# BI_CATEGORY_2 = '纺织行业专用仪器'
# BI_CATEGORY_2 = '煤炭行业专用仪器'
# BI_CATEGORY_2 = '橡塑行业专用仪器'
# BI_CATEGORY_2 = '包装行业专用仪器'
# BI_CATEGORY_2 = '锂电行业专用仪器'
# BI_CATEGORY_2 = '金属与冶金行业专用仪器'
# BI_CATEGORY_2 = '危险化学品检测专用仪器'
# BI_CATEGORY_2 = '建筑工程专用仪器'
# BI_CATEGORY_2 = '其它行业专用仪器/仪表'
# BI_CATEGORY_2 = '教学专用仪器'
# BI_CATEGORY_2 = '氢能行业专用仪器'
# BI_CATEGORY_2 = '天平/衡器'
# BI_CATEGORY_2 = '温湿度检测仪器'
# BI_CATEGORY_2 = '几何量精密测量仪器'
# BI_CATEGORY_2 = '压力检测仪器'
# BI_CATEGORY_2 = '流量计'
# BI_CATEGORY_2 = '其它测量仪器'
# BI_CATEGORY_2 = '薄膜生长设备'
# BI_CATEGORY_2 = '工艺测量和检测设备'
# BI_CATEGORY_2 = '集成电路测试与分选设备'
# BI_CATEGORY_2 = '光刻及涂胶显影设备'
# BI_CATEGORY_2 = '热工艺设备/热处理设备'
# BI_CATEGORY_2 = '硅片制备/晶体生长设备'
# BI_CATEGORY_2 = '掩模版和中间掩模版制造设备'
# BI_CATEGORY_2 = '离子注入设备'
# BI_CATEGORY_2 = '干法工艺设备'
# BI_CATEGORY_2 = '湿法工艺设备'
# BI_CATEGORY_2 = '组装与封装设备'
# BI_CATEGORY_2 = '其他半导体行业仪器设备'
# BI_CATEGORY_2 = '在线电导率仪'
# BI_CATEGORY_2 = '在线氧分析仪'
# BI_CATEGORY_2 = '在线pH计'
# BI_CATEGORY_2 = '在线流量计'
# BI_CATEGORY_2 = '流量计流速仪/测漏仪'
# BI_CATEGORY_2 = '工业色谱仪'
# BI_CATEGORY_2 = '工业用粘度计'
# BI_CATEGORY_2 = '工业用颗粒度仪'
# BI_CATEGORY_2 = '在线反应分析系统'
# BI_CATEGORY_2 = '其它工业过程控制及在线分析仪'
# BI_CATEGORY_2 = '仪器租赁'
# BI_CATEGORY_2 = '维修保养'
# BI_CATEGORY_2 = '产品培训'
# BI_CATEGORY_2 = '认证校准'
# BI_CATEGORY_2 = '数据处理'
# BI_CATEGORY_2 = 'LIMS/软件'
# BI_CATEGORY_2 = '实验室搬迁'
# BI_CATEGORY_2 = '实验室规划与设计'
# BI_CATEGORY_2 = '可靠性测试'
# BI_CATEGORY_2 = '其它服务'
# BI_CATEGORY_2 = '二手分析仪器'
# BI_CATEGORY_2 = '二手光学仪器'
# BI_CATEGORY_2 = '其他二手仪器'
# BI_CATEGORY_2 = '通用电子测量仪器'
# BI_CATEGORY_2 = '辅助仪器'
# BI_CATEGORY_2 = '射频和微波测试仪器'
# BI_CATEGORY_2 = '电子元器件测试仪器'
# BI_CATEGORY_2 = '网络分析仪器'
# BI_CATEGORY_2 = '通讯测试仪器'
# BI_CATEGORY_2 = '医学影像'
# BI_CATEGORY_2 = '临床检验仪器设备'
# BI_CATEGORY_2 = '基础仪表'
# BI_CATEGORY_2 = '工业仪表'
BI_CATEGORY_2 = '其它相关仪表'

# START_URLS = ['https://www.instrument.com.cn/show/sort-1/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-2/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-4/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-7/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-11/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-19/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-3/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-39/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-46/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-251/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-252/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-253/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-255/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-103/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-5/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-29/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-118/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-125/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-38/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-6/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-9/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-31/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-40/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-45/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-18/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-100/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-37/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-156/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-47/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-90/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-34/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-243/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-50/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-51/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-54/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-13/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-53/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-49/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-48/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-55/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-120/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-111/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-14/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-52/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-12/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-259/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-261/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-126/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-257/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-130/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-276/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-128/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-129/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-56/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-254/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-262/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-260/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-258/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-256/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-108/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-58/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-275/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-26/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-25/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-27/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-28/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-250/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-59/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-42/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-30/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-33/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-35/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-36/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-10/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-43/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-152/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-223/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-132/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-131/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-22/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-277/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-288/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-60/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-62/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-61/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-147/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-148/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-44/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-263/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-264/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-265/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-266/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-267/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-268/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-269/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-270/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-271/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-272/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-273/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-274/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-93/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-98/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-109/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-97/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-86/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-63/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-64/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-65/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-92/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-17/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-139/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-135/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-136/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-138/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-140/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-16/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-142/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-143/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-151/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-144/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-133/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-289/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-290/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-225/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-235/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-227/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-233/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-231/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-229/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-247/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-57/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-21/']
# START_URLS = ['https://www.instrument.com.cn/show/sort-67/']
START_URLS = ['https://www.instrument.com.cn/show/sort-66/']

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

FILES_STORE = r'C:\Users\98214\Desktop\pdfs'

SPIDER_MODULES = ["instrument.spiders"]
NEWSPIDER_MODULE = "instrument.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "instrument (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = "INFO"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_TIMEOUT = 30
# CONCURRENT_REQUESTS = 10
DOWNLOAD_DELAY = 2
# CONCURRENT_REQUESTS_PER_DOMAIN = 10
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
