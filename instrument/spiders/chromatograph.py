import scrapy
from instrument.items import NewProductItem

xpath_selectors = {
    'bi_brand': '//div[@class="yqyx-TRANS-product-intro-info-desc flex flex-w"]//label[contains(text(), "品牌")]/following-sibling::p/text()',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
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
        # 品牌
        item['bi_brand'] = response.xpath(xpath_selectors['bi_brand']).extract_first() if response.xpath(xpath_selectors['bi_brand']).extract_first() else None
        #



