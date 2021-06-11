# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2020/10/15 14:34:34
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   pytest框架使用demo
'''

# here put the import lib


# 引入模块
import requests
import pytest

# 待测功能
def add(a,b):
    return a + b

def test_001_add():
    """异常用例"""
    c= add(1,3)
    # 断言
    assert c == 5, "c结果不满足"

def test_002_add():
    """正常用例"""
    c= add(1,3)
    # 断言
    assert c == 4, "c结果不满足"

def test_000_login():
    """用户登录正常用例"""
    api = "http://sit2.elimen.com.cn:5515/gateway/login"
    username = "jiulong"
    password = "OaBIVZUuzPQKGE02ujonS4x7viidbVWwsqTWBVu2QVqObiqjLsc0uegyl7vR6CfdxQBNVHpVTEr5N+M29mc0nStmfl543+rZOhrfD4IY699t+mmIkyHI0q+kAceLhivA6So/cQhPhVRuOP52vzrd1RnOM3Fc+5bLM6omNYu2PGQ="
    data = {'username': username,'password': password,'rememberMe': True,'kaptchaReceived':'!@#$','client': 'frontend',
            'grant_type': 'password',
            'appCode': 'GOVERNOR',
            'qrcodeLogin': False,
            'loginUUid':'',
            'uuid': '',
            'certNo': '',
            'loginMethod': 'pwd',
            "loginEnd":"portal"
        }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        }
    resp = requests.post(api,data=data,headers=header)
    result_msg = resp.json()["msg"]

    # 断言
    # 方法一：断言响应码
    assert resp.status_code == 200, "登录失败"
    # 方法二：断言响应
    assert result_msg == "登录成功！", "登录失败"
    

if __name__ == "__main__":
    '''
    test_cases = []
    for i in range(len(Cases.case)):
        test_cases.append((Cases.case[i]["payload"],Cases.case[i]["expect"]))

    @pytest.mark.parametrize("payload,expect_result",test_cases)
    def test_login(payload,expect_result):
        """登录"""
        method = Login.method
        api = host + Login.api
        header =  {
            "Referer": "http://10.132.4.99:9050/",
            "Content-Type": "application/x-www-form-urlencoded",
            }
        resp = requests.request(method,api,headers=header,data=payload)
        
        assert resp.status_code == 200,"{}：登录响应状态码错误".format(resp.status_code)
        assert resp.json()["msg"] == expect_result, "断言失败！当前返回：{}".format(resp.json())
    '''
    pass
    