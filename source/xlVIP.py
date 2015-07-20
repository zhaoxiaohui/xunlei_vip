#coding:gb2312
# ********************************** #
#          本程序仅供娱乐                                                            #
#          勿作商业用途                                                                #
#    对使用本程序造成的任何损失，本人概不负责                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

###########################################
# 本来想做图形化的，感觉真的是没有必要（运行终端模式的直接复制吧#
# 以后有精力在改进，或者直接点击登陆时弹出更好                                        #
###########################################
from crawl import Crawl
import ctypes
import sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_BLUE = 0x09 # blue.

def run():
    crawler = Crawl()
    vips = crawler.all_come_to_bowl()
    print_vips(vips)

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()

#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
    
def printColor(mess, type):
    if type == 0:
        printDarkWhite(mess)
    else:
        printGreen(mess)
        
def print_vips(vips):
    cid = 0
    for vip in vips:
        printColor("%s\t\t%s\n" % (vip[0], vip[1]), cid)
        cid = ~cid
        
if __name__=="__main__":
    run()