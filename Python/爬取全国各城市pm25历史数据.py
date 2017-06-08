
#-*- coding: utf-8 -*-

import os
import sys
import urllib2
import requests
import re
from lxml import etree
import csv
import codecs

base_url = 'https://www.aqistudy.cn/historydata/'
result_List =[]#所有爬取结果

#记录对象
class AirQualityItem:
    city_name = ''      # 城市名称
    record_date = ''    # 检测日期
    aqi_val = ''        # AQI
    range_val = ''      # 范围
    quality_level = ''  # 质量等级
    pm2_5_val = ''      # PM2.5
    pm10_val = ''       # PM10
    so2_val = ''        # SO2
    co_val = ''         # CO
    no2_val = ''        # NO2
    o3_val = ''         # O3
    rank = ''           # 排名

#对含中文参数url地址编码
def encodeurl(url):
    url=url.encode('utf-8')
    url=urllib2.unquote(url)
    return url

#获取某个url下网页html源码
def getWebHTML(url):
    url = encodeurl(url)
    code = urllib2.urlopen(url).read()
    dom = etree.HTML(code)
    return dom

#结果存储文件函数
def SaveCSV(filename,data):
    print '准备保存爬取数据，总记录数：',len(data)
    csvfile = file(filename, 'wb')
    #防止csv中中文乱码
    csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile)
    writer.writerow(['城市','检测日期', 'AQI', '范围','质量等级', 'PM2.5', 'PM10',
                     'SO2', 'CO', 'NO2','O3','排名']) 
    writer.writerows(data)    
    csvfile.close() 


#解析某城市的月份数据
def city_month(monthlist_url):       
    # 获取该城市的所有月份URL
    print '获取该城市的所有月份URL',monthlist_url
    dom = getWebHTML(monthlist_url)    
    monthurl_list = dom.xpath('//table[@class="table table-condensed '
                                        'table-bordered table-striped table-hover '
                                        'table-responsive"]//a//@href')
    i=0
    for month_url in monthurl_list:
        #if i>0:
        #    break
        # 依次遍历月份URL
        cityday_url = base_url + month_url
        # 解析该城市的每日数据
        city_day(cityday_url)
        i+=1

#解析该城市的每日数据
def city_day(day_url):    
    city_url_name = day_url[day_url.find('=') + 1:day_url.find('&')]
    
    
    # 获取每日记录
    dom = getWebHTML(day_url)
    day_record_list = dom.xpath('//table[@class="table table-condensed '
                                        'table-bordered table-striped table-hover '
                                        'table-responsive"]//tr')
    # 解析url中文
    item = AirQualityItem()
    item.city_name = city_url_name.encode('utf8') # parse.unquote(city_url_name)
    for i, day_record in enumerate(day_record_list):
        # 跳过表头
        if i == 0:        
            continue        
        td_list = day_record.xpath('.//td')
        item.record_date = td_list[0].xpath('text()')[0].rstrip().encode('utf8')           # 检测日期
        item.aqi_val = td_list[1].xpath('text()')[0].rstrip().encode('utf8')               # AQI
        item.range_val = td_list[2].xpath('text()')[0].rstrip().encode('utf8')             # 范围
        item.quality_level = td_list[3].xpath('.//div/text()')[0].rstrip().encode('utf8')  # 质量等级
        item.pm2_5_val = td_list[4].xpath('text()')[0].rstrip().encode('utf8')             # PM2.5
        item.pm10_val = td_list[5].xpath('text()')[0].rstrip().encode('utf8')              # PM10
        item.so2_val = td_list[6].xpath('text()')[0].rstrip().encode('utf8')               # SO2
        item.co_val = td_list[7].xpath('text()')[0].rstrip().encode('utf8')                # CO
        item.no2_val = td_list[8].xpath('text()')[0].rstrip().encode('utf8')               # NO2
        item.o3_val = td_list[9].xpath('text()')[0].rstrip().encode('utf8')                # O3
        item.rank = td_list[10].xpath('text()')[0].rstrip().encode('utf8')                 # 排名

        itemtuple =(item.city_name,item.record_date,item.aqi_val,item.range_val,item.quality_level,
                    item.pm2_5_val,item.pm10_val,item.so2_val,item.co_val,
                    item.no2_val,item.o3_val,item.rank)
        result_List.append(itemtuple)
        print '当前城市：',city_url_name,item.record_date
        
           
#爬取主体
def SpiderData(url):
    try:    
        print '爬取:',url        
        #获取主页网页源代码
        dom = getWebHTML(url)
        
        # 获取所有城市的URL
        i =0
        cityurl_list = dom.xpath('//div[@class="all"]//div[@class="bottom"]//a//@href')
        for url in cityurl_list:
            #获取各城市月份数据有效url
            monthlist_url = base_url+url
            print '正在爬取月数据：',monthlist_url
            city_month(monthlist_url)
            i+=1
    finally :
            print '爬取结束！'
                    

#入口主函数  
if __name__== '__main__':

    #爬取数据存储内存
    print '爬取天气数据开始'
    #url = 'https://www.aqistudy.cn/historydata/index.php'
    url = "https://www.aqistudy.cn/historydata"
    SpiderData(url)

    #保存结果数据到csv
    SaveCSV(u'PM25各城市历史数据.CSV',result_List)

    
    print '爬取天气数据结束'
