# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy import log
import settings
from items import TicketCrawlerItem
from sqlalchemy import create_engine,Table,Column
from sqlalchemy import Integer,String,MetaData,VARCHAR,DATETIME,TEXT
#票概要信息
class TicketcrawlerPipeline(object):

    def __init__(self):

        try:
            # 数据库连接
            self.connect = pymysql.connect(
                host=settings.MYSQL_HOST,
                db = settings.MYSQL_DBNAME,
                user = settings.MYSQL_USER,
                passwd = settings.MYSQL_PASSWORD,
                charset = settings.MYSQL_CHARSET,
            )
            #游标
            self.cursor = self.connect.cursor()
        except Exception as err:
            print err
    #处理数据
    def process_item(self, item, spider):

        if item.__class__==TicketCrawlerItem:
            try:
                #创建数据表,若表存在则忽略
                self.createTable()
                #插入sql语句
                sqlInsert = "INSERT INTO ticketCrawler.tickets(name,price,time,address,type,url)values(%s,%s,%s,%s,%s,%s)"
                self.insertIntoTable(item['url'],sqlInsert,item)
            except Exception as err:
                print err

        return item

    #创建表
    def createTable(self):

        try:
            #创建连接
            engine = create_engine("mysql+mysqldb://root:xxxxxx@127.0.0.1:3306/ticketCrawler?charset=utf8", max_overflow=10000)
            #获取元数据
            metadata = MetaData()
            #定义表
            tickets = Table('tickets',metadata,
                            Column('id',Integer,primary_key=True),
                            Column('name',VARCHAR(256)),
                            Column('price',VARCHAR(256)),
                            Column('time',VARCHAR(256)),
                            Column('address',VARCHAR(256)),
                            Column('type',VARCHAR(256)),
                            Column('url',VARCHAR(256)),
                            Column('introduction',TEXT),
                            Column('last_update_time',DATETIME)
            )
            metadata.create_all(engine)
        except Exception as err:
            print err

    #插入数据表
    def insertIntoTable(self,url,sql,item):
        try:
            engine = create_engine("mysql+mysqldb://root:xxxxx@127.0.0.1:3306/ticketCrawler?charset=utf8",max_overflow=10000)
            #插入去重判断
            selectSql = "SELECT COUNT(*) FROM tickets WHERE url = '%s'" % url
            result = engine.execute(selectSql)
            count_exist = result.fetchall()
            if count_exist[0][0]>=1:
                print "数据表中已有数据"
            else:
                engine.execute(sql,(item['name'],item['price'],item['time'],item['address'],item['type'],item['url']))
        except Exception as err:
            print err
    #更新数据表introduction
    def updateTable(self):
        try:
            pass
        except Exception as err:
            print err

# #介绍
# class IntroCrawlerPipeline(object):
#     pass





