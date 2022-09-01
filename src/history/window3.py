#
# Window Edited by Pycharm.
# Time : 2022/08/30
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

import tkinter # 窗口视窗
from tkinter import messagebox  # 消息窗口
from tkinter import ttk  # 下拉选择框

import threading  # 多线程操作
import pygame  # 游戏引擎
from mutagen.mp3 import MP3  # 获取mp3总时长


# 全局变量
VERSION = 'Window V1.2'  # 版本信息


# 主要逻辑运行
class MainGUI:
    # 固定变量
    window_0 = None  # 窗口 编号:0
    window_0_width = 500  # 窗口宽度
    window_0_height = 300  # 窗口宽度
    button_0 = None  # 按钮 编号:0 确认
    button_1 = None  # 按钮 编号:1 返回
    label_0 = None  # 标签 编号:0 文本显示
    entry_0 = None  # 输入框 编号:0 --
    checkbutton_0 = None  # 复选按钮 编号:0 --
    radiobutton_0 = None  # 单选按钮 编号:0 --
    combobox_0 = None  # 下拉选择框 编号:0 --

    def __init__(self):
        # 窗口初始化
        self.initALLWindow()
        # 按钮初始化
        self.initAllButton()
        # 标签初始化
        self.initAllLable()
        # 输入框初始化
        self.initAllEntry()
        # 复选按钮初始化
        self.initAllCheckbutton()
        # 单选按钮初始化
        self.initAllRadiobutton()
        # 下拉框初始化
        self.initAllCombobox()

    # 窗口初始化
    def initALLWindow(self):
        # 窗口 编号:0 初始化
        MainGUI.window_0 = tkinter.Tk()  # 创建窗口
        MainGUI.window_0.title(VERSION)  # 窗口命名
        MainGUI.window_0.geometry(str(MainGUI.window_0_width) + 'x' +
            str(MainGUI.window_0_height) + '+500+200')  # 设置窗口大小 -- 格式 : '长x宽+x+y'

    # 按钮初始化
    def initAllButton(self):
        # 按钮 编号:0 初始化
        MainGUI.button_0 = tkinter.Button(MainGUI.window_0, background='azure', font=('dengxian', 16))  # 放到 window_0 上
        MainGUI.button_0['text'] = '→'  # 按钮命名
        # MainRun.button_0.grid(column=0, row=1, columnspan=1, rowspan=1, ipadx=10, ipady=5)  # 按钮定位 列号 行号
        MainGUI.button_0.place(x=MainGUI.window_0_width - 50, y=0, width=50, height=25)
        MainGUI.button_0.bind("<Button-1>", self.jumpMassage_0)
        # 按钮 编号:1 初始化
        MainGUI.button_1 = tkinter.Button(MainGUI.window_0, background='azure', font=('dengxian', 16))  # 放到 window_0 上
        MainGUI.button_1['text'] = '←'  # 按钮命名
        # MainRun.button_1.grid(column=1, row=3, columnspan=1, rowspan=1, ipadx=10, ipady=5)  # 按钮定位 列号 行号
        MainGUI.button_1.place(x=0, y=0, width=50, height=25)
        MainGUI.button_1.bind("<Button-1>", self.jumpMassage_1)

    # 文本显示
    def initAllLable(self):
        # 标签 编号:0 初始化
        MainGUI.label_0 = tkinter.Label(self.window_0, text='封茗囧菌( • ̀ω•́ )✧', font=('dengxian', 16), background='pink')
        MainGUI.label_0.place(x=100, y=50, width=300, height=50)

    # 输入框显示
    def initAllEntry(self):
        # 输入框 编号:0 --
        MainGUI.entry_0 = tkinter.Entry(self.window_0, font=('dengxian', 16), background='yellow')
        MainGUI.entry_0.place(x=100, y=100, width=300, height=50)

    # 复选按钮显示
    def initAllCheckbutton(self):
        MainGUI.checkbutton_0 = tkinter.Checkbutton(self.window_0,text='清新', background='lightGreen')
        MainGUI.checkbutton_0.place(x=200, y=150, width=50, height=25)

    # 单选按钮显示
    def initAllRadiobutton(self):
        # 输入框 编号:0 --
        MainGUI.radiobutton_0 = tkinter.Radiobutton(self.window_0,text='纯色', background='lightGreen')  # aqua
        MainGUI.radiobutton_0.place(x=100, y=150, width=50, height=25)

    # 下拉选择框显示
    def initAllCombobox(self):
        MainGUI.combobox_0 = ttk.Combobox(
            master=MainGUI.window_0,  # 父容器
            height=10,  # 高度，下拉显示的条目数量
            width=20,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、disabled(禁止输入选择)
            cursor='arrow',  # 鼠标移动时样式
            font=('dengxian', 15),  # 字体 字号
            # textvariable='',  # 通过StringVar设置可以改变的值
            values=['select_0', 'select_1', 'select_2', 'select_3', 'select_4'],  # 设置设置下拉框的选项
        )
        MainGUI.combobox_0.place(x=100, y=175)

    # 按钮 编号:0 确认 消息弹窗
    def jumpMassage_0(self, e):
        tkinter.messagebox.showinfo('提示', '确认成功!(◕ᴗ◕✿)')  # 窗口名称 点击成功

    # 按钮 编号:1 确认 消息弹窗
    def jumpMassage_1(self, e):
        tkinter.messagebox.showinfo('提示', '返回成功!(◕ᴗ◕✿)')  # 窗口名称 点击成功

    # 主程序入口
    def Start(self):
        # 循环显示窗口
        MainGUI.window_0.mainloop()


# 开始运行
if __name__ == '__main__':
    MainGUI().Start()  # 运行
