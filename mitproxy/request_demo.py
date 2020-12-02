from mitmproxy import http


def request(flow: http.HTTPFlow):
    #增加请求头信息中心的字段
    flow.request.headers["myheader"] = "wuitianhao"
    print(flow.request.headers)
