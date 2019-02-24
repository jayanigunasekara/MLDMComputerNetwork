from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from filesplit import *
from sha import *
import os


class Root (Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.selfile = ""
        self.title("Group E")
        self.minsize(440, 200)
        self.wm_iconbitmap('icon.ico')
        self.configure(background='#bdb76b')

        self.labelFrame = ttk.Labelframe(self, text="Upload a file")
        self.labelFrame.grid(column=0, row=1, padx=40, pady=40)

        self.button1()
        self.button2()

    def button1(self):
        self.button1 = ttk.Button(self.labelFrame, text="Browse a file", command=self.filedialog)
        self.button1.grid(column=1, row=1)

    def button2(self):
        self.button2 = ttk.Button(self.labelFrame, text="Upload", command=self.upload)
        self.button2.grid(column=1, row=5)

    def filedialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetype=(("jpeg", "*.jpg"), ("All Files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        self.selfile = self.filename

    def upload(self):

        if self.selfile:
            dir_path = os.path.split(self.selfile)[0]
            filename = os.path.split(self.selfile)[1]
            if not os.path.exists("Splitted_" + filename):
                os.mkdir("Splitted_" + str(filename))
                print("Directory ", "Splitted_" + str(filename), " Created ")
            else:
                print("Directory ", "Splitted_" + filename, " already exists")
            fs = FileSplit(dir_path + "/" + filename, 1024 * 2, "Splitted_" + filename)
            fs.split()
            sha = Sha(self.selfile, "Splitted_" + filename, "Library.txt")
            sha.calc_sha()
            self.selfile = ""


if __name__ == '__main__':
    root = Root()
    root.mainloop()
