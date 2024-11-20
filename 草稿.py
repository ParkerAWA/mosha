# 草稿1
# $.ajax({
#     url: '/order/add/',
#     type: 'post',
#     data: $("#formadd").serialize(),
#            dataTypes: 'json',
# success: function(res)
# {
# if (res.status)
# {
#     {
# # alert('成功');#}
#
# $("#formadd")[0].reset();
# {
# # 清空表单#}
# $('#myModal').modal('hide');
# {  # 关闭模态框#}
#     location.reload();
# {  # 用js刷新页面#}
#
# } else {
# $.each(res.error, function(name, errorlist)
# {
#     {
# # console.log(name, data);#}
# $('#id_' + name).next().text(errorlist[0]);
#
# })
# }
#
# }
# })
# // 向后台发送添加的ajax请求

# 草稿2
# $.ajax({
#     url: '/echarts/bar/',
#     type: 'get',
#     dataType: 'json',
#     success: function(res) {
#                            // 将后台返回的数据更新到option中
#     if (res.status) {
#         option.legend.data = res.data.legend_list;
# option.xAxis.data = res.data.x_axis;
# option.series = res.data.series_list;
# // 使用刚指定的配置项和数据显示图表。
# myChart.setOption(option);
#
# }
#
# }
# })
def my_write():
    file = open('a.txt', 'w', encoding='utf-8')
    file.write('hello world')
    file.close()


if __name__ == '__main__':
    my_write()