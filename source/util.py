#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

from config import Configure

import time
from __builtin__ import staticmethod

class Util(object):
    '''
    工具类，这么个破东西，整个还像个样子，doubi
    '''
    config = Configure()
    _m_days_o = [31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
    _m_days_n = [31, 29, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
    @staticmethod  
    def get_time():
        if Util.config.get_time_type() == 0:
            return Util._get_system_time()
        else:
            return Util._get_network_time()
        
    @staticmethod
    def get_day_before(cur_day):
        if len(cur_day) != 3:
            return cur_day
        day = int(cur_day[2])
        mon = int(cur_day[1])
        year = int(cur_day[0])
        new_day = cur_day[:]
        if day != 1:
            new_day[2] = str(day - 1)
            return new_day
        days = Util._get_days(cur_day)
        new_day = cur_day[:]
        if mon-1 != 0:
            new_day[1] = str(mon-1)
            new_day[2] = str(days[mon-1])
        else:
            new_day[0] = str(year-1)
            new_day[1] = '12'
            new_day[2] = '31'
        return new_day
        
    @staticmethod
    def _get_days(cur_day):
        if len(cur_day) != 3:
            return Util._m_days_o
        year = int(cur_day[0])
        if (year%4 == 0 and year%100 != 0 ) or year%400 == 0:
            return Util._m_days_n
        return Util._m_days_o
    @staticmethod  
    def _get_system_time():
        ltime = time.localtime()
        if ltime != None:
            return [str(ltime.tm_year),"%02d" % ltime.tm_mon, "%02d" % ltime.tm_mday]
        else:
            return None
    
    @staticmethod
    def _get_network_time():
        '''
        Currently we just use local time
        Otherwise we should specify an timezone
        '''
        return Util._get_system_time()
        