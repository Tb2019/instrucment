import scrapy
from instrument.items import NewProductItem

xpath_selectors_single_info = {
    ## 基本信息部分
    # 品牌
    'bi_brand': '//div[@class="yqyx-TRANS-product-intro-info-desc flex flex-w"]//label[contains(text(), "品牌")]/following-sibling::p/text()',
    # todo: 应用领域：后续另外爬取数据进行关联处理
    # 产地类别
    'bi_origin_category': '//em[contains(text(), "产地类别")]/following-sibling::i/text()',
    # 产地
    'bi_origin': '//div[@class="yqyx-TRANS-product-intro-info-desc flex flex-w"]//label[contains(text(), "产地")]/following-sibling::p/text()',
    # 厂商性质
    'bi_manufacturer_type': '//ul[@class="yqyx-TRANS-product-intro-info-company-card-desc flex a-c"]/li[last()]/text()',
    # 仪器名称
    'bi_instrument_name': '//div[@class="yqyx-TRANS-product-intro-info-title"]/h1/a/text()',
    # 型号
    'bi_model_number': '//div[@class="yqyx-TRANS-product-intro-info-desc flex flex-w"]//label[contains(text(), "型号")]/following-sibling::p/text()',
    # 厂商名称
    'bi_manufacturer_name': '//div[@class="yqyx-TRANS-product-intro-info-company-card-title flex a-c"]/a/text()',
    # 厂商LOGO
    'bi_manufacturer_logo': '//div[@class="yqyx-TRANS-product-intro-info-company-card flex a-c"]//div[@class="img-box"]//img/@src',
    # 营业执照审核状态
    'bi_business_license_status': '//span[@class="yqyx-TRANS-product-intro-info-company-card-title-tag flex a-c"]/text()',
    # 评分
    'bi_rating': '//span[@class="yqyx-TRANS-product-intro-info-desc-item-top-rate-number"]/text()',
    # 参考报价
    'bi_reference_price': '//span[@class="yqyx-TRANS-product-intro-info-desc-item-top-amt-yuan"]/text()',
    # 样本链接
    'bi_sample_src': '//div[@class="yqyx-TRANS-product-intro-info-desc flex flex-w"]//label[contains(text(), "样本")]/following-sibling::a/@href',
}

xpath_selectors_multi_info = {
    # 仪器图片
    'bi_instrument_image': '//div[@class="swiper-container"]//div[contains(@class, "swiper-slide")]//img/@src'
}


class ChromatographSpider(scrapy.Spider):
    name = "chromatograph"
    allowed_domains = ["www.instrument.com.cn"]
    start_urls = ["https://www.instrument.com.cn/show/sort-1/"]

    def parse(self, response):
        '''
        解析二级分类页面，获取各个三级分类链接
        :param response:
        :return:
        '''
        item = NewProductItem()
        item['bi_category_1'] = '化学分析仪器'
        item['bi_category_2'] = '色谱仪器'

        category_3_info_eles = response.xpath('//div[@class="pc-towType-yxt bgf pt16 pl16 mb16"]/div/a')
        for ele in category_3_info_eles:
            item['bi_category_3'] = ele.xpath('.//p[contains(@class, "tit omit")]/text()').extract_first()
            link = response.urljoin(ele.xpath('./@href').extract_first())
            item_ = item.copy()  # 深拷贝。否则传递的是引用，会导致后续的item被修改，值是相同的
            yield scrapy.Request(url=link, callback=self.parse_detail_category_3_list, meta={'item': item_})
            break

    def parse_detail_category_3_list(self, response):
        '''
        解析三级分类页面，获取具体仪器的链接
        :param response:
        :return:
        '''

        # 提取每页中详情页链接
        page_list_infos = response.xpath('//div[@class="tertiaryClasstC-left-list"]/div[contains(@class, "tertiaryClasstC-left-list-item")]')
        for info in page_list_infos:
            href = response.urljoin(info.xpath('//div[@class="flex a-c"]/a/@href').extract_first())
            # print(href)
            item_ = response.meta['item'].copy()  # 深拷贝。否则传递的是引用，会导致后续的item被修改，值是相同的
            yield scrapy.Request(url=href, callback=self.parse_detail, meta={'item': item_})
            break

        # 翻页
        # 计算页数
        base_url = response.url.split('?page')[0]
        # print('base:', base_url)
        total_num = int(response.xpath('//div[@class="tertiaryClasstC-left-tab-sort-total"]//em/text()').extract_first())
        total_page = total_num // 30 + 1
        for i in range(2, total_page + 1):
            # print(base_url + '?page=' + str(i))
            item_ = response.meta['item'].copy()
            yield scrapy.Request(url=base_url + '?page=' + str(i), callback=self.parse_detail_category_3_list, meta={'item': item_})
            break

    def parse_detail(self, response):
        '''
        解析每个仪器详情页
        :param response:
        :return:
        '''
        item = response.meta['item']
        # 填充单一信息
        for key, xpath in xpath_selectors_single_info.items():
            item[key] = response.xpath(xpath).extract_first() if response.xpath(xpath).extract_first() else None
        # 填充多信息字段
        for key, xpath in xpath_selectors_multi_info.items():
            item[key] = response.xpath(xpath).extract() if response.xpath(xpath).extract() else None
        print(item)
