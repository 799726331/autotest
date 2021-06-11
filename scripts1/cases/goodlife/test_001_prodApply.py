'''
@File    :   test_001_prodApply.py
@Time    :   2021/1/13 21:44 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

import sys,os
sys.path.append(os.getcwd().split("scripts1", 1)[0])
from scripts1.apis.goodlife import goodlife_api
from scripts1.datas.goodlife.data_001_prodApply import *
from scripts1.model.goodlife.goodlife_req import goodlife_req

api = goodlife_api.ProdApply_Api.api
def data_list(test_host):
    """
    获取测试集
    :param test_host:
    :return: data
    """
    if test_host == "135":
        data = goodlife_prodApply_135_data
    elif test_host == "100":                                                                                                                          
        data = goodlife_prodApply_135_data
    return data

def test_000_custInfoQuery(test_host):
    i = 0
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = goodlife_req(test_host,api,case)
    assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
    assert expection == resp.json()["data"]["openSts"]                                                                                                                                                        