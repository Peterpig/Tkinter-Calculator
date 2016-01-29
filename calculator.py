# coding=utf-8

from Tkinter import * 

class Calculator:
    def __init__(self):
        self.total = 0
        self.top = Tk()
        self.top.title('收银系统 V1.0')
        self.top.geometry('300x350')

        # frame_top
        self.frame_top = Frame(self.top)

        # 单价Label
        self.price = Label(self.frame_top, text='单价：')
        self.price.grid(row=0, column=0)

        # 单价输入框
        self.p = StringVar()
        self.price_entry = Entry(self.frame_top, textvariable=self.p)
        self.price_entry.grid(row=0, column=1)

        # 确定按钮
        self.ok_button = Button(self.frame_top, text='确定', command=self.ok, padx=10, activebackground='green')
        self.ok_button.grid(row=0, column=2, padx=5, pady=5)

        # 数目label
        self.num = Label(self.frame_top, text='数目：')
        self.num.grid(row=1, column=0)

        # 数目输入框
        self.n = StringVar()
        self.num_entry = Entry(self.frame_top, textvariable=self.n)
        self.num_entry.grid(row=1, column=1)

        # 重置按钮
        self.reset_button = Button(self.frame_top, text='重置', command=self.reset, padx=10, activebackground='red')
        self.reset_button.grid(row=1, column=2, padx=5, pady=5)

        self.frame_top.pack()

        # 账单
        self.text_area = Text(self.top, height=15)
        self.text_area.config(state=DISABLED)
        self.text_area.pack()

        self.frame_bottom = Frame(self.top)
        self.label = Label(self.frame_bottom, text='合计：', font=('Helvetica', 12))
        self.label2 = Label(self.frame_bottom, text=self.total, font=('Helvetica', 20, 'bold'))
        self.label.grid(row=0, column=0)
        self.label2.grid(row=0, column=1)
        self.frame_bottom.pack(side=LEFT)

    def ok(self):
        """确定按钮事件"""
        num = 0
        price = 0
        try:
            price = int(self.p.get())
        except Exception, e:
            self.p.set('请输入正确的值！')

        try:
            num = int(self.n.get())
        except Exception, e:
            self.n.set('请输入正确的值！')

        if num and price:
            self.text_area.config(state=NORMAL)
            _total = price * num
            self.total += _total
            text = "单价：%s  数量：%s  合计：%s \n" % (price, num, _total)
            self.text_area.insert(END,text)
            self.text_area.config(state=DISABLED)
            self.label2['text']= self.total

    def reset(self):
        """重置按钮事件"""
        self.p.set('')
        self.n.set('')
        self.text_area.config(state=NORMAL)
        self.text_area.delete("0.0", END)
        self.text_area.config(state=DISABLED)
        self.total = 0
        self.label2['text'] = self.total

def main():
    c = Calculator()
    mainloop()


if __name__ == '__main__':
    main()