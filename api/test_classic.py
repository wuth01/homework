import datetime
import json

import requests


# todo: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# todo: 代码冗余，需要封装
# todo: 无法清晰的描述业务
# todo: 使用jsonpath表达更灵活的递归查找

def test_tag_list():
    """
    获取access_token
    """
    corpid = 'ww9f9937b00575cb31'
    corpsecret = 'zwP2nf2XpHJvBrCx_xIFdvxm_7IDi9tlLKVxWpVqF44'

    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}

    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token = r.json()['access_token']
    """
    获取标签列表
    """
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    """
    更新标签名字
    """
    tag_name = 'tag1_new_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            'id': 'etZr3CEAAAGT3VFfvEHKrfzcGLLodcxg',
            'name': tag_name
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    """
    获取标签列表
    """
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == '测试'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    # jsonpath(f"$..[?(@.name='{tag_name}')]") jmepath
    assert tags != []
def test_add_tag():
    """
    获取access_token
    """
    corpid = 'ww9f9937b00575cb31'
    corpsecret = 'zwP2nf2XpHJvBrCx_xIFdvxm_7IDi9tlLKVxWpVqF44'

    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}

    )
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token = r.json()['access_token']
    print(token)
    """
    创建标签
    """
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        params={"access_token": token},
        json= {
            "group_name": "测试",
            "tag": [{"name": "Test1","order": 1},{"name": "Test","order": 2}]
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

def test_delete_tag():
    """
       获取access_token
       """
    corpid = 'ww9f9937b00575cb31'
    corpsecret = 'zwP2nf2XpHJvBrCx_xIFdvxm_7IDi9tlLKVxWpVqF44'

    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    token = r.json()['access_token']
    print(token)

    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
        params={"access_token": token},
        json={
            "tag_id":["etZr3CEAAAXv8XcwTllO3gP1sG05h5dw","etZr3CEAAAXv8XcwTllO3gP1sG05h5dw"]
        }
    )
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
