#
# Window Edited by Pycharm.
# Time : 2022/08/29
# Author : YU.J.P
#

"""
    版本: V1.2
    基本功能:
        1. 简洁的窗体；
        2. 新增按钮 以及相应提示
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
from tkinter import messagebox  # 消息窗口
from mutagen.mp3 import MP3  # 获取mp3总时长


# 全局变量
VERSION = 'Window V1.2'  # 版本信息


# 主要逻辑运行
class MainRun:
    # 固定变量
    window_0 = None  # 窗口 编号:0
    window_0_width = 500  # 窗口宽度
    window_0_height = 300  # 窗口宽度
    button_0 = None  # 按钮 编号:0 确认
    button_1 = None  # 按钮 编号:11 返回

    def __init__(self):
        pass

    # 窗口初始化
    def initALLWindow(self):
        # 窗口 编号:0 初始化
        MainRun.window_0 = tkinter.Tk()  # 创建窗口
        MainRun.window_0.title(VERSION)  # 窗口命名
        MainRun.window_0.geometry(str(MainRun.window_0_width) + 'x' +
            str(MainRun.window_0_height) + '+500+200')  # 设置窗口大小 -- 格式 : '长x宽+x+y'

    # 按钮初始化
    def initAllButton(self):
        # 按钮 编号:0 初始化
        MainRun.button_0 = tkinter.Button(MainRun.window_0)  # 放到 window_0 上
        MainRun.button_0['text'] = '>>'  # 按钮命名
        # MainRun.button_0.grid(column=0, row=1, columnspan=1, rowspan=1, ipadx=10, ipady=5)  # 按钮定位 列号 行号
        MainRun.button_0.place(x= MainRun.window_0_width - 50, y=0, width=50, height=25)
        MainRun.button_0.bind("<Button-1>", self.jumpMassage_0)
        # 按钮 编号:1 初始化
        MainRun.button_1 = tkinter.Button(MainRun.window_0)  # 放到 window_0 上
        MainRun.button_1['text'] = '<<'  # 按钮命名
        # MainRun.button_1.grid(column=1, row=3, columnspan=1, rowspan=1, ipadx=10, ipady=5)  # 按钮定位 列号 行号
        MainRun.button_1.place(x=0, y=0, width=50, height=25)
        MainRun.button_1.bind("<Button-1>", self.jumpMassage_1)

    # 按钮 编号:0 确认 消息弹窗
    def jumpMassage_0(self, e):
        tkinter.messagebox.showinfo('提示', '确认成功!(◕ᴗ◕✿)')  # 窗口名称 点击成功

    # 按钮 编号:1 确认 消息弹窗
    def jumpMassage_1(self, e):
        tkinter.messagebox.showinfo('提示', '返回成功!(◕ᴗ◕✿)')  # 窗口名称 点击成功

    # 主程序入口
    def Start(self):
        # 窗口初始化
        self.initALLWindow()
        # 按钮初始化
        self.initAllButton()

        # 循环显示窗口
        MainRun.window_0.mainloop()


# 开始运行
if __name__ == '__main__':
    MainRun().Start()  # 运行
