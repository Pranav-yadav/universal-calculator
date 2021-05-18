# Programmers Calculator Script
from tkinter import *
from arithmetic import *
import tkinter as tk


def systemConverter():
    class App:
        def __init__(self, master):

            self.menubar = tk.Menu(master)
            master.config(menu=self.menubar)

            self.entry = tk.Entry(master)

            self.lstbx1 = tk.Listbox(master, selectmode=tk.BROWSE, exportselection=0)
            self.lstbx2 = tk.Listbox(master, selectmode=tk.BROWSE, exportselection=0)

            for i in ["Binary", "Octal", "Decimal", "Hexadecimal"]:
                self.lstbx1.insert(tk.END, i)
                self.lstbx2.insert(tk.END, i)

            self.result = tk.Label(master, text="0")
            self.error = tk.Label(master, text="")
            #self.credits = tk.Label(master, text="Copyright whatever idc")

            self.quit_button = tk.Button(master, text="Quit", fg="red",
                                         command=master.quit)

            self.submit_button = tk.Button(master, text="Submit", command=self.submit)

            self.layout()

        def layout(self):
            self.lstbx1.grid(row=0, column=0)
            self.lstbx2.grid(row=0, column=1)
            self.entry.grid(row=1, column=0)
            self.result.grid(row=1, column=1)
            self.submit_button.grid(row=2, column=0)
            self.quit_button.grid(row=2, column=1)
            #self.credits.grid(row=3, column=0)
            self.error.grid(row=3, column=1)

        def submit(self):
            try:
                tmp = self.entry.get()
                calc_src = self.lstbx1.curselection()
                calc_dst = self.lstbx2.curselection()

                src = {0: 2, 1: 8, 2: 10, 3: 16}
                tmp = int(tmp, src[calc_src[0]])

                dst = {0: bin, 1: oct, 2: int, 3: hex}
                tmp = dst[calc_dst[0]](tmp)

                self.error.configure(text="")
                self.result.configure(text=tmp)
            except ValueError:
                self.error.configure(text="ERR")
                print("Error, cannot convert the specified input")

    root = tk.Tk()
    app = App(root)
    root.mainloop()
    #root.destroy()

if __name__ == "__main__":
    systemConverter()