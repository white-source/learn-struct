# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request,Spider
from ticketCrawler.items import TicketCrawlerItem
from scrapy.selector import Selector
import sys
from lxml import etree
from calculate import calculatePageNumber
class TicketSpider(scrapy.Spider):
    #爬虫标识
    name = "ticketCrawler"
    #爬虫起始url
    start_urls = ['http://www.chinaticket.com/']
    #文艺演出票url
    urls = {
        'yanchanghui':"http://www.chinaticket.com/wenyi/yanchanghui/",
        'huaju':"http://www.chinaticket.com/wenyi/huaju/",
        'yinlehui':"http://www.chinaticket.com/wenyi/yinlehui/",
        'yinleju':"http://www.chinaticket.com/wenyi/yinleju/",
        'xiqu':"http://www.chinaticket.com/wenyi/xiqu/",
        'baleiwu':"http://www.chinaticket.com/wenyi/baleiwu/",
        'qinzijiating':"http://www.chinaticket.com/wenyi/qinzijiating/",
        'zaji':"http://www.chinaticket.com/wenyi/zaji/",
        'xiangshengxiaopin':"http://www.chinaticket.com/wenyi/xiangshengxiaopin/",
        'zongyijiemu':"http://www.chinaticket.com/wenyi/zongyijiemu/",
        'zuqiu':"http://www.chinaticket.com/tiyu/zuqiu/",
        'gaoerfuqiu':"http://www.chinaticket.com/tiyu/gaoerfuqiu/",
        'Cbalanqiu':"http://www.chinaticket.com/tiyu/Cbalanqiu/",
        'saiche':"http://www.chinaticket.com/tiyu/saiche/",
        'quanji':"http://www.chinaticket.com/tiyu/quanji/",
        'dianyingpiao':"http://www.chinaticket.com/qita/dianyingpiao/",
        'jingdianmenpiao':"http://www.chinaticket.com/qita/jingdianmenpiao/",
        'zhanlan':"http://www.chinaticket.com/qita/zhanlan/",
        'yundongxiuxian':"http://www.chinaticket.com/qita/yundongxiuxian/",
        'lipinquan':"http://www.chinaticket.com/qita/lipinquan/",
        'huiyi':"http://www.chinaticket.com/qita/huiyi/",
    }
    #页面请求
    def start_requests(self):
        try:
            for key,value in self.urls.items():
                yield Request(value.encode('utf-8'),meta={"type":key.encode('utf-8')},callback=self.parse)
        except Exception as err:
            print err
    #获取下一页面url
    def get_next_url(self):
        try:
            pass
        except Exception as  err:
            print err

    #票标题页面解析函数
    def parse(self, response):
        try:
            item = TicketCrawlerItem()
            meta = response.meta
            result = response.text.encode("utf-8")
            if result == '' or result == 'None':
                print ("Can't get the sourceCode ")
                sys.exit()
            tree = etree.HTML(result)
            data = []
            #演出条数
            page = tree.xpath("//*[@class='s_num']/text()")[1].replace("\n","").replace(" ","").encode("utf-8")
            #页数
            calculateNum = calculatePageNumber()
            pageNUM = calculateNum.calculate_page_number(page)
            count = (pageNUM/10)+1
            # print count

            listDoms = tree.xpath("//*[@class='s_ticket_list']//ul")
            # print listDoms
            if(listDoms):
                for itemDom in listDoms:
                    # #数据存放
                    # itemData = {}
                    #type
                    item['type'] = meta['type'].encode("utf-8")
                    # print item['type']
                    #name
                    try:
                        titleDom = itemDom.xpath("li[@class='ticket_list_tu fl']/a/text()")
                        if(titleDom[0]):
                            item['name'] = titleDom[0].encode("utf-8")
                            # print item['name']
                    except Exception as err:
                        print err
                    #url
                    try:
                        urlDom = itemDom.xpath("li[@class='ticket_list_tu fl']/a/@href")
                        if(urlDom[0]):
                            item['url'] = urlDom[0].encode("utf-8")
                            # print item['url']
                    except Exception as err:
                        print err
                    #time
                    try:
                        timeDom = itemDom.xpath("li[@class='ticket_list_tu fl']/span[1]/text()")
                        if(timeDom[0]):
                            item['time'] = timeDom[0].encode("utf-8").replace('时间:','')
                            # print item['time']
                    except Exception as err:
                        print err
                    #address
                    try:
                        addressDom = itemDom.xpath("li[@class='ticket_list_tu fl']/span[2]/text()")
                        if(addressDom[0]):
                            item['address'] = addressDom[0].encode("utf-8").replace('地点:','')
                            # print item['address']
                    except Exception as err:
                        print err
                    #price
                    try:
                        priceDom = itemDom.xpath("li[@class='ticket_list_tu fl']/span[3]/text()")
                        if(priceDom[0]):
                            item['price'] = priceDom[0].encode("utf-8").replace('票价:','')
                            # print item['price']
                    except Exception as err:
                        print err
                    # data.append(item)
                    yield item
            for i in range(2,count+1):
                next_page = "http://www.chinaticket.com/wenyi/"+str(meta['type'])+"/?o=2&page="+str(i)
                if next_page is not None:
                    yield scrapy.Request(next_page, meta={"type":meta['type']},callback=self.parse)
        except Exception as err:
            print err

    #票详情页面解析函数
    def parseTicketDetail(self,response):
        try:
            pass
        except Exception as err:
            print err