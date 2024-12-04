# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstrumentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewProductItem(scrapy.Item):
    instru_link = scrapy.Field()  # 仪器链接
    bi_category_1 = scrapy.Field()  # 基本信息-1级分类
    bi_category_2 = scrapy.Field()  # 基本信息-2级分类
    bi_category_3 = scrapy.Field()  # 基本信息-3级分类
    bi_brand = scrapy.Field()  # 基本信息-品牌
    bi_application_field = scrapy.Field()  # 基本信息-应用领域
    bi_origin_category = scrapy.Field()  # 基本信息-产地类别
    bi_origin = scrapy.Field()  # 基本信息-产地
    bi_manufacturer_type = scrapy.Field()  # 基本信息-厂商性质
    bi_instrument_name = scrapy.Field()  # 基本信息-仪器名称
    bi_instrument_image = scrapy.Field()  # 基本信息-仪器图片
    bi_model_number = scrapy.Field()  # 基本信息-型号
    bi_manufacturer_name = scrapy.Field()  # 基本信息-厂商名称
    bi_manufacturer_logo = scrapy.Field()  # 基本信息-厂商LOGO
    bi_business_license_status = scrapy.Field()  # 基本信息-营业执照审核状态
    bi_rating = scrapy.Field()  # 基本信息-评分
    bi_reference_price = scrapy.Field()  # 基本信息-参考报价
    bi_sample_src = scrapy.Field()  # 基本信息-样本链接
    core_parameters = scrapy.Field()  # 核心参数
    product_description = scrapy.Field()  # 产品介绍
    after_sale_service = scrapy.Field()  # 售后服务相关
    relevant_solutions = scrapy.Field()  # 相关方案
    relevant_article = scrapy.Field()   # 相关文章
    user_evaluation = scrapy.Field()  # 用户评价

    category = scrapy.Field()  # 方案大类
    sub_links_num = scrapy.Field()
    finish_link_count = scrapy.Field()
    user_evaluation_finished = scrapy.Field()
    evaluation_finished = scrapy.Field()
