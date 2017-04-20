from tkinter import *
from tkinter import ttk

root = Tk()


Label(root, text='选出你觉得史上最帅的男人：').grid(row=0, column=0, sticky=W)

Radiobutton(root, text='帅森森', value=1).grid(row=1, column=0, sticky=W)
Radiobutton(root, text='我森', value=4).grid(row=2, column=0, sticky=W)
Radiobutton(root, text='赵汉森', value=3).grid(row=3, column=0, sticky=W)
Radiobutton(root, text='最帅森', value=6).grid(row=4, column=0, sticky=W)

Label(root, text='他的哪里最吸引你：').grid(row=1, column=1, sticky=W)
Checkbutton(root, text='迷人的眼睛').grid(row=2, column=1, stick=W)
Checkbutton(root, text='健硕的肌肉').grid(row=3, column=1, stick=W)
Checkbutton(root, text='性感的歌声').grid(row=4, column=1, stick=W)
root.mainloop()