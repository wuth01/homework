import datetime
import json

import requests
import yaml


class Tag():

    def __init__(self):
        self.token=self.test_get_token()

    def test_get_token(self):
        corpid = 'ww9f9937b00575cb31'
        corpsecret = 'zwP2nf2XpHJvBrCx_xIFdr1BkcdoXpQnmaKfPyL-JRs'

        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}

        )
        # print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        token = r.json()['access_token']
        return token

    def add(self,group_name,tag):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name": group_name,
                "tag": tag
            }
        )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        tag_id = []
        tag_name = []
        r = r.json()['tag_group']['tag']
        for i in r:
            tag_id.append(i['id'])
            tag_name.append(i['name'])
        return [tag_name,tag_id]

    def add_fail(self,group_name,tag):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name": group_name,
                "tag": tag
            }
        )
        return r
    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={
                'tag_id': []
            }
        )
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': tag_name
            }
        )
        return r

    def delete(self,tag_id):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": tag_id
            }
        )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'ok'

    def get_tag_id(self,group_name):
        r = self.list()
        r = r.json()['tag_group']
        tag_id = []
        for i in r:
            if i['group_name'] == group_name:
                tag = i['tag']
                for i in tag:
                    tag_id.append(i['id'])
        print(tag_id)
        return tag_id