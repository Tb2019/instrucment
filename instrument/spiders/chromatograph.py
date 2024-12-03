import json
import re
import scrapy
from instrument.Pdf_url_request import PdfUrlRequest
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

# 核心参数
core_parameters_xpath = '//div[@class="yqyx-TRANS-product-intro-parameters-core flex flex-w"]/p'
# 产品介绍
product_description_xpath = '//div[@class="yqyx-TRANS-product-intro-details-introduction-text"]'
# 售后服务
after_sale_xpath = '//div[@id="yqyx-TRANS-commitment"]/div[2]/p'

# 相关方案
relevant_solutions_xpath = '//div[@id="yqyx-TRANS-relatedplans"]'
relevant_solutions_num_xpath = '//div[@id="yqyx-TRANS-relatedplans"]/ul/li/a/@href'  # 计数

sample_detection_xpath = '//div[@class="s-c-top-item fl mb20"]/span[contains(text(), "检测样品")]/following-sibling::span/text()'  # 详情页内容
detection_item_xpath = '//div[@class="s-c-top-item fl mb20"]/span[contains(text(), "检测项目")]/following-sibling::span/text()'  # 详情页内容
vendor_logo_xpath = '//div[@class="inlineBlock s-v-left va"]/a/img/@src'
vendor_name_xpath = '//p[@class="tit omit inlineBlock"]/text()'
solution_detail_xpath = '//div[@class="s-detail-content positionR"]'

# 相关资料
relevant_article_xpath = '//ul[@id="yqyx-TRANS-introAbout3"]'
relevant_article_num_xpath = '//ul[@id="yqyx-TRANS-introAbout3"]/li/div[1]/a/@href'  # 计数

