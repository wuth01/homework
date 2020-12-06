import datetime
import json
import logging
import requests



class Tag():
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.token=self.test_get_token()

    def status(self,r):
        try:
            assert r.status_code == 200
            assert r.json()['errcode'] == 0
        except AssertionError as E:
            logging.info(r.json())
        return r.json()

    def test_get_token(self):
        corpid = 'ww9f9937b00575cb31'
        corpsecret = 'zwP2nf2XpHJvBrCx_xIFdr1BkcdoXpQnmaKfPyL-JRs'

        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}

        )
        # print(json.dumps(r.json(), indent=2))
        self.status(r)

        token = r.json()['access_token']
        return token

    def add(self,group_name,tag):
        logging.info(group_name)
        logging.info(tag)
        while True:
            r = requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                params={"access_token": self.token},
                json={
                    "group_name": group_name,
                    "tag": tag
                }
            )
            status = self.status(r)
            if status['errcode'] == 0:
                tag_name = ""
                r = r.json()['tag_group']['tag']
                for i in r:
                    tag_name=i['name']
                logging.info(tag_name)
                return tag_name

            if status['errcode'] == 40071:
                group_id = self.get_group_id()
                self.delete_group_id(group_id)


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

    def delete_tag_id(self,tag_id):#通过tagid删除标签
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": tag_id
            }
        )
        self.status(r)

    def delete_group_id(self,group_id):#通过group_id删除标签
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "group_id": group_id
            }
        )
        self.status(r)

    def get_tag_id(self,group_name):
        logging.info(group_name)
        while True:
            r = self.list()
            r = r.json()['tag_group']
            # g = self.get_group_name()
            # for i in g:
            #     if i == group_name:
            tag_id = []
            for i in r:
                try:
                    if i['group_name'] == group_name:
                        tag = i['tag']
                        for i in tag:
                            tag_id.append(i['id'])
                        logging.info(f'{group_name}的tag_id是{tag_id}')
                        return tag_id
                    else:
                        logging.info(i['group_name'])
                except:
                    print(r)

    def get_group_name(self):
        r = self.list()
        r = r.json()['tag_group']
        group_name = []
        for i in r:
            group_name.append(i['group_name'])
        logging.info(f'group_name是:{group_name}')
        return  group_name

    def get_group_id(self):
        r = self.list()
        r = r.json()['tag_group']
        group_id = []
        for i in r:
            group_id.append(i['group_id'])
        logging.info(f'group_id是{group_id}')
        return group_id