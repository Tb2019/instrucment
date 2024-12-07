import scrapy
from instrument.items import ApplicationFieldItem
from scrapy.utils.project import get_project_settings

instru_info_divs_xpath = '//div[@class="tertiaryClasstC-left-list"]/div[contains(@class, "tertiaryClasstC-left-list-item")]'

class GetApplicationFieldSpider(scrapy.Spider):
    name = "get_application_field"
    custom_settings = {
        'ITEM_PIPELINES': {
            'instrument.pipelines.ApplicationFieldPipeline': 300,
        }
    }
    allowed_domains = ["www.instrument.com.cn"]
    start_urls = get_project_settings()['START_URLS']
    # start_urls = ["https://www.instrument.com.cn/show/sort-1"]

    bi_category_1 = get_project_settings()['BI_CATEGORY_1']
    bi_category_2 = get_project_settings()['BI_CATEGORY_2']
    # bi_category_1 = '化学分析仪器'
    # bi_category_2 = '色谱仪器'

    def parse(self, response):
        '''
        解析二级分类页面，获取各个三级分类链接
        :param response:
        :return:
        '''

        category_3_info_eles = response.xpath('//div[@class="pc-towType-yxt bgf pt16 pl16 mb16"]/div/a')
        for ele in category_3_info_eles:
            bi_category_3 = ele.xpath('.//p[contains(@class, "tit omit")]/text()').extract_first()
            link = response.urljoin(ele.xpath('./@href').extract_first())
            # item_ = item.copy()  # 深拷贝。否则传递的是引用，会导致后续的item被修改，值是相同的
            yield scrapy.Request(url=link, callback=self.get_field_link, meta={'bi_category_3': bi_category_3})
            # break

    def get_field_link(self, response):
        application_file_info_lis = response.xpath('//ul[@data-title="应用领域"]/li')
        for li in application_file_info_lis:
            data_val = '?sampleIds=' + li.xpath('./@data-val').extract_first()
            field_name = li.xpath('./text()').extract_first()
            yield scrapy.Request(url=response.urljoin(data_val), callback=self.get_field_item,
                                 meta={'field_name': field_name,
                                       'bi_category_3': response.meta['bi_category_3'],
                                       'page': 1})
            # break

    def get_field_item(self, response):
        total_num = response.xpath('//div[@class="tertiaryClasstC-left-tab-sort-total"]//em/text()').extract_first()
        total_pages = int(total_num) // 30 + 1

        item = ApplicationFieldItem()
        instru_info_divs = response.xpath(instru_info_divs_xpath)
        for div in instru_info_divs:
            instru_name = div.xpath('.//h3/a/text()').extract_first()
            item['bi_category_2'] = self.bi_category_2
            item['bi_category_3'] = response.meta['bi_category_3']
            item['instru_name'] = instru_name
            item['field'] = response.meta['field_name']
            yield item

        if response.meta['page'] == 1:
            for page in range(2, total_pages+1):
                yield scrapy.Request(url=response.url + '&page=' + str(page), callback=self.get_field_item,
                                     meta={'field_name': response.meta['field_name'],
                                           'bi_category_3': response.meta['bi_category_3'],
                                           'page': page})
