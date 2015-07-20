#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #
from crawl import Crawl

def run():
    crawler = Crawl()
    vips = crawler.all_come_to_bowl()
    print_vips(vips)

def print_vips(vips):
    for vip in vips:
        print "用户名：%s\t密码：%s" % (vip[0], vip[1])
        
if __name__=="__main__":
    run()