# 定义分页组件

"""
在视图函数中
def number_list(request, ):
    1.筛选数据

    queryset = models.number.objects.filter(**data_dict).order_by('-leve')
    2.实列化分页数据
    page_object = pagination(request, queryset)

    context = {'queryset': page_object.page_queryset,
               # 分页数据
               'search_data': search_data,
               'page_string': page_object.html()
               # 页码
               }

    return render(request, 'number_list.html', context)






    在HTML页面中：
     <div class=" clearfix" style="display: flex;justify-content: center">

            <ul class="pagination" style="float: left">
                {{ page_string }}
                <li>
                    <form style="float: left;margin-top: -1px;" method="get">
                        <input type="text" class="form-control"
                        style="position: relative;float: left;display: inline-block;width: 60px;border-radius: 0;"
                        name="page" placeholder="页码">
                        <button class="btn btn-default" type="submit">跳转</button>
                    </form>
                </li>
            </ul>

    </div>



"""

from django.utils.safestring import mark_safe


class pagination(object):
    def __init__(self, request, queryset, page_param='page', page_size=9, plus=5):
        """
        :param request: 请求对象
        :param queryset: 符合分页的数据
        :param page_param: url中查询参数的页码；列如：/?page=12
        :param page_size: 每页显示多少条数据
        :param plus: 页码前后显示多少页
        """

        import copy
        from django.http.request import QueryDict

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * 9
        self.end = page * 9
        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.total_page_count <= 2 * self.plus:
            start_page = 1
            end_page = self.total_page_count

        else:
            # 当前页码小于等于5
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
                # 当前页码大于5
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:

                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])

        page_str_list.append('<li class="disabled"><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])

            prev = '<li class="disabled"><a href="?{}">上一页</a></li>'.format(1)
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])

            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])

            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())

        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])

            prev = '<li class="disabled"><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])

        page_str_list.append('<li class="disabled"><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))
        page_string = mark_safe(''.join(page_str_list))
        """
        <li><a href="http://127.0.0.1:8000/number/list/">1</a></li>
                    <li><a href="?page=2">2</a></li>
                    <li><a href="?page=3">3</a></li>
                    <li><a href="?page=4">4</a></li>
                    <li><a href="?page=5">5</a></li>
        """
        return page_string
