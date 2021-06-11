# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2020/10/28 17:06:27
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   定时清理过期log文件
'''

# here put the import lib


import glob,os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.utils.config import GetLogPath

path = []
# 添加log项目名称
log_pro_name = ["bank","common","ecome","elimen","revfactor","pay","goodlife"]
for i in log_pro_name:
    path.append(GetLogPath.log_dir + i + "/*.log") 

def del_log_file(num):
    """删除过期日志，日志备份数量"""
    for filename in path :
        path_file_number = glob.glob(filename)    # 获取指定路径下文件集合
        name = filename.split("/")[4]
        
        if len(path_file_number)>num:
            os.remove(path_file_number[0])  # 删除指定文件
            print("{}:已成功删除：{}".format(name,path_file_number[0]))
        else:
            print("{}:历史log文件无需删除".format(name))
        


if __name__ == "__main__":
    del_log_file(1)
    print(path)
    


