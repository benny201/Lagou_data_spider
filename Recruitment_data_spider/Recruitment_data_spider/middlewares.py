# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
from scrapy import signals
from fake_useragent import UserAgent
import random

class RecruitmentDataSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RecruitmentDataSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()

        self.ua = UserAgent()
        # self.per_proxy = crawler.settings.get('RANDOM_UA_PER_PROXY', False)
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')
        # self.proxy2ua = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            '''Gets random UA based on the type setting (random, firefox…)'''
            return getattr(self.ua, self.ua_type)

        # if self.per_proxy:
        #     proxy = request.meta.get('proxy')
        #     if proxy not in self.proxy2ua:
        #         self.proxy2ua[proxy] = get_ua()
        #         # logger.debug('Assign User-Agent %s to Proxy %s'
        #         #              % (self.proxy2ua[proxy], proxy))
        #     request.headers.setdefault('User-Agent', self.proxy2ua[proxy])
        # else:
        #     ua = get_ua()
        #     request.headers.setdefault('User-Agent', get_ua())

        # ua = get_ua()
        # request.headers.setdefault('User-Agent', get_ua())
        request.headers.setdefault('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9')

class RandomProxyMiddleware(object):
    #更改代理ip
    def process_request(self, request, spider):
        proxy_ips = [
            'http://f8310c05f6:jJqT75pf@104.227.62.143:4444',
            'http://f8310c05f6:jJqT75pf@104.227.6.47:4444',
            'http://f8310c05f6:jJqT75pf@104.227.62.143:4444',
            'http://f8310c05f6:jJqT75pf@107.152.198.15:4444',
            'http://f8310c05f6:jJqT75pf@107.152.254.94:4444',
            'http://f8310c05f6:jJqT75pf@198.20.178.247:4444',
            'http://f8310c05f6:jJqT75pf@198.20.180.214:4444',
            'http://f8310c05f6:jJqT75pf@198.20.180.214:4444',
            'http://f8310c05f6:jJqT75pf@23.254.10.201:4444',
            'http://f8310c05f6:jJqT75pf@23.254.3.189:4444',
            'http://f8310c05f6:jJqT75pf@104.144.129.185:4444',
            'http://f8310c05f6:jJqT75pf@104.144.197.81:4444',
            'http://f8310c05f6:jJqT75pf@107.152.240.79:4444',
            'http://f8310c05f6:jJqT75pf@138.128.51.251:4444',
            'http://f8310c05f6:jJqT75pf@192.186.168.227:4444',
            'http://f8310c05f6:jJqT75pf@192.241.84.127:4444',
            'http://f8310c05f6:jJqT75pf@198.154.82.181:4444',
            'http://f8310c05f6:jJqT75pf@23.254.11.161:4444',
            'http://f8310c05f6:jJqT75pf@23.254.17.77:4444',
            'http://f8310c05f6:jJqT75pf@45.72.3.253:4444'
        ]

        request.meta['proxy'] = proxy_ips[random.randint(0, proxy_ips.__len__() - 1)]