# 用户评价链接
user_evaluation_link_xpath = '//div[@class="yqyx-TRANS-product-intro-usercomments-footer"]/a/@href'
user_evaluation_xpath = '//div[@class="yqyx-TRANS-product-intro-usercomments-list"]/div'
user_evaluation_num_xpath = '//div[@class="pc-paging flex a-c j-c bgf"]/span/text()'


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
            item_['instru_link'] = href
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
        # 核心参数信息提取
        ps = response.xpath(core_parameters_xpath)
        if ps:
            item['core_parameters'] = {}
            for p in ps:
                parameters_name = p.xpath('./em/text()').extract_first().replace('：', '').strip()
                parameters_value = p.xpath('./i/text()').extract_first().strip()
                item['core_parameters'][parameters_name] = parameters_value
        else:
            item['core_parameters'] = None
        # 产品介绍
        item['product_description'] = response.xpath(product_description_xpath).get()
        # 售后服务
        ps = response.xpath(after_sale_xpath)
        if ps:
            item['after_sale_service'] = {}
            for p in ps:
                ass_name = p.xpath('./span[1]/text()').extract_first()
                ass_value = p.xpath('./span[2]/text()').extract_first()
                item['after_sale_service'][ass_name] = ass_value
        else:
            item['after_sale_service'] = None

        # 包含子页面部分
        sub_links_num = 0  # todo: 计算总的子页面链接数，方便决定什么时候返回item。但是评论里存在翻页，需要考虑这样是否可行
        finish_link_count = 0

        # 相关方案链接数
        sub_links_num += len(response.xpath(relevant_solutions_num_xpath).extract())
        # 相关资料链接数
        sub_links_num += len(response.xpath(relevant_article_num_xpath).extract())
        # 用户评论是否爬取完毕标志
        user_evaluation_finished = False

        item['sub_links_num'] = sub_links_num
        item['finish_link_count'] = finish_link_count
        item['user_evaluation_finished'] = user_evaluation_finished

        # 相关方案
        info = response.xpath(relevant_solutions_xpath)
        if info:
            item['relevant_solutions'] = {}
            id_category_dict = {}

            # 获取id-类别对
            category_infos = info.xpath('./div/div/a')
            for category_info in category_infos:
                category_id = category_info.xpath('./@data-name').extract_first()
                category_value = category_info.xpath('./text()').extract_first()
                id_category_dict[category_id] = category_value
                # 将类比信息填充至item
                item['relevant_solutions'][category_value] = []

            uls = info.xpath('./ul')
            for ul in uls:
                id_ = ul.xpath('./@id').extract_first()
                # 获得id对应的类别
                category = id_category_dict[id_]
                lis = ul.xpath('./li')
                for li in lis:
                    solution_href = li.xpath('./a/@href').extract_first()
                    solution_img = li.xpath('./a/img/@src').extract_first()
                    solution_title = li.xpath('./div/div/a/text()').extract_first()
                    solution_intro = li.xpath('./div/span/text()').extract_first()
                    solution_tag = li.xpath('./div/p/em/text()').extract_first()
                    solution_time = li.xpath('./div/p/i/text()').extract_first()
                    yield scrapy.Request(url=solution_href,
                                         callback=self.parse_relevant_solutions,
                                         dont_filter=True,
                                         meta={'item': item,
                                               'solution_img': solution_img,
                                               'solution_title': solution_title,
                                               'solution_intro': solution_intro,
                                               'solution_tag': solution_tag,
                                               'solution_time': solution_time,
                                               'category': category})
        else:
            item['relevant_solutions'] = None

        # 相关文章
        article = response.xpath(relevant_article_xpath)
        if article:
            item['relevant_article'] = []
            lis = article.xpath('./li')
            for li in lis:
                article_href = li.xpath('./div[1]/a/@href').extract_first()
                pdf_serial = re.search(r'down_(\d+)\.htm', article_href.split('/')[-1], re.S).group(1)
                article_title = li.xpath('./div[1]/a/text()').extract_first()
                article_time = li.xpath('./div[2]/span[2]/text()').extract_first()
                article_intro = li.xpath('./p/text()').extract_first()
                yield PdfUrlRequest(url=article_href,
                                    callback=self.parse_relevant_article,
                                    meta={'item': item,
                                          'article_title': article_title,
                                          'article_time': article_time,
                                          'article_intro': article_intro,
                                          'pdf_serial': pdf_serial})
        else:
            item['relevant_article'] = None

        # 用户评论
        user_evaluation = response.xpath(user_evaluation_link_xpath)
        if user_evaluation:
            item['user_evaluation'] = []
            evaluation_link = response.urljoin(user_evaluation.xpath('./a/@href').extract_first())
            yield scrapy.Request(url=evaluation_link,
                                 dont_filter=True,
                                 callback=self.parse_user_evaluation,
                                 meta={'item': item,
                                       'page': 1})
        else:
            item['user_evaluation'] = None

    def parse_relevant_solutions(self, response):
        '''
        解析相关方案详情页
        :param response:
        :return:
        '''
        item = response.meta['item']
        category = response.meta['category']  # 方案大类
        sample_detection = response.xpath(sample_detection_xpath).extract_first() if response.xpath(sample_detection_xpath).extract_first() else None  # 样本检测
        detection_item = response.xpath(detection_item_xpath).extract_first() if response.xpath(detection_item_xpath).extract_first() else None # 检测项目
        vendor_logo = response.xpath(vendor_logo_xpath).extract_first() if response.xpath(vendor_logo_xpath).extract_first() else None  # 厂商logo
        vendor_name = response.xpath(vendor_name_xpath).extract_first() if response.xpath(vendor_name_xpath).extract_first() else None  # 厂商名称
        solution_detail = response.xpath(solution_detail_xpath).get()

        item['relevant_solutions'][category].append({
            'solution_img': response.meta['solution_img'],
            'solution_title': response.meta['solution_title'],
            'solution_intro': response.meta['solution_intro'],
            'solution_tag': response.meta['solution_tag'],
            'publication_time': response.meta['solution_time'],
            'sample_detection': sample_detection,
            'detection_item': detection_item,
            'vendor_logo': vendor_logo,
            'vendor_name': vendor_name,
            'solution_detail': solution_detail
        })

        item['finish_link_count'] += 1
        if (item['finish_link_count'] == item['sub_links_num']) and (item['user_evaluation_finished'] is True):
            yield item

    def parse_relevant_article(self, response):
        '''
        解析相关文章详情页，获取pdf链接
        :param response:
        :return:
        '''
        item = response.meta['item']
        pdf_link = response.json()['data']
        item['relevant_article'].append({
            'article_title': response.meta['article_title'],
            'article_time': response.meta['article_time'],
            'article_intro': response.meta['article_intro'],
            'pdf_serial': response.meta['pdf_serial'],
            'pdf_link': pdf_link
        })

        item['finish_link_count'] += 1
        if (item['finish_link_count'] == item['sub_links_num']) and (item['user_evaluation_finished'] is True):
            yield item


    def parse_user_evaluation(self, response):
        '''
        重新考虑判断评论抓取完毕的逻辑，因为最后一个请求yield完成之后，就会执行修改逻辑，即使最后一个请求的爬取并未完成
        :param response:
        :return:
        '''
        item = response.meta['item']
        evaluation_divs = response.xpath(user_evaluation_xpath)
        for evaluation_div in evaluation_divs:
            user_name = evaluation_div.xpath('./div[1]/div/span/text()').extract_first()
            user_avatar = evaluation_div.xpath('./div[1]/div/img/@src').extract_first()
            evaluation_content = evaluation_div.xpath('./div[2]/text()').extract_first()
            evaluate_time = evaluation_div.xpath('./div[3]/em/text()').extract_first()
            item['user_evaluation'].append({
                'user_name': user_name,
                'user_avatar': user_avatar,
                'evaluation_content': evaluation_content,
                'evaluate_time': evaluate_time
            })

        evaluation_nums = re.search(r'(\d+)', response.xpath(user_evaluation_num_xpath).extract_first())
        pages = int(evaluation_nums.group(1)) // 10 + 1

        # 判断该当前是否是最后一页评论。若是，则修改标志为完成状态
        if response.meta['page'] == pages:
            item['user_evaluation_finished'] = True

        if (item['finish_link_count'] == item['sub_links_num']) and (item['user_evaluation_finished'] is True):
            yield item

        for page in range(2, pages+1):
            yield PdfUrlRequest(url=response.url + '&page=' + str(page),
                                callback=self.parse_user_evaluation,
                                meta={'item': item,
                                      'page': page})
