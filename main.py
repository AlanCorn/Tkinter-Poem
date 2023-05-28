import tkinter as tk
import requests
from pprint import pprint

# 今日诗词API
URL = 'https://v2.jinrishici.com/sentence'
Headers = {
    'X-User-Token': 'TgzlHhedtfTCyo3GVNuNeoDzrgUpViD/'
}
# 进行窗口的基本配置
root_window = tk.Tk()
root_window.title('今日诗词')  # 设置窗口title
root_window.geometry('800x800')  # 设置窗口大小:宽x高
root_window["background"] = "#E6E6E6"  # 设置主窗口的背景颜色
# 配置tkinter变量，实现页面响应式
title = tk.StringVar()
author = tk.StringVar()
poem = tk.StringVar()

# 刷新数据的函数
def loadPoemData():
    poemData = requests.get(URL, headers=Headers).json()['data']
    pprint(poemData)
    title.set(poemData['origin']['title'])
    author.set("[" + poemData['origin']['dynasty'] + "]" + poemData['origin']['author'])
    poem.set('\n'.join(poemData['origin']['content']))

loadPoemData()
# 添加三个Label控件，配置基本属性
titleLabel = tk.Label(root_window,
                      textvariable=title,
                      bg="#E6E6E6",
                      font=('Time', 20, 'bold'))
authorLabel = tk.Label(root_window,
                       textvariable=author,
                       bg="#E6E6E6",
                       font=('Time', 10))
poemLabel = tk.Label(root_window,
                     textvariable=poem,
                     bg="#E6E6E6",
                     font=('Time', 12))
# 将文本内容放置在主窗口内
titleLabel.pack()
authorLabel.pack()
poemLabel.pack()

# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
refresh = tk.Button(root_window, text="换一首", command=loadPoemData)
button = tk.Button(root_window, text="关闭", command=root_window.quit)

# 将按钮放置在主窗口内
button.pack(side="bottom")
refresh.pack(side="bottom")

# 进入主循环，显示主窗口
root_window.mainloop()
