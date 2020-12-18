import logging
import requests

from api.base_api import BaseApi


class Tag(BaseApi):
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        super().__init__()

    def status(self,r):
        try:
            assert r.status_code == 200
            assert r.json()['errcode'] == 0
        except AssertionError as E:
            logging.info(r.json())
        return r.json()

    def add(self,group_name,tag,**kwargs):
        logging.info(group_name)
        logging.info(tag[0]['name'])
        while True:
            data = {
                "method": "post",
                "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                "params": {"access_token": self.token},
                "json" : {"group_name": group_name,"tag": tag,**kwargs}
            }
            r = self.send(data)
            status = self.status(r)
            if status['errcode'] == 0:
                tag_name = ""
                r = r.json()['tag_group']['tag']
                for i in r:
                    tag_name=i['name']
                logging.info(tag_name)
                return tag_name

            if status['errcode'] == 40071:
                tag_name = tag[0]['name']
                tag_id = self.get_tag_name_id(group_name,tag_name)
                logging.info(tag_id)
                # group_id = self.get_group_id()
                # self.delete_group_id(group_id)
                self.delete_tag_id(tag_id)
            if status['errcode'] == 40068:
                logging.info(status['errcode'])


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
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": self.token},
            "json": { 'tag_id': []}
        }
        r = self.send(data)
        return r

    def update(self, id, tag_name):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            "params": {"access_token": self.token},
            "json":{
                'id': id,
                'name': tag_name
            }
        }
        r = self.send(data)
        return r

    def delete_tag_id(self,tag_id):#通过tagid删除标签
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id
            }
        }
        r = self.send(data)
        self.status(r)
        logging.info(r.json())
        return r.json()

    def delete_group_id(self,group_id):#通过group_id删除标签
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id
            }
        }
        r = self.send(data)
        self.status(r)

    def get_tag_id(self,group_name):
        logging.info(group_name)
        while True:
            r = self.list()
            r = r.json()['tag_group']
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

    def get_tag_name_id(self,group_name,tag_name):
        logging.info(tag_name)
        r = self.list()
        r = r.json()['tag_group']
        tag_id = []
        for i in r:
            try:
                if i['group_name'] == group_name:
                    tag = i['tag']
                    for i in tag:
                        if tag_name == i['name']:
                            tag_id.append(i['id'])
                    logging.info(f'{tag_name}的tag_id是{tag_id}')
                    return tag_id
                else:
                    logging.info(i['group_name'])
            except:
                logging.info(r)

        return tag_id

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