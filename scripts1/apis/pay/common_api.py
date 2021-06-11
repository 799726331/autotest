# -*- encoding: utf-8 -*-
'''
@File    :   common_api.py
@Time    :   2020/11/19 16:16:03
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   大支付平台公共接口
'''

# here put the import lib

class ReqEncrySign_V2():
    """加密接口"""
    api = "/plumber/cxf/mockit/reqEncrySign_V2"
    method = "post"

class RspDecry_V2():
    """解密接口"""
    def __init__(self,channel):
        self.channel = channel
        self.row_api = "/plumber/cxf/mockit/rspDecry_V2?channel="
        self.api = self.row_api + self.channel
        self.method = "post"

if __name__ == "__main__":
    print(RspDecry_V2("00000010").api)
