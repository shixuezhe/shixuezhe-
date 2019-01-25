# -*- coding: utf-8 -*-

from shiyanlou.models import Repositories,engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
#        item['update_time']=datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Repositories(**item))
        return item
    def open_spider(self,spider):
        Session=sessionmaker(bind=engine)
        self.session=Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
