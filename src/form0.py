#
# Window Edited by Pycharm.
# Time : 2022/08/30
# Author : YU.J.P
#

"""
    版本: V1.0
    基本功能:
        1. 基本窗体模板

"""

import tkinter as tk # 窗口视窗
from tkinter import messagebox  # 消息窗口
from tkinter import ttk  # 下拉选择框


# 自定义 GUI
class CustomGUI:

    __VERSION = 'Form V1.2'  # 版本信息 私有

    root_width = 500  # 窗口宽度
    root_height = 300  # 窗口宽度

    # 构造函数
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.__VERSION)
        self.root.geometry(str(self.root_width) + 'x' + str(self.root_height) + '+500+150')
        # 创建主菜单实例
        self.menubar = tk.Menu(self.root)
        # 显示菜单,将root根窗口的主菜单设置为menu
        self.root.config(menu=self.menubar)
        # 加载组件
        self.interface()

    # 加载组件
    def interface(self):
        """"界面编写位置"""
        # 在 menubar 上设置菜单名，并关联一系列子菜单
        self.menubar.add_cascade(label="文件", menu=self.papers())
        self.menubar.add_cascade(label="查看", menu=self.about())

    #
    def papers(self):
        # menu = tk.Menu(self.menubar, tearoff=1)  # 创建子菜单实例
        # 1的话多了一个虚线,如果点击的话就会发现,这个菜单框可以独立出来显示
        menu = tk.Menu(self.menubar, tearoff=0)
        # 创建单选框
        for item in ['新建', '打开', '保存', '另存为']:
            menu.add_command(label=item)
        return menu

    # 查看指示按钮
    def about(self):
        amenu = tk.Menu(self.menubar, tearoff=0)
        # 添加复选框
        for item in ['项目复选框', '文件扩展名', '隐藏的项目']:
            amenu.add_checkbutton(label=item)
        return amenu


# 运行
if __name__ == '__main__':
    CustomGUI().root.mainloop()