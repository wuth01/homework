# -*- coding: utf-8 -*-
"""
@author:wutianhao
@file:test_rewrite.py
@time:2020/11/30
"""
import json

from mitmproxy import http

def request(flow: http.HTTPFlow):
    with open("./datas/mok.json", encoding='utf-8') as f:
        data = f.read()
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件

            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中数据作为返回内容
                data,
                # 指定返回数据的类型
                {"Content-Type": "application/json"}  # (optional) headers
            )

