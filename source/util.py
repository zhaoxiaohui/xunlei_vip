#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #

from config import Configure

class Util(object):
    '''
    工具类，这么个破东西，整个还像个样子，doubi
    '''
    config = Configure()
    @staticmethod  
    def get_time():
        if Util.config.get_time_type() == 0:
            return Util._get_system_time()
        else:
            return Util._get_network_time()
    @staticmethod  
    def _get_system_time():
        return (7, 9)
    
    @classmethod
    def _get_network_time():
        return (7, 9)