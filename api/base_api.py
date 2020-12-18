import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww9f9937b00575cb31'
        corpsecret = 'zwP2nf2XpHJvBrCx_xIFdr1BkcdoXpQnmaKfPyL-JRs'
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        return r