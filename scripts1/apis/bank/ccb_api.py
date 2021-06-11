
# -*- encoding: utf-8 -*-
'''
@File    :   ccb_api.py
@Time    :   2020/09/11 11:14:54
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   CCB api接口目录
'''

# here put the import lib


class Transfer_Api():
    """人民币单笔付款"""
    api = "/plumberpay/cxf/chnel/v1/payment/transfer"
    method = "post"

class TransferRstQry_Api():
    """单笔付款结果查询"""
    method = "post"
    api = "/plumberpay/cxf/chnel/v1/payment/transferRstQry"

# 第一期
class ObtainPubKey_Api():
    """渠道与壹链盟密钥交换接口"""
    api = "/plumberpay/cxf/chnel/v1/payment/keyTransfer/obtainPubKey"
    method = "POST"

# 第一期
class TransferRstUpd_Api():
    """单笔付款结果修改"""
    api = "/plumberpay/cxf/chnel/v1/payment/transferRstUpd"
    method = "post"

# 第一期
class BatchTransfer_Api():
    """人民币批量付款"""
    api = "/plumberpay/cxf/chnel/v1/payment/batchTransfer"
    method = "post"

# 第一期
class BatchTransferRstQry_Api():
    """付款结果批量查询"""
    api = "/plumberpay/cxf/chnel/v1/payment/batchTransferRstQry"
    method = "post"

# 第一期
class RcvdTransferRsts_Api():
    """已接收结果返回"""
    api = "/plumberpay/cxf/chnel/v1/payment/rcvdTransferRsts"
    method = "post"


