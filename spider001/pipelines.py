# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import openpyxl
import pymysql

"""
  钩子函数---回调函数---当爬虫结束时会自动调用此函数
  """


class ExcelPipeline:
    """
    向Excel文件写入数据
    """

    def __init__(self):
        self.wb = openpyxl.Workbook()
        # 工作簿
        # wb.create_sheet(index=0, title='top250')
        # 新建表，index=0表示将新工作表插入到工作簿的第一个位置，即成为第一个工作表。

        self.ws = self.wb.active
        # 获取工作簿的工作表
        self.ws.title = 'top250'

        self.ws.append(('标题', '评分', '主题', '时长', '导演'))
        # 加表头

    # def open_spider(self, spider):

    # 在爬虫启动时执行的操作。

    def close_spider(self, spider):
        """

        在爬虫关闭时执行的操作。

         爬虫关闭时自动调用的回调函数。

        此方法被设计为在爬虫结束时调用，它的目的是保存当前的工作簿到一个Excel文件，
        并关闭这个工作簿。这确保了所有的爬虫数据都被正确地保存，而且资源（如文件句柄）
        被适当地释放。

        参数:
        - spider: 表示当前关闭的爬虫对象。虽然在这个方法中没有直接使用这个参数，
                  它的存在是为了符合Scrapy框架中回调函数的常规签名。
            """
        self.wb.save('电影数据.xlsx')

    # process_item----处理item
    def process_item(self, item, spider):
        """
        数据处理，每拿到一条数据就调用一次
        :param item:
        :param spider:
        :return:
        """

        title = item.get('title', '')
        # 拿到title返回title，如果没有则返回空字符串
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        time = item.get('time', '')
        director = item.get('director', '')
        self.ws.append((title, rank, subject, time, director))
        # 向表格中添加数据
        # item---是爬虫返回的item，这里是指我们爬取的数据
        # 爬虫获取的数据需要封装成Item对象，Item对象中封装了爬取到的数据

        return item


class DBPipeline:
    """
    向MySQL数据库写入数据
    """

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='movie',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        time = item.get('time', '')
        director = item.get('director', '')

        self.data.append((title, rank, subject, time, director))

        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()

        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into tb_top_movie(title,rating,subject,showtime,director) values(%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()
