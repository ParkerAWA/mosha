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
        self.data = []

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')

        self.data.append((title, rank, subject))

        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()

        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into tb_top_movie(title,rating,subject) values(%s,%s,%s)',
            self.data
        )
        self.conn.commit()

