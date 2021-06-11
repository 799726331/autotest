# -*- encoding: utf-8 -*-
'''
@File    :   data_001_transferRstQry.py
@Time    :   2020/12/16 10:42:10
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   单笔付款结果查询用例
'''

# here put the import lib

channel = "99999998"

class TransferRstQry_abc_Data():
    """
        100环境：
            支付平台建行测试
    """
    def __init__(self,test_host):
        if test_host == "135":
            self.custPyNo0 ="abC202012231649360044"
            self.custPyNo1 ="aBC2020122316014025"
            self.custPyNo2 ="abC202012231649360044"
        elif test_host == "100":
            self.custPyNo0 ="aBC20201228111407471"
            self.custPyNo1 ="aBC20201228111407312"
            self.custPyNo2 ="abC202012281520010000"

    def get_case(self):
        cases = [
            {
                "title":"000-查询支付成功，查询成功",
                "expection":"1",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":self.custPyNo0}}
            },
            {
                "title":"001-查询支付失败，查询成功",
                "expection":"2",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":self.custPyNo1}}
            },
            {
                "title":"002-查询含有未确认原因的支付单，查询成功",
                "expection":"1",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":self.custPyNo2}}
            },
            {
                "title":"003-custPyNo交易流水号为空，查询失败",
                "expection":"客户方交易流水号不能为空",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":""}}
            },
            {
                "title":"004-custPyNo交易流水号不存在，查询失败",
                "expection":"2",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":"345674343242654"}}
            },
            {
                "title":"005-custPyNo交易流水号存在于其他渠道，查询失败",
                "expection":"2",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":"Aplabc0001591003"}}
            },
            {
                "title":"006-custPyNo交易流水号超过65位，查询失败",
                "expection":"校验参数错误[客户订单号格式非法|]",
                "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20201107","reqTime":"152430","bankCode":"105","version":"1.0","remark":"单笔支付结果查询"},"custPyNo":"QW202012160916550030QW202012160916550030QW202012160916550030123456"}}
            },
        ]
        return cases

if __name__ == "__main__":
    print(TransferRstQry_abc_Data.cases[0]["case"])