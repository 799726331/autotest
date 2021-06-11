# -*- encoding: utf-8 -*-
'''
@File    :   query_asset.py
@Time    :   2020/09/04 16:21:54
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   None 
'''

# here put the import lib
import sys,os
sys.path.append(os.getcwd().split("scripts1",1)[0])

import requests

from scripts1.apis.elimen.commonapi import (
    QuerySscreenedAsset,ChangeEnt,
    Login
    )
from scripts1.datas.elimen.login import Cases

name = "yjj"
pwd = "OaBIVZUuzPQKGE02ujonS4x7viidbVWwsqTWBVu2QVqObiqjLsc0uegyl7vR6CfdxQBNVHpVTEr5N+M29mc0nStmfl543+rZOhrfD4IY699t+mmIkyHI0q+kAceLhivA6So/cQhPhVRuOP52vzrd1RnOM3Fc+5bLM6omNYu2PGQ="

host = "http://10.132.4.99:9050"



def login(name, pwd):
    method = Login.method
    api = host + Login.api
    payload = {"username":name,"password":pwd,"rememberMe":"TRUE","kaptchaReceived":"!@#$","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"}
    header =  {
        "Referer": "http://10.132.4.99:9050/",
        "Content-Type": "application/x-www-form-urlencoded",
        }
    resp = requests.request(method,api,headers=header,data=payload)
    cookie = requests.utils.dict_from_cookiejar(resp.cookies)
    for key,value in cookie.items():
        cookie = "{}={}".format(key,value)
    return resp, cookie

class TestCases():

    @classmethod
    def setup_class(cls):
        # 在当前测试类的开始前，执行一次
        cls.resp, cls.cookie = login(name,pwd)
        print("test start")
    
    @classmethod
    def teardown_class(cls):
        # 在当前测试类全部执行完后，执行一次
        print("test end")

    def setup_method(self):
        # 在每一个测试方法执行前，执行一遍
        print("用例开始")

    def teardown_method(self):
        # 在每一个测试方法执行完后，执行一遍
        print("用例结束")

    
    def test_001(self):
        """应付资产查询"""
        params = dict(
            pageSize="10",
            pageNo="1",
            assetCode="",
            assetCodeEs="",
            assetCusName="",
            ownerName="",
            fcstAmtBegin="",
            fcstAmtEnd="",
            assetState="",
            sendFlag="",
            sortName="",
            sortType=""
        )
        api = host + QuerySscreenedAsset.api
        method = QuerySscreenedAsset.method
        header = {
            "Referer":"http://10.132.4.99:9050/ebill/",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":self.cookie
            }
            
        resp = requests.request(method,api,data=params,headers=header)
        assert resp.json()["total"] == 168,"断言失败！实际返回：{}".format(resp.json())

    def test_002(self):
        """切换企业"""
        params = dict(
            entId="1cd0d2dd91544f24a28e78be30fac42a",
            client="frontend",
            grant_type="password",
            appCode="GOVERNOR"
        )
        api = host + ChangeEnt.api
        method = ChangeEnt.method
        header = {
            "Referer":"http://10.132.4.99:9050/ebill/",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":self.cookie
            }
            
        resp = requests.request(method,api,data=params,headers=header)
        assert resp.json()["msg"] == "企业切换成功！"
        


if __name__ == "__main__":
    resp, cookie = login(name, pwd)
    
    def test_001():
        params = dict(
            pageSize="10",
            pageNo="1",
            assetCode="",
            assetCodeEs="",
            assetCusName="",
            ownerName="",
            fcstAmtBegin="",
            fcstAmtEnd="",
            assetState="",
            sendFlag="",
            sortName="",
            sortType=""
        )
        api = host + QuerySscreenedAsset.api
        method = QuerySscreenedAsset.method
        header = {
            "Referer":"http://10.132.4.99:9050/ebill/",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":cookie
            }
            
        resp = requests.request(method,api,data=params,headers=header)
        print(resp.json())
    
    test_001()
