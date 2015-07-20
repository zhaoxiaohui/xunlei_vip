#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

from common import Singleton

class Configure(Singleton):
    '''
    配置公共类，对于本程序，所有公共配置都硬编码进本类，不在用文件处理
    '''
    _VIP_URL = "http://www.521xunlei.com"
    _VIP_TITLE = u'爱密码迅雷号'
    _VIP_PASS = u'首发密码'
    
    def get_vip_url(self):
        return Configure._VIP_URL
    
    def get_vip_tile_target(self):
        return Configure._VIP_TITLE
    
    def get_vip_pass_target(self):
        return Configure._VIP_PASS
    
    def get_time_type(self):
        return 0
    