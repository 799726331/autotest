1. 项目说明
    -- scripts
        |-- apis ========       接口文档
        |    -- bank ====           子项目
        |    ....
        |-- cases =======       测试用例
        |-- datas =======       测试用例数据
        |-- log =========       日志
        |-- model =======       公共请求类
        |-- report ======       报告
        |-- utils =======       工具类
        |-- run.py ======       运行入口
        |-- readme ======       说明

2. 项目运行命令
    运行run.py文件，执行用例
        python run.py [项目名]/[用例文件名称] [测试报告名称] [环境代码] [是否发送邮件]
            环境代码: 135、100
            是否发送邮件：YES/NO

        1. 执行指定项目指定用例
            python run.py [项目名]/[用例文件名称] [测试报告名称] [环境代码] [是否发送邮件]
        2. 执行指定项目中全部用例
            python run.py [项目名] [测试报告名称] [环境代码] [是否发送邮件]
            e.g: 
                    1. 执行指定用例
                        python run.py elimen/test_login.py rport.html 135 YES/NO
                    2. 执行指定项目中全部用例
                        python run.py elimen rport.html 135 YES/NO

3. 第三方包
    pytest==6.0.1

    pytest-html==2.1.1

    requests==2.24.0


4. 配置文件config
    report_dir： 测试报告文件存放路径
    case_dir：   测试用例文件存放路径
    emailinfo：   邮件地址
    log_dir:     日志文件保存路径
    Db_dir:      数据库的基础配置参数


5. 命名规则
    5.1 接口文件：
        公共接口文件：common_api.py -------- 统一存放公共接口，例如加密接口、解密接口
        业务接口文件：xxx_api.py ------------[项目名称]_api.py
            接口类：class xxxx_Api():------ class [接口名称]_Api():  # XXX, 首字母大写

    5.2 用例文件：
        文件：test_000_xxxx.py ------ test_[序号]_[接口名称].py
            函数：def test_000_xxx() ------ def test_[序号]_[接口名称]()
    
    5.3 用例数据文件
        文件：data_000_xxxx.py ------ data_[序号]_[接口名称].py
            类：
            class Transfer_135_Data(): ------------------------------- [接口名称]_[环境代码]_Data.py
                cases = [
                    {
                        "title":"000-正常用例", ------------------- 用例序号及用例标题
                        "case":{"payload1":"","payload2":""},----- json参数
                        "expection":"交易成功" -------------------- 预期
                    }]

    5.4 公共请求方法文件（model）
        xxxx_req.py ------ [项目名称]_req.py
    

6. 工具类
    config.py ------ 获取配置参数及配置调用
    host.py ------ 设置host集合
    log.py ------ 设置log
    send_email.py ------ 设置邮件
    


注意事项:
1、需要在api文件夹里添加新业务的接口配置
2、在cases文件夹里新增新业务的测试用例集,文件名为test_xxx.py,类名Test_xxx,方法名为test_xxx
3、需要在datas里新增新项目相对应的测试入参请求报文json串
4、在log文件夹里面新增一个项目文件夹,用于存放所生成的日志
5、需要在model新增一个新业务的请求方法,用于进行业务的报文请求
6、在report文件夹里新增一个新业务的文件夹,用于存放测试报告
7、需要在util文件里log.py添加一个日志的方法
