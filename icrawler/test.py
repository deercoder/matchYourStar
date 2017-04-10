# -*- coding: utf-8 -*-

import logging
import sys
from datetime import date

from icrawler.builtin import (BaiduImageCrawler, BingImageCrawler,
                              FlickrImageCrawler, GoogleImageCrawler,
                              GreedyImageCrawler, UrlListCrawler)

star_list = {
u'范冰冰',
u'周杰伦',
u'谢霆锋',
u'成龙',
u'黄晓明',
u'孙俪',
u'赵薇',
u'刘德华',
u'李易峰',
u'陈奕迅',
u'邓紫棋',
u'Angelababy',
u'李冰冰',
u'汪峰',
u'李娜',
u'蔡依林',
u'周迅',
u'刘嘉玲',
u'李晨',
u'唐嫣',
u'章子怡',
u'黄渤',
u'郭富城',
u'王力宏',
u'古天乐',
u'吴奇隆',
u'邓超',
u'林志玲',
u'周润发',
u'刘诗诗',
u'杨幂',
u'舒淇',
u'吴秀波',
u'冯小刚',
u'刘恺威',
u'姜文',
u'鹿晗',
u'陆毅',
u'罗志祥',
u'张嘉译',
u'姚晨',
u'吴亦凡',
u'赵丽颖',
u'五月天',
u'钟汉良',
u'甄子丹',
u'吴镇宇',
u'霍建华',
u'梁朝伟',
u'贾乃亮',
u'佟大为',
u'韩寒',
u'萧敬腾',
u'闫妮',
u'汤唯',
u'宁浩',
u'海清',
u'黄磊',
u'那英',
u'李宗盛',
u'陈乔恩',
u'李宇春',
u'胡歌',
u'郎朗',
u'唐家三少',
u'佟丽娅',
u'刘涛',
u'徐峥',
u'陈赫',
u'陈伟霆',
u'王宝强',
u'林丹',
u'王菲',
u'陈晓',
u'徐熙娣',
u'高圆圆',
u'林更新',
u'郭敬明',
u'苏打绿',
u'张歆艺',
u'郭采洁',
u'林心如',
u'张智霖',
u'马苏',
u'陈妍希',
u'郑恺',
u'彭于晏',
u'何炅',
u'刘烨',
u'田馥甄',
u'华晨宇',
u'TFBOYS',
u'李云迪',
u'羽泉',
u'蔡卓妍',
u'张杰',
u'周星驰',
u'冯绍峰',
u'郭德纲',
u'汪涵'
}

def test_google():
    for item in star_list:
	filename = item.encode('utf-8')
    	google_crawler = GoogleImageCrawler(
        	downloader_threads=4,
        	storage={'root_dir': 'images/google/'+filename},
        	log_level=logging.INFO)
    	google_crawler.crawl(
        	item,
        	max_num=50,
        	date_min=date(2016, 2, 1),
        	date_max=date(2016, 3, 15))


def test_bing():
    bing_crawler = BingImageCrawler(
        storage={'root_dir': 'images/bing'}, log_level=logging.DEBUG)
    bing_crawler.crawl('sunny', max_num=10)


def test_baidu():
    baidu_crawler = BaiduImageCrawler(
        downloader_threads=4, storage={'root_dir': 'images/baidu'})
    baidu_crawler.crawl('bird', max_num=10)


def test_flickr():
    flickr_crawler = FlickrImageCrawler(
        apikey=None,
        downloader_threads=4,
        storage={'root_dir': 'images/flickr'})
    flickr_crawler.crawl(
        max_num=10,
        tags='family,child',
        tag_mode='all',
        group_id='68012010@N00')


def test_greedy():
    greedy_crawler = GreedyImageCrawler(
        parser_threads=4, storage={'root_dir': 'images/greedy'})
    greedy_crawler.crawl(
        'http://www.bbc.com/news', max_num=10, min_size=(100, 100))


def test_urllist():
    urllist_crawler = UrlListCrawler(
        downloader_threads=3, storage={'root_dir': 'images/urllist'})
    urllist_crawler.crawl('test_data/test_list.txt')


def main():
    if len(sys.argv) == 1:
        dst = 'all'
    else:
        dst = sys.argv[1:]
    if 'all' in dst:
        dst = ['google', 'bing', 'baidu', 'flickr', 'greedy', 'urllist']
    if 'google' in dst:
        test_google()
    if 'bing' in dst:
        test_bing()
    if 'baidu' in dst:
        test_baidu()
    if 'flickr' in dst:
        test_flickr()
    if 'greedy' in dst:
        test_greedy()
    if 'urllist' in dst:
        test_urllist()


if __name__ == '__main__':
    main()
