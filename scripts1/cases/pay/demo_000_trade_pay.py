# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_pay.py
@Time    :   2020/11/23 09:51:07
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   支付平台-统一付款接口
'''

# here put the import lib

import os, sys

sys.path.append(os.getcwd().split("scripts1", 1)[0])

from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_demo_000_trade_pay import *


from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_pay.api


def data_list(test_host):
    """
    获取测试集
    :param test_host:
    :return: data
    """
    if test_host == "135":
        data = Trade_pay_135_data()
    elif test_host == "100":
        data = Trade_pay_100_data()
    return data


def test_000_trade_pay(test_host):
    """000-支付成功"""
    i = 0
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]

    resp = pay_req(test_host, api, case, "99999998")

    assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
    # assert expection == eval(resp.json()["rstCnt"])["rstSts"]


# def test_001_trade_pay(test_host):
#     """001-仅必填字段，支付成功"""
#     i = 1
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_002_trade_pay(test_host):
#     """002-客户订单号重复outTxNo，支付失败"""
#     i = 2
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_003_trade_pay(test_host):
#     """003-客户业务编号重复outBizNo(已支付成功)，支付失败"""
#     i = 3
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_004_trade_pay(test_host):
#     """004-客户业务编号重复outBizNo（支付失败），可支付成功"""
#     i = 4
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_005_trade_pay(test_host):
#     """005-客户订单号outTxNo，含有中文，支付失败"""
#     i = 5
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_006_trade_pay(test_host):
#     """006-客户订单号outTxNo，含有非指定特殊符号，支付失败"""
#     i = 6
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_007_trade_pay(test_host):
#     """007-金额校验txAmt，整数，支付成功"""
#     i = 7
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_008_trade_pay(test_host):
#     """008-金额校验txAmt，1位小数，支付成功"""
#     i = 8
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_009_trade_pay(test_host):
#     """009-金额校验txAmt，3位小数，支付失败"""
#     i = 9
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_010_trade_pay(test_host):
#     """010-金额校验txAmt，负数，支付失败"""
#     i = 10
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_011_trade_pay(test_host):
#     """011-金额校验txAmt，为空，支付失败"""
#     i = 11
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_012_trade_pay(test_host):
#     """012-金额校验txAmt，支付长度校验大于16位，支付失败"""
#     i = 12
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_013_trade_pay(test_host):
#     """013-支付场景payScene，非指定场景，支付失败"""
#     i = 13
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_014_trade_pay(test_host):
#     """014-支付场景payScene，为空，支付失败"""
#     i = 14
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_015_trade_pay(test_host):
#     """015-支付产品payProduct，非指定场景，支付失败"""
#     i = 15
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_016_trade_pay(test_host):
#     """016-支付产品payProduct，为空，支付失败"""
#     i = 16
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_017_trade_pay(test_host):
#     """017-支付产品payProduct，长度超过7位，支付失败"""
#     i = 17
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_018_trade_pay(test_host):
#     """018-支付场景payScene，长度超过7位，支付失败"""
#     i = 18
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_019_trade_pay(test_host):
#     """019-客户订单号outTxNo，为空，支付失败"""
#     i = 19
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_020_trade_pay(test_host):
#     """020-客户订单号outTxNo，长度为51，支付失败"""
#     i = 20
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_021_trade_pay(test_host):
#     """021-客户业务单据编号outBizNo，长度为51，支付失败"""
#     i = 21
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_022_trade_pay(test_host):
#     """022-客户业务单据编号outBizNo，为空，支付失败"""
#     i = 22
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_023_trade_pay(test_host):
#     """023-付款方账号，pyrAcctNo，为空，支付失败"""
#     i = 23
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_024_trade_pay(test_host):
#     """024-付款方账号，pyrAcctNo，长度为61，支付失败"""
#     i = 24
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_025_trade_pay(test_host):
#     """025-收款方开户行号，rcvDepBankNo，为空，支付失败"""
#     i = 25
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_026_trade_pay(test_host):
#     """026-收款方开户行号，rcvDepBankNo，长度为13，支付失败"""
#     i = 26
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_027_trade_pay(test_host):
#     """027-收款方行类别，rcvBankCgy，为空，支付失败"""
#     i = 27
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_028_trade_pay(test_host):
#     """028-收款方行类别，rcvBankCgy，长度为3，支付失败"""
#     i = 28
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_029_trade_pay(test_host):
#     """029-收款方行类别，rcvBankCgy，非默认值，支付失败"""
#     i = 29
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_030_trade_pay(test_host):
#     """030-收款方账号，rcvAcctNo，为空，支付失败"""
#     i = 30
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_031_trade_pay(test_host):
#     """031-收款方账号，rcvAcctNo，长度61位，支付失败"""
#     i = 31
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_032_trade_pay(test_host):
#     """032-收款方账户名称，rcvAcctName，为空，支付失败"""
#     i = 32
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_033_trade_pay(test_host):
#     """033-收款方账户名称，rcvAcctName，长度121，支付失败"""
#     i = 33
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_034_trade_pay(test_host):
#     """034-收款方账户类别，rcvAcctCgy，为空，支付失败"""
#     i = 34
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_035_trade_pay(test_host):
#     """035-收款方账户类别，rcvAcctCgy，长度3，支付失败"""
#     i = 35
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_036_trade_pay(test_host):
#     """036-收款方账户类别，rcvAcctCgy，非默认值，支付失败"""
#     i = 36
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_037_trade_pay(test_host):
#     """037-币种，currCode，为空，支付失败"""
#     i = 37
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_038_trade_pay(test_host):
#     """038-币种，currCode，4位，支付失败"""
#     i = 38
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_039_trade_pay(test_host):
#     """039-币种，currCode，非默认值，支付失败"""
#     i = 39
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_040_trade_pay(test_host):
#     """040-用途名称，useName，为空，支付失败"""
#     i = 40
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_041_trade_pay(test_host):
#     """041-用途名称，useName，长度501，支付失败"""
#     i = 41
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_042_trade_pay(test_host):
#     """042-渠道号不正确，支付失败"""
#     i = 42
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 500, "相应状态不正确{}".format(resp.status_code)
#     # assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#     assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())
#
#
# def test_043_trade_pay(test_host):
#     """043-路由method不正确，支付失败"""
#     i = 43
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     # assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#     assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())
#
#
# def test_044_trade_pay(test_host):
#     """044-字符集非utf-8，支付失败"""
#     i = 44
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     # assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#     assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())
#
#
# def test_045_trade_pay(test_host):
#     """045-请求时间格式非法，支付失败"""
#     i = 45
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())
#     # assert expection == eval(resp.json()["rstCnt"])["rstSts"]
#
#
# def test_046_trade_pay(test_host):
#     """046-版本号非1.0，支付失败"""
#     i = 46
#     cases_list = data_list(test_host)
#     case = cases_list.cases[i]["case"]
#     expection = cases_list.cases[i]["expection"]
#     resp = pay_req(test_host, api, case, "99999998")
#     assert resp.status_code == 200, "相应状态不正确{}".format(resp.status_code)
#     assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())
#
#
# if __name__ == "__main__":
#
#     import json
#     import traceback
#     import requests
#     import random
#
#     header = {'Content-Type': 'application/json', "Accept-Encoding": ""}
#     cases_list = Trade_pay_100_data()
#
#     for i in range(len(cases_list.cases)):
#         #print("测试序号：", i)
#         if i == 700:
#             print("跳过：", i)
#         elif i ==0 :
#             import time
#             time.sleep(1)
#             cases_list = Trade_pay_100_data()
#             title = cases_list.cases[i]["title"]
#             case = cases_list.cases[i]["case"]
#             resp = pay_req("100", api, case, "99999998")
#
#             try:
#                 print("==========================================================")
#                 print(case)
#                 print(resp.status_code)
#                 print(title, ":", resp.json())
#                 print("")
#                 if "不存在的方法名" in str(resp.json()):
#                     print(111111)
#                 with open("paytestresult.txt", "a+", encoding="utf-8")as f:
#                     f.write("统一支付接口" + title + ":" + "\n")
#                     f.write(json.dumps(resp.json(), ensure_ascii=False) + "\n")
#                     f.write("\n")
#             except Exception as f:
#                 print(traceback.print_exc())
#
