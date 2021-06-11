'''
@File    :   data_001_prodApply.py
@Time    :   2021/1/13 20:58 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

import time
import random

bankDot = "314136600212"
bizCode = "YJES20200612001"
# channel = "00000009"


custTag = "SELLER_COMPANY"
applyId = "bb1073b56b6b49d63a513316y0" + str(random.randint(11111,99999))
certNo = "12010119900307" + str (random.randint(1111,9999))
custName = "经常打包的人" + str(random.randint(1111,9999))
acctNo = "36010219900399" + str(random.randint(1111,9999))
loginName = "卢梓轩" + str(random.randint(111,2000))


class goodlife_prodApply_135_data():
    cases = [
        {
            "title":"000-开通产品成功",
            "expection":"2",
            "case":{"channel":"00000009","data":{"commonInput":{"version":"1.0.0","channel":"00000009","reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"remark":"hhh"},"applyId":applyId,"prodCode":"EBT01","callbackUrl":"","userId":"","custId":"","msg":"","bizCode":bizCode,"channel":channel,"accreditationFalg":True,"updateUserFlag":True,"checkFlag":True,"custBase":{"addrArea":"白云区","addrCity":"广州市","addrProv":"广东省","address":"京溪办公广场1号","certNo":certNo,"certType":"C","certExp":"99991231","corpCertExp":"20251008","corpCertNo":"110101199003076771","corpName":"陈嘉欣","corpTel":"18515514512","ctrlName":"册35","ctrlCertType":"1","ctrlCertNo":"110101199003078857","ctrlCertExp":"20500817","custInd":"1451","custName":custName,"bizScope":"测试经营范围","regCap":"5000000.00","custScale":"04","custType":"1","custTag":custTag},"custRel":{"relCustCode":"","relType":""},"custAcct":{"acctName":custName,"acctNo":acctNo,"bankDot":bankDot},"user":{"certNo":"430621199802134444","certNoExp":"99991231","certType":"1","loginName":loginName,"userName":"测试83","userTel":"13129080384"},"files":[{"fileCode":"bizLic","fileName":"营业执照.jpg","fileUrl":"/00000009/prod/营业执照.jpg"},{"fileCode":"corpCertFront","fileName":"法人身份证正面.jpg","fileUrl":"/00000009/prod/法人身份证正面.jpg"},{"fileCode":"corpCertBack","fileName":"法人身份证反面.jpg","fileUrl":"/00000009/prod/法人身份证反面.jpg"},{"fileCode":"acctOpenCert","fileName":"银行账户证明照.jpg","fileUrl":"/00000009/prod/银行账户证明照.jpg"},{"fileCode":"userLivePhoto","fileName":"管理员现场照.jpg","fileUrl":"/00000009/prod/管理员现场照.jpg"},{"fileCode":"userCertFront","fileName":"管理员身份证正面.jpg","fileUrl":"/00000009/prod/管理员身份证正面.jpg"},{"fileCode":"userCertBack","fileName":"管理员身份证反面.jpg","fileUrl":"/00000009/prod/管理员身份证反面.jpg"},{"fileCode":"custAuth","fileName":"授权委托书.jpg","fileUrl":"/00000009/prod/授权委托书.jpg"}]}}
        }
    ]

if __name__ == '__main__':
    import json
    # print(json.dumps(goodlife_prodApply_135_data().cases[0]["case"]))
    # print(type(acctNo))
    # print(time.strftime("%Y-%m-%d-%H-%M-%S"))