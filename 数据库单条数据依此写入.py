import pymysql


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

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')

        self.cursor.execute(
            'insert into tb_top_movie(title,rating,subject) values(%s,%s,%s)',

            (title, rank, subject)
        )
        return item
