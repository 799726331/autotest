import configparser
import os
config = configparser.ConfigParser()

# 配置文件路径
path = "f:/autotest/scripts1/config/config.ini"
config.read(path,encoding = "utf-8")

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

class FileDir():
    """获取文件路径配置"""
    # report_dir = config["report_dir"]["file_dir"]
    # case_dir = config["case_dir"]["file_dir"]
    report_dir = os.path.join(project_path,"report")
    case_dir = os.path.join(project_path,"cases")

class GetEmailInfo():
    """获取邮件信息"""
    from_addr = config["emailinfo"]["from_addr"]
    password = config["emailinfo"]["password"]
    to_addr = config["emailinfo"]["to_addr"]

class GetLogPath():
    """"获取日志路径"""
    # log_dir = config["log_dir"]["log_dir"]
    log_dir = os.path.join(project_path,"log")

class Get_Db():
    """获取数据库属性"""
    host_dir = config["db_dir"]["host"]
    port_dir = eval(config["db_dir"]["port"])
    user_dir = config["db_dir"]["user"]
    passwd_dir = config["db_dir"]["passwd"]



if __name__ == "__main__":
    print(FileDir().case_dir)
    print(GetLogPath.log_dir)
    print(project_path)
    # print(type(Get_Db.port_dir))
    # print(FileDir().report_dir)
    # print(type(GetEmailInfo().from_addr))
    # print(FileDir().report_dir)
    # print(type(GetEmailInfo().to_addr),str(GetEmailInfo.to_addr))
    # print(config.sections())
    # print(config.options("report_dir"))
