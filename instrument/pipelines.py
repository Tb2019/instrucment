# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class InstrumentPipeline:
    def process_item(self, item, spider):
        print('*****')
        print(item)
        return item


class ApplicationFieldPipeline:
    result = {}

    def process_item(self, item, spider):
        self.bi_category_2 = item['bi_category_2']
        if not self.result.get(item['bi_category_3'], None):
            self.result[item['bi_category_3']] = {}
            self.result[item['bi_category_3']][item['instru_name']] = [item['field']]
        else:
            if not self.result[item['bi_category_3']].get(item['instru_name'], None):
                self.result[item['bi_category_3']][item['instru_name']] = [item['field']]
            else:
                self.result[item['bi_category_3']][item['instru_name']] += [item['field']]
        # return item

    def close_spider(self, spider):
        with open(f'./ApplicationField/{self.bi_category_2}/application_field.json', 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False)
