# -*- coding: utf-8 -*-

import os
import sys
import scrapy
from scrapy.cmdline import execute
#找到main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','ticketCrawler'])