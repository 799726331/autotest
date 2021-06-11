

class Login():
    """登录接口"""
    api = "/gateway/login"
    method = "post"
    
class ChangeEnt():
    """切换企业"""
    api = "/gateway/auth/change-ent"
    method = "post"
    
class QuerySscreenedAsset():
    """应付资产管理查询"""
    api = "/gateway/zuul/assetor/biz/query/asset-query/query-screened-asset-for-fin-by-page"
    method = "post"
    