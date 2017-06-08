
#-*- coding: utf-8 -*-

import os
import sys
import urllib2
import requests
import re
from lxml import etree

#结果存储文件函数
def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    with open(path, "w+") as fp:
        i=1
        for s in slist:
            fp.write("%s\t\t%s\t\t%s\n" % (i,s[0].encode("utf8"), s[1].encode("utf8")))
            i+=1

#获取第一级新闻分类，及其连接
def Page_Info(myPage):
    #正则表达式
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info


#根据第一级新闻连接，获取所有新闻标题和新闻连接
def PageInfo(new_page):
    #读取html源码
    dom = etree.HTML(new_page)
    #获取新闻标题列表
    new_items = dom.xpath('//tr/td/a/text()')
    #获取新闻href
    new_urls = dom.xpath('//tr/td/a/@href')
    #异常判断，标题列表长度和连接列表长度理论上应该是一样的
    assert(len(new_items) == len(new_urls))
    #新闻标题和新闻连接对应
    return zip(new_items, new_urls)

#爬取主体
def SpiderData(url):
    i=0
    print '爬取:',url
    #获取主页网页源代码
    newPage = requests.get(url).content.decode("gbk")
    myPageResults = Page_Info(newPage)
    #print newPageResults

    #获取第一级新闻大类；保存新闻分类和内容到txt文本中
    save_path = u"网易头条新闻爬取"
    filename = str(i)+"_"+u"新闻排行榜"
    StringListSave(save_path, filename, myPageResults)
    i += 1
    
    #获取每类新闻下的头条新闻；保存新闻标题和连接到txt文本中
    for item, url in myPageResults:
        try:
            print u"\t获取%s 新闻,地址：%s" % (item,url)   #为什么不带u会报错？         
            new_page = requests.get(url).content.decode("gbk")
            # new_page = urllib2.urlopen(url).read().decode("gbk")
            newPageResults = PageInfo(new_page)
            filename = str(i)+"_"+item
            StringListSave(save_path, filename, newPageResults)
            i += 1
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
        else:
            print '\t\t保存完成：',filename
    

#入口主函数  
if __name__== '__main__':
    print '爬取数据开始'
    url = "http://news.163.com/rank/"
    SpiderData(url)
    print '爬取数据结束'
