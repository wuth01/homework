from mitmproxy import http


def request(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            # 读取文件中数据作为返回内容
            b"Hello World",
            # 指定返回数据的类型
            {"Content-Type": "text/html"}
        )