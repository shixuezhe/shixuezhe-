# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from shiyan.models import Repositories,engine
from shiyan.items import ShiyanItem

class ShiyanPipeline(object):
    def process_item(self, item, spider):
        self.session.add(Repositories(**item))
    def open_spider(self,spider):
        Session=sessionmaker(bind=engine)
        self.session=Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()

