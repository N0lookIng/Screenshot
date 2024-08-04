# GUI Powered By Tkinter
from keyboard import wait
from time import time
from threading import Thread, enumerate
import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path
from pyautogui import screenshot, size

try:
    def close():
        root.destroy()


    def nwindow(dict):
        while True:
            wait("Alt+Q")
            root.withdraw()
            st = time()
            screenshot1 = screenshot()
            dir1 = dict + '/screenshot' + str(time()) + '.png'
            screenshot1.save(dir1)
            end = time()
            root.deiconify()
            root.attributes('-topmost', True)
            messagebox.showinfo("提示", "已截图")


    def is_alive(var: list):
        for i in range(0, len(var) - 1):
            if var[i].name == "SC":
                return True
        return False


    def on_button_click():
        root.attributes("-topmost", 1)
        directory = filedialog.askdirectory(title='选择存储路径...')
        if directory:
            THC = enumerate()
            if not is_alive(THC):
                SC = Thread(name="SC", target=nwindow, args=(directory,))
                SC.start()
        else:
            directory = str(Path.home() / 'Desktop')
            print("将默认保存在桌面")
        label.config(text="按下Alt+Q以截图")
        dir_label.config(text="当前保存位置: " + directory)
        on_started(290, 90)


    def on_started(windowx, windowy):
        root.geometry(str(windowx) + 'x' + str(windowy) + '+' +
                      str(size[0] - windowx - 10) + '+' + str(size[1] - windowy - 40))


    # 主程序代码
    root = tk.Tk()
    root.title("截屏")
    size = list(size())

    # 不可调节大小
    root.resizable(width=False, height=False)
    # 重写关闭 WM_DELETE_WINDOW
    root.protocol("WM_DELETE_WINDOW", close)
    # 窗口初始化
    on_started(170, 70)
    root.attributes("-topmost", 1, "-toolwindow", 1)

    # 添加控件
    label = tk.Label(root, text='请选择截图保存路径', font=('微软雅黑', 10), justify=tk.CENTER, anchor=tk.E)
    label.pack()
    button = tk.Button(root, text="保存位置...", command=on_button_click, cursor="hand2", bd=2,
                       justify=tk.CENTER, anchor=tk.E)
    button.pack()
    dir_label = tk.Label(root, text="", font=('微软雅黑', 9), justify=tk.CENTER, anchor=tk.S)
    dir_label.pack()
    root.mainloop()

except KeyboardInterrupt:
    messagebox.showinfo("退出", "您已按下Crtl+C键")
except PermissionError:
    messagebox.showerror("PermissionError", "您没有适当的权限。请联系管理员")
except tk.TclError as e:
    messagebox.showerror("Fatal Error", "程序出现了一个问题\n" + str(e))
except Exception as e:
    messagebox.showerror("Fatal Error", "程序在运行时出现了一个错误\n" + str(e))
