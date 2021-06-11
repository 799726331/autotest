'''
@File    :   goodlife_api.py
@Time    :   2021/1/11 17:42 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

class ProdApply_Api():
    '''产品开通接口'''
    api = "/plumber/cxf/chnel/v1/prod/prodApply"
    method = "post"

class ProdApplyResult_Api():
    '''产品开通结果查询接口'''
    api = "/plumber/cxf/chnel/v1/prod/prodApplyResult"
    method = "post"

class AcctInfoQuery_Api():
    '''账户查询'''
    api = "/plumber/cxf/user/v1/acct/acctInfoQuery"
    method = "post"

class AcctSign_Api():
    '''账户签约接口'''
    api = "/plumber/cxf/user/v1/acct/acctSign"
    method = "post"

class CustInfoQuery_Api():
    """客户查询接口"""
    api = "/plumber/cxf/chnel/v1/customer/custInfoQuery"
    method = "post"

class ContQuery_Api():
    '''合同查询接口'''
    api = "/plumber/cxf/chnel/v1/contract/contQuery"
    method = "post"

class ContCheckCodeGet_Api():
    '''合同签章验证码获取接口'''
    api = "/plumber/cxf/chnel/v1/contract/contCheckCodeGet"
    method = "post"

class ContSign_Api():
    '''合同签章接口'''
    api = "/plumber/cxf/chnel/v1/contract/contSign"
    method = "post"

class PdfSeal_Api():
    '''合同文件签章'''
    api = "/plumber/cxf/chnel/v1/contract/pdfSeal"
    method = "post"

class UserLogin_Api():
    '''用户单点登录'''
    api = "/plumber/cxf/chnel/v1/user/userLogin"
    method = "post"

class ProdQuotarResult_Api():
    '''额度查询接口'''
    api = "/plumber/cxf/chnel/v1/prod/prodQuotarResult"
    method = "post"

class ProdRateResult_Api():
    '''利率查询接口'''
    api = "/plumber/cxf/chnel/v1/prod/prodRateResult"
    method = "post"

class DiscountApply_Api():
    '''融资申请口'''
    api = "/plumber/cxf/chnel/v1/dct/discountApply"
    method = "post"

class RpmtQuery_Api():
    '''还款查询接口'''
    api = "/plumber/cxf/chnel/v1/user/rpmtQuery"
    method = "post"

class CustInfoModify_Api():
    '''客户信息变更接口'''
    api = "/plumber/cxf/chnel/v1/customer/custInfoModify"
    method = "post"

class DiscountApplyResult_Api():
    '''融资结果查询'''
    api = "/plumber/cxf/chnel/v1/dct/discountApplyResult"
    method = "post"

