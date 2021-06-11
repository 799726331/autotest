'''
@File    :   test_000_custInfoQuery.py
@Time    :   2021/1/11 22:04 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''
import sys,os
sys.path.append(os.getcwd().split("scripts1", 1)[0])
from scripts1.apis.goodlife import goodlife_api
from scripts1.datas.goodlife.data_000_custInfoQuery import *
from scripts1.model.goodlife.goodlife_req import goodlife_req
import pytest_rerunfailures,pytest

api = goodlife_api.CustInfoQuery_Api.api
def data_list(test_host):
    """
    获取测试集
    :param test_host:
    :return: data
    """
    if test_host == "23":
        data = goodlife_custInfoQuery_23_data()
    elif test_host == "100":
        data = goodlife_custInfoQuery_23_data()
    return data

@pytest.mark.flaky(reruns = 3)
def test_000_custInfoQuery(test_host):
    i = 0
    # 区分环境
    cases_list = data_list(test_host)
    # 获取测试用例和预期结果
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    # 请求对应的接口
    resp = goodlife_req(test_host,api,case)
    # 断言结果
    assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
    assert expection == resp.json()["rspCode"]

@pytest.mark.flaky(reruns = 3)
def test_001_custInfoQuery(test_host):
    i = 1
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = goodlife_req(test_host,api,case)
    assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
    assert expection == resp.json()["rspCode"]


if __name__ == '__main__':
    print(test_000_custInfoQuery("23"))