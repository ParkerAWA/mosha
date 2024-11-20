from django.http import JsonResponse
from django.shortcuts import render


# 数据统计页面
def echarts_list(request):
    return render(request, 'echarts_list.html')


# 构造柱状图的数据
def echarts_bar(request):

    # 数据可以到数据库中取
    legend_list = ['zxl',  '木森']
    a=[5, 20, 36, 10, 10, 50]

    series_list = [
        {
            'name': 'zxl',
            'type': 'bar',
            'data': a
        },
        {
            'name': '木森',
            'type': 'bar',
            'data': [25, 30, 40, 50, 15, 20]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        'status': True,
        'legend_list': legend_list,
        'series_list': series_list,
        'x_axis': x_axis
    }
    return JsonResponse(result)


# 构造饼图的数据
def echarts_pie(request):
    series_list = [
        {'value': 400, 'name': 'andy'},
        {'value': 735, 'name': '周祥龙'},
        {'value': 580, 'name': 'zxl'},
        {'value': 484, 'name': '木森'},
        {'value': 300, 'name': 'parker'}
    ]
    result = {
        'status': True,
        'series_list': series_list
    }
    return JsonResponse(result)


# 构造线性图的数据
def echarts_line(request):
    series_list = [
        {
            'name': 'andy',
            'type': 'line',
            'data': [5, 20, 36, 10, 10, 50]
        },
        {
            'name': 'parker',
            'type': 'line',
            'data': [25, 30, 40, 50, 15, 20]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    legend = ['andy', 'parker']

    result = {
        'status': True,
        'series_list': series_list,
        'x_axis': x_axis,
        'legend_list': legend
    }
    return JsonResponse(result)
