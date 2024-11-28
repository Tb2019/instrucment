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
    rs_image = scrapy.Field()  # 相关方案-图片
    rs_title = scrapy.Field()  # 相关方案-标题
    rs_case_description = scrapy.Field()  # 相关方案-案例介绍
    rs_application_field = scrapy.Field()  # 相关方案-应用领域
    rs_release_date = scrapy.Field()  # 相关方案-发布时间
    rs_test_sample = scrapy.Field()  # 相关方案-检测样品
    rs_test_item = scrapy.Field()  # 相关方案-检测项目
    rs_case_details = scrapy.Field()  # 相关方案-案例详情
    rs_manufacturer_logo = scrapy.Field()  # 相关方案-厂商LOGO
    rs_manufacturer_name = scrapy.Field()  # 相关方案-厂商名称
    ra_title = scrapy.Field()  # 相关文章-标题
    ra_release_date = scrapy.Field()  # 相关文章-发布时间
    ra_article_details = scrapy.Field()  # 相关文章-文章详情
    ass_warranty_period = scrapy.Field()  # 售后服务-保修期
    ass_extendable_warranty = scrapy.Field()  # 售后服务-是否可延长保修期
    ass_on_site_tech_consul = scrapy.Field()  # 售后服务-现场技术咨询
    ass_free_training = scrapy.Field()  # 售后服务-免费培训
    ass_free_instr_maintenance = scrapy.Field()  # 售后服务-免费仪器保养
    ass_warranty_repair_commit = scrapy.Field()  # 售后服务-保内维修承诺
    ass_repair_request_commit = scrapy.Field()  # 售后服务-报修承诺
    ue_user_avatar = scrapy.Field()  # 用户评价-用户头像
    ue_username = scrapy.Field()  # 用户评价-用户名
    ue_product_quality_rating = scrapy.Field()  # 用户评价-产品质量评分
    ue_after_sales_service_rating = scrapy.Field()  # 用户评价-售后服务评分
    ue_usability_rating = scrapy.Field()  # 用户评价-易用性评分
    ue_cost_performance_rating = scrapy.Field()  # 用户评价-性价比评分
    ue_comment_text = scrapy.Field()  # 用户评价-评论文字
    ue_comment_images = scrapy.Field()  # 用户评价-评论图片
    ue_publish_time = scrapy.Field()  # 用户评价-发布时间
