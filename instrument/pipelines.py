# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging
import pymysql
import scrapy.pipelines.files
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 获取应用领域
class InstrumentPipeline:
    def __init__(self, category_2):
        self.category_2 = category_2

    @classmethod
    def from_crawler(cls, crawler):
        # print([*crawler.settings])
        # print(f'我获取了二级分类为：{crawler.settings["BI_CATEGORY_2"]}')
        return cls(crawler.settings.get('BI_CATEGORY_2'))

    def open_spider(self, spider):
        self.file = open(f'./instrument/ApplicationField/{self.category_2}/application_field.json', 'r', encoding='utf-8')
        self.field_content = json.load(self.file)

    def process_item(self, item, spider):
        instru_name = item['bi_instrument_name']
        instru_category_3 = item['bi_category_3']
        item['bi_application_field'] = self.field_content[instru_category_3].get(instru_name.strip(), None)
        # print(item)
        return item

    def close_spider(self, spider):
        self.file.close()


# 下载pdf文件
class InstruPdfDownloadPipeline(scrapy.pipelines.files.FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        pdf_serial = request.meta['pdf_serial']
        file_name = f'{pdf_serial}.pdf'
        return file_name

    def item_completed(self, results, item, info):
        return item

    def get_media_requests(self, item, info):
        if item['relevant_article']:
            for article in item['relevant_article']:
                pdf_serial = article['pdf_serial']
                pdf_link = article['pdf_link']
                yield scrapy.Request(pdf_link, meta={'pdf_serial': pdf_serial})

    def media_failed(self, failure, request, info):
        logging.error(f"Download failed: {failure}, URL: {request.url}")
        super().media_failed(failure, request, info)


# 保存到mysql数据库
class Save2MysqlPipeline:
    def __init__(self, host, port, db, user, password, table, table_fields):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.table = table
        self.table_fields = table_fields

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings.get('MYSQL_HOST')
        port = crawler.settings.get('MYSQL_PORT')
        db = crawler.settings.get('MYSQL_DB')
        user = crawler.settings.get('MYSQL_USER')
        password = crawler.settings.get('MYSQL_PASSWORD')
        table = crawler.settings.get('MYSQL_TABLE')
        table_fields = crawler.settings.get('TABLE_FIELDS')
        pipeline = cls(host, port, db, user, password, table, table_fields)
        return pipeline

    def open_spider(self, spider):
        self.db = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.password)

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        table = self.table
        item_ = {}
        for key, value in item.items():
            if key in self.table_fields:
                item_[key] = str(value) if value is not None else None
            else:
                continue
        keys = ','.join(item_.keys())
        values = ','.join(['%s'] * len(item_))
        cursor = self.db.cursor()
        sql = f'insert into {table}({keys}) values({values})'
        try:
            cursor.execute(sql, tuple(item_.values()))
            self.db.commit()
            print('存储成功')
        except Exception as e:
            self.db.rollback()
            print('存储失败', e)


# 应用领域爬虫的单独pipeline，将应用领域信息保存为json文件
class ApplicationFieldPipeline:
    result = {}

    def process_item(self, item, spider):
        self.bi_category_2 = item['bi_category_2']

        if not self.result.get(item['bi_category_3'], None):
            self.result[item['bi_category_3']] = {}
            self.result[item['bi_category_3']][item['instru_name'].strip()] = [item['field']]
        else:
            if not self.result[item['bi_category_3']].get(item['instru_name'], None):
                self.result[item['bi_category_3']][item['instru_name'].strip()] = [item['field']]
            else:
                self.result[item['bi_category_3']][item['instru_name'].strip()] += [item['field']]
        # return item

    def close_spider(self, spider):
        with open(f'./instrument/ApplicationField/{self.bi_category_2}/application_field.json', 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False)
