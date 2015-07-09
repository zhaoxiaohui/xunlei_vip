#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #
from common import Singleton

class Configure(Singleton):
    '''
    配置公共类，对于本程序，所有公共配置都硬编码进本类，不在用文件处理
    '''
    _VIP_URL = "www.521xunlei.com"
    
    def get_vip_url(self):
        return Configure._VIP_URL
    
    def get_time_type(self):
        return 0
    