# -*- encoding: utf-8 -*-
"""
@File    :   test_login.py
@Time    :   2020/09/04 14:36:02
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   登录测试
"""

# here put the import lib
import sys,os
sys.path.append(os.getcwd().split("scripts1",1)[0])
import requests

from scripts1.apis.elimen.commonapi import Login
from scripts1.datas.elimen.login import Cases
from scripts1.utils.host import HOST
from scripts1.utils.log import GetLog
import traceback

log = GetLog.elimen_Log

# 功能
def login(payload):
    '''登录功能'''
    try:
        method = Login.method
        api = HOST["135"] + Login.api
        header =  {
            "Referer": "http://10.132.4.99:9050/",
            "Content-Type": "application/x-www-form-urlencoded",
            }
        log.logger.info("{}:{}".format("请求参数",payload))
        resp = requests.request(method,api,headers=header,data=payload)
        # 获取cookie值
        cookie = requests.utils.dict_from_cookiejar(resp.cookies)
        for key,value in cookie.items():
            cookie = "{}={}".format(key,value)
        log.logger.info("{}:{}".format("返回报文",resp.json()))
        return resp, cookie
    except Exception as r:
        log.logger.debug("{}:{}".format("请求参数",payload))
        log.logger.error(traceback.format_exc())



# 用例
def test_000_login():
    """用户登录成功"""
    case = Cases.case[0]
    payload = case["payload"]
    resp, cookie = login(payload)
    assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
    assert resp.json()["msg"] == case["expect"], "断言失败！当前返回：{}".format(resp.json())

def test_001_login():
    """验证码为空"""
    case = Cases.case[1]
    payload = case["payload"]
    resp,cookie = login(payload)
    assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
    assert resp.json()["msg"] == case["expect"], "断言失败！当前返回：{}".format(resp.json())

def test_002_loign():
    """用户名为空"""
    case = Cases.case[2]
    payload = case["payload"]
    resp,cookie = login(payload)
    assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
    assert resp.json()["msg"] == case["expect"], "断言失败！当前返回：{}".format(resp.json())

def test_003_login():
    """密码为空"""
    case = Cases.case[3]
    payload = case["payload"]
    resp,cookie = login(payload)
    assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
    assert resp.json()["msg"] == case["expect"], "断言失败！当前返回：{}".format(resp.json())

def test_004_login():
    """密码错误"""
    case = Cases.case[4]
    payload = case["payload"]
    resp,cookie = login(payload)
    assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
    assert resp.json()["msg"] == case["expect"], "断言失败！用例：{},当前返回：{}".format(case["title"],resp.json())



if __name__ == "__main__":
    pass
