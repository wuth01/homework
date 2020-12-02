# -*- coding: utf-8 -*-
"""
@author:wutianhao
@file:test_rewrite.py
@time:2020/11/30
"""
import json

from mitmproxy import http

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # print(data)
        # 修改第一支股票的名称
        name = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] = name + name
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)