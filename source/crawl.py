#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #
from config import Configure
from util import Util



class Crawl(object):
    '''
    抓取提供VIP网站的网页，获取当天的用户名和密码列表
    请确保自己机器的时间同当前的日期时间相符（以后可能会更新为网络获取时间）
    '''
    def __init__(self):
        self.config = Configure()
    
    def _get_content(self, url):
        '''
        获取网页内容
        '''
        return None
    def _get_day_link(self):
        '''
        获取当天的分享链接
        '''
        cur_day = Util.get_time()
        return ["thread-6785-1-1.html", "thread-6787-1-1.html"]
    
    def _get_vips(self, url):
        '''
        获取某一页的所有VIP账号密码
        '''
        return [('hehe', 'f..k'), ('haha', 'm..m')]
        
    def all_come_to_bowl(self):
        '''
        vips come to my bowl quickly
        '''
        links = self._get_day_link()
        ret = []
        for link in links:
            cur_links = self._get_vips(self.config.get_vip_url() + "/" + link)
            ret.append(cur_links)
        return ret
        