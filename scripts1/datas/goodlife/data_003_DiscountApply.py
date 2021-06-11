'''
@File    :   data_000_custInfoQuery.py
@Time    :   2021/1/11 22:07 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

import random
import time
import random
import datetime


bizCode = "YJES20200612001"
ownerIdType = "C"
ownerIdCode = "110105199003076670"
ownerName = "渤海一号科技有限公司"
sellerName = "渤海一号科技有限公司"
sellerCertType = "C"
sellerCertNo = "110105199003076670"
assetAmt = "2600"
finName = "渤海银行股份有限公司"
finCertNo = "911200007109339563"
sellerAcctNo = ""
debtorName = "优选好生活科技（珠海）有限公司"
debtorIdCode = "91440400MA4WMQXB44"
finCode = "CBHB"

dt = datetime.datetime.now()
out_date = (dt + datetime.timedelta(days=60)).strftime("%Y%m%d")

class goodlife_DiscountApply_23_data():
    cases = [
        {
            "title": "000-渤海融资申请推送成功,支付状态正确",
            "expection": "1",
            "expection2":"0",
            "expection3": "3",
            "expection4": "3",
            "case": {
    "channel":"00000009",
    "data":{"commonInput":{"version":"1.0.0","channel":"00000009","reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"remark":str(random.randint(1,50000))},"bizCode":bizCode,"asset":{"assetCode":str(random.randint(100,99999,)),"assetType":"1","ownerIdType":ownerIdType,"ownerIdCode":ownerIdCode,"ownerName":ownerName,"pmtType":"5","assetAmt":assetAmt,"acctPeriod":"60","debtorIdType":"C","debtorIdCode":debtorIdCode,"debtorName":debtorName,"contractNo":"bfd424411e3e4c7092c9c64a98c45501","contractName":"佣金e收产品服务协议","insPmtMode":"1","insAmtMax":"10.00","importor":"1","prodCode":"EBT01","bizId":str(random.randint(100,99999))},"discountInfo":{"dctCode":str(random.randint(100,99999)),"sellerName":sellerName,"sellerCertType":sellerCertType,"sellerCertNo":sellerCertNo,"sellerAcctNo":sellerAcctNo,"finCode":finCode,"finName":finName,"finCertType":"C","finCertNo":finCertNo,"dctAmt":assetAmt,"expDate":out_date,"dctDate":time.strftime("%Y%m%d"),"dctDays":"60","settMode":"1","remark":"融资测试","contNo":"contNo-003----测试融资协议编号"},"housings":[{"applyNo":"DL0111024","buildName":"嘉裕公馆","unitNo":"2号楼-1-101","preSaleSpace":"120","ownerName":"弟弟","contractPrice":"1000000.03","actSubDate":"20200324","subPassDate":"20200325","actSignDate":"20200326","signPassDate":"20200327","totalCommission":"20200.01","commission":"10008.02","settleNode":"回款","salesman":"销售1号","houseFiles":[{"hfileType":str(random.randint(26,28)),"hfileName":"001-0.pdf","hfileUrl":"https://kfcdn.lifeat.cn/%E4%BF%9D%E7%90%86%E5%8D%8F%E8%AE%AEHSHELMEMARK2020060500000001-0.pdf"}]}],"files":[{"fileType":"2","fileUrl":"/00000009/cont/测试发票.jpg","fileName":"测试发票.jpg","fileData":{"openType":"1","buyerName":debtorName,"custSignName":"1","invAmt":"10000000","invCode":str(random.randint(1000000000,9990000000)),"invContent":"1","invDate":"20200501","invNo":str(random.randint(30000000,99999000)),"isCheckSign":"1","sellerName":ownerName,"taxRate":"1","taxAmt":"1","invType":"01"}},{"fileType":"5","fileUrl":"/00000009/cont/融资合同（好生活）-"+finName+".pdf","fileName":"合作协议-"+debtorName+".pdf","fileData":{"acceptorName":ownerName,"isCheckSign":"1","contName":"1","signDate":"20190831","signOnline":"1","sponsorName":debtorName}},{"fileType":"6","fileUrl":"/00000009/cont/融资合同（好生活）-"+finName+".pdf","fileName":"渠道合作函/分销函-"+debtorName+".pdf","fileData":{"coopEndDate":"20200401","coopStartDate":"20200331","custSignName":debtorName,"isCheckSign":"1","projName":"2","receiverName":ownerName,"signOnline":"1","signPartyName":debtorName,"settInfos":[{"settNode":"1","settStd":"1","prodName":"1"}]}},{"fileType":"7","fileUrl":"/00000009/cont/融资合同（好生活）-"+finName+".pdf","fileName":"佣金确认单-"+debtorName+".pdf","fileData":{"contName":ownerName,"custSignName":debtorName,"isCheckSign":"1","subDate":"20200201","signOnline":"1"}},{"fileType":"8","fileUrl":"/00000009/cont/融资合同（好生活）-"+finName+".pdf","fileName":"付款审批表-"+debtorName+".pdf","fileData":{"buildName":"1","commNum":"1","commission":"1","dctAmt":"1","isCheckSign":"0","organName":"1","payee":ownerName,"payer":debtorName,"pmtType":"1","startDate":"20200401","unitNo":"1"}},{"fileType":"14","fileUrl":"/00000009/cont/付款承诺函（渤海银行版已盖章）.pdf","fileName":"付款承诺函（渤海银行版已盖章）.pdf"},{"fileType":"16","fileUrl":"/00000009/cont/国内反向保理业务融资申请书(已盖章).pdf","fileName":"国内反向保理业务融资申请书(已盖章).pdf"},{"fileType":"17","fileUrl":"/00000009/cont/债权转让通知书(已盖章).pdf","fileName":"债权转让通知书(已盖章).pdf"},{"fileType":"18","fileUrl":"/00000009/cont/壹链盟平台e单开具协议(已盖章).pdf","fileName":"壹链盟平台e单开具协议(已盖章).pdf"}]}
}
        }
    ]

if __name__ == '__main__':
    import json
    a = goodlife_DiscountApply_23_data().cases[0]["case"]
    b = json.dumps(a)
    print(b)