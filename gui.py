# 页面设计：通过tkinter库建立gui界面，并使用其中的图形化界面控件来设计简洁的程序界面，便于交互，提升使用体验。

import tkinter
from test import Spider
from data_analysis import data_analysis
import sys

spider = Spider()
d_a = data_analysis()
#IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.

def touch1():  # 点击按钮1
    spider.getdata()


def touch2():  # 点击按钮2
    mname = e1.get()
    # print(mname)
    spider.insert(mname=mname)


def touch3():  # 点击按钮3
    dname = e1.get()
    comment = d_a.read(dname=dname)
    kword = " ".join(d_a.fenci(comment=comment))
    d_a.wcloud(kword)  # 调用词云


def touch4():  # 退出按钮
    sys.exit()


def touch5():  #
    d_a.read(dname=e1.get())
    grade = d_a.grades
    d_a.showg(grade=grade)

# 主界面
tk = tkinter.Tk()
tk.title('table')
width, height = 300, 400
width_max, height_max = tk.maxsize()
s_center = '%dx%d+%d+%d' % (width, height, (width_max-width)/2, (height_max-height)/2)  # 居中
tk.geometry(s_center)
tk.resizable(width=True, height=True)  # 是否可缩放

# 按钮
b1 = tkinter.Button(tk, text='开始', width=8, height=2, command=touch1)  # 开始获取数据按钮
b1.place(x=20, y=60)
b2 = tkinter.Button(tk, text='上传', width=8, height=2, command=touch2)  # 输入剧名按钮
b2.place(x=100, y=60)
b3 = tkinter.Button(tk, text="词云", width=8, height=2, command=touch3)  # 生成词云
b3.place(x=20, y=120)
b4 = tkinter.Button(tk, text="退出", width=8, height=2, command=touch4)  # 退出
b4.place(x=100, y=120)
b5 = tkinter.Button(tk, text="评分曲线", width=8, height=2,command=touch5)  # 评分曲线图
b5.place(x=20, y=180)

# 输入框
e1 = tkinter.Entry(tk, width=20)
e1.place(x=20, y=20)


tk.mainloop()
