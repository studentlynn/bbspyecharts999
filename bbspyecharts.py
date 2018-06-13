# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import Response
from flask import Flask, render_template
from pyecharts import Bar
"""
Windows 系统
set FLASK_APP=bbspyecharts.py
flask run
"""
app = Flask(__name__)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/')
def bbspyecharts():
	# bar = Bar("我的第一个图表", "这里是副标题")
	# # bar.use_theme('dark') 更换主体色系
	# bar.add("服装"
	# 		, ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	# 		, [5, 20, 36, 10, 75, 90]
	# 		, is_more_utils=True)
	# # is_more_utils = True 按右边的下载按钮将图片下载到本地
	#
	# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
	# bar.render()  # 生成本地 HTML 文件
	# # bar.render(r"/templates/my_first_chart.html")
	# # return 'Hello World!'
	return Response_headers('hello world')


if __name__ == '__main__':
	app.run()
