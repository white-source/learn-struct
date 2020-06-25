# -*- coding: utf-8 -*-
import re
#计算页面数量
class calculatePageNumber():

    def calculate_page_number(self,page):
        try:
            result = re.findall(r"\d+\.?\d*",page)
            return int(result[0])
        except Exception as err:
            print err

