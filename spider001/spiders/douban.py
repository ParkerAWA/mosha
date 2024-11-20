# import scrapy
import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from spider001.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]

    # start_urls = ["https://movie.douban.com/top250"]

    # 设置url
    def start_requests(self):
        for page in range(1):
            yield Request(
                url=f"https://movie.douban.com/top250?start={page * 25}&filter=",
                # meta={'proxy': '127.0.0.1:54321'}
                # callback=self.parse,
            )

    # 起始页面

    def parse(self, response: HtmlResponse, **kwargs):
        """
        解析起始页面
        :param response:
        :return:
        """
        sel = Selector(response)

        list_items = sel.css("#content > div > div.article > ol > li")

        for list_item in list_items:
            detail_url = list_item.css('div.info > div.hd > a::attr(href)').extract_first()
            movie_item = MovieItem()
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            movie_item['rank'] = list_item.css('span.rating_num::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()

            # yield movie_item

            yield Request(
                url=detail_url,
                callback=self.parse_detail,
                # meta={'item': movie_item},
                cb_kwargs={'item': movie_item}
            )
        # # 解析分页url
        # href_list = sel.css(' div.paginator > a::attr(href)')
        # for href in href_list:
        #     url = response.urljoin(href.extract())
        #     yield Request(url=url)

    def parse_detail(self, response: HtmlResponse, **kwargs):
        """
        解析详情页面
        :param response:
        :return:
        """
        movie_item = kwargs['item']
        sel = Selector(response)
        # movie_item['time'] = sel.css('span[property = "v:runtime"]::text').extract()
        # span[property = v:runtime]::text
        # span[property = "v:runtime"]::attr(content)
        movie_item['director'] = sel.css('span.attrs > a::text').extract_first()
        yield movie_item
