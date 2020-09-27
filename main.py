import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=1, fill=tk.BOTH, anchor=tk.NW)
        self.create_widgets()

    def create_widgets(self):
        # URL入力バー
        self.url_bar = tk.Entry(self)
        self.url_bar.grid(column = 0, row = 0, sticky = 'nsew')
        # 移動ボタン
        self.url_button = tk.Button(self, text="GO", command=self.enter_url)
        self.url_button.grid(column = 1, row = 0, sticky = 'nsew')
        self.columnconfigure(0, weight=1)
        # ページフレーム
        self.page = tk.Frame(self, bg='WHITE')
        self.page.grid(column = 0, row = 1, columnspan= 2, sticky = 'nsew')
        self.rowconfigure(1, weight=1)

    def reset_page(self):
        self.page.pack_forget()

    def enter_url(self):
         #ページをリセット
        self.reset_page()
        # ページ表示
        x1 = tk.Label(self.page, text='Hello world!', bg='WHITE')
        x1.place(x=0, y=0)

root = tk.Tk()
root.geometry('800x600')
app = Application(master=root)
app.mainloop()

