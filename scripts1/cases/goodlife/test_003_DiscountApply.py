'''
@File    :   test_000_custInfoQuery.py
@Time    :   2021/1/11 22:04 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''
import sys,os
sys.path.append(os.getcwd().split("scripts1", 1)[0])
# 改
from scripts1.apis.goodlife import goodlife_api
from scripts1.datas.goodlife.data_003_DiscountApply import *
from scripts1.model.goodlife.goodlife_req import goodlife_req
import pytest_rerunfailures,pytest
from scripts1.utils.db import *

# 改
api = goodlife_api.DiscountApply_Api.api
def data_list(test_host):
    """
    获取测试集
    :param test_host:
    :return: data
    """
    # 改
    try:
        if test_host == "dev2":
            data = goodlife_DiscountApply_23_data()
        elif test_host == "23":
            data = goodlife_DiscountApply_23_data()
        elif test_host == "135":
            data = goodlife_DiscountApply_23_data()
        else:
            print("请输入正确的环境编号")
        return data
    except Exception as f:
        print(f)

# @pytest.mark.flaky(reruns = 3)
# 改
def test_003_DiscountApply(test_host):
    i = 0
    host = "sit"
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    expection2 = cases_list.cases[i]["expection2"]
    expection3 = cases_list.cases[i]["expection3"]
    expection4 = cases_list.cases[i]["expection4"]
    resp = goodlife_req(test_host,api,case)
    assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
    # assert expection ==
    try:
        dctId = resp.json()["data"]["dctId"]
        print(dctId)
        # time.sleep(10)
        # print(dctId)
        # print(db_select_002(dctId))
        # print(expection2)
        assert expection == db_select_001(host,dctId)
        assert expection2 == db_select_002(host,dctId)
        assert expection3 == db_select_003(host,dctId)
        assert expection4 == db_select_004(host,dctId)
    except Exception as f:
        print("错误提示:",resp.json())
# @pytest.mark.flaky(reruns = 3)
# def test_001_custInfoQuery(test_host):
#     i = 1
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = goodlife_req(test_host,api,case)
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == resp.json()["rspCode"]


if __name__ == '__main__':
    test_003_DiscountApply("23")
