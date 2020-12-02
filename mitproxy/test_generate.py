# -*- coding: utf-8 -*-
"""
@author:wutianhao
@file:test_rewrite.py
@time:2020/11/30
"""
import json

from mitproxy.generate_testcase import json_travel


def test_json_travel():
    with open("./datas/mok.json", encoding='utf-8') as f:
        data = json.load(f)
        print(json.dumps(json_travel(data, array=3),indent=2, ensure_ascii=False))
        # print(json.dumps(json_travel(data, text=4), indent=2, ensure_ascii=False))
        # print(json.dumps(json_travel(data, num=6), indent=2, ensure_ascii=False))
    return data
