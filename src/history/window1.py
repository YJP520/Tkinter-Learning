#
# Window Edited by Pycharm.
# Time : 2022/08/28
# Author : YU.J.P
#

"""
    版本: V1.0
    基本功能:
        1. 简洁的窗体；
    更新内容 :
        -
    需求：
        - 设计窗体

"""
import copy  # 拷贝函数
import os  # 文件输入
import random  # 随机包
import threading  # 多线程操作
import pygame  # 游戏引擎
import tkinter # 窗口视窗
from mutagen.mp3 import MP3  # 获取mp3总时长


# 全局变量
VERSION = 'V1.0'  # 版本信息


# 主要逻辑运行
class MainRun:
    # 固定变量
    window_0 = None  # 第一窗口

    def __init__(self):
        pass

    # 主程序入口
    def Start(self):
        # 创建一个窗口程序
        MainRun.window_0 = tkinter.Tk()
        # 窗口命名
        MainRun.window_0.title('Window ' + VERSION)
        # 设置窗口大小
        MainRun.window_0.geometry('500x300+500+200')  # '长x宽+x+y'

        # 循环显示窗口
        MainRun.window_0.mainloop()


# 开始运行
if __name__ == '__main__':
    MainRun().Start()  # 运行
