from Tkinter import *
import ttk
import tkFileDialog
import xlrd


class TeacherApp(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.initUI()

        # Treeview for showing people in excel file

        self.tree = ttk.Treeview(columns=["ID", "Name", "Section"], show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.column("ID",width=80)

        self.tree.heading("Name", text="Name")
        self.tree.column("Name", width=100)

        self.tree.heading("Section", text="Section")
        self.tree.column("Section", width=80)

        self.tree.bind("<<TreeviewSelect>>",self.select_person)

        self.scollbar = Scrollbar(self.frame2, orient="vertical", command=self.tree.yview)

        self.tree.grid(row=0, column=0,in_=self.frame2)
        self.scollbar.grid(row=0, column=1, sticky='nsew')
        self.tree.configure(yscrollcommand=self.scollbar.set)


    def initUI(self):
        # first frame
        self.frame1 = Frame(self)
        self.pack()
        self.frame1.pack(fill=X)
        # second frame

        self.frame2 = Frame(self)
        self.frame2.pack()

        self.sign1 = Label(self.frame1, text="Grades Management Tool", bg="spring green", fg="white", font="Times 25 bold",height=1)
        self.sign1.pack(fill=X, anchor=N)

        self.selectfile = Button(self.frame1, text="Select File", width=10, command=self.select_file)
        self.selectfile.pack(padx=50, pady=10, anchor=NW)

        self.showdata = Button(self.frame2, text="Show Data", width=10, command=self.select_showdata)
        self.showdata.grid(row=0, column=2)

        # this frame for studnet details

        self.frame2_2 = Frame(self.frame2, borderwidth=1, height=15, width=100, relief=GROOVE)
        self.frame2_2.grid(row=0, column=3, padx=5)

        self.frame2_2_1 = Frame(self.frame2_2)
        self.frame2_2_1.grid(row=0, column=0)

        self.sign2_2 = Label(self.frame2_2_1, text="Student Details:", bg="cornflower Blue", fg="white", font="Times 10 bold",
                        height=1, width=40)
        self.sign2_2.pack(fill=X, anchor=N)

        self.frame2_2_2 = Frame(self.frame2_2)
        self.frame2_2_2.grid(row=1, column=0)

        self.frame2_2_2_1 = Frame(self.frame2_2_2)
        self.frame2_2_2_1.grid(row=0, column=0, sticky=W)

        Label(self.frame2_2_2_1, text="Name:").grid(row=0, column=0, sticky=W)
        Label(self.frame2_2_2_1, text="Section:").grid(row=1, column=0, sticky=W)
        Label(self.frame2_2_2_1, text="ID:").grid(row=2, column=0, sticky=W)
        Label(self.frame2_2_2_1, text="Dept:").grid(row=3, column=0, sticky=W)
        Label(self.frame2_2_2_1, text="GPA:").grid(row=4, column=0, sticky=W)

        self.frame2_2_2_2 = Frame(self.frame2_2_2)
        self.frame2_2_2_2.grid(row=0, column=1)

        self.frame2_2_2_3 = Frame(self.frame2_2_2)
        self.frame2_2_2_3.grid(row=0, column=2)

        Label(self.frame2_2_2_3, text="MP1 Grade:").grid(row=0, column=0, sticky=W)
        Label(self.frame2_2_2_3, text="MP2 Grade:").grid(row=1, column=0, sticky=W)
        Label(self.frame2_2_2_3, text="MP3 Grade:").grid(row=2, column=0, sticky=W)
        Label(self.frame2_2_2_3, text="MT Grade:").grid(row=3, column=0, sticky=W)
        Label(self.frame2_2_2_3, text="Final Grade:").grid(row=4, column=0, sticky=W)

        self.frame2_2_2_4 = Frame(self.frame2_2_2)
        self.frame2_2_2_4.grid(row=0, column=3)

        # third frame

        self.frame3 = Frame(self, height=15, width=40, borderwidth=1, relief=GROOVE)
        self.frame3.pack()

        Label(self.frame3, text="Projects:\nGrades: \nExport As:").grid(row=0, column=0, sticky=W)

        # this frame for entreies

        self.frame3_1 = Frame(self.frame3)
        self.frame3_1.grid(row=0, column=1)

        Label(self.frame3_1, text="MP1").grid(row=0, column=0, padx=10)
        Label(self.frame3_1, text="MP2").grid(row=0, column=1, padx=10)
        Label(self.frame3_1, text="MP3").grid(row=0, column=2, padx=10)
        Label(self.frame3_1, text="MT").grid(row=0, column=3, padx=10)
        Label(self.frame3_1, text="Final").grid(row=0, column=4, padx=10)

        self.entry1 = StringVar()
        self.entry2 = StringVar()
        self.entry3 = StringVar()
        self.entrymt = StringVar()
        self.entryf = StringVar()

        self.mp1_entry = Entry(self.frame3_1, width=10, textvariable=self.entry1).grid(row=1, column=0, padx=10)
        self.mp2_entry = Entry(self.frame3_1, width=10, textvariable=self.entry2).grid(row=1, column=1, padx=10)
        self.mp3_entry = Entry(self.frame3_1, width=10, textvariable=self.entry3).grid(row=1, column=2, padx=10)
        self.mt_entry = Entry(self.frame3_1, width=10, textvariable=self.entrymt).grid(row=1, column=3, padx=10)
        self.final_entry = Entry(self.frame3_1, width=10, textvariable=self.entryf).grid(row=1, column=4, padx=10)

        self.save_grades = Button(self.frame3, text="Save Grades", width=10, command=self.save_grades)
        self.save_grades.grid(row=0, column=2)

        self.frame4 = Frame(self, height=15, width=40)
        self.frame4.pack()

        Checkbutton(self.frame4).grid(row=0, column=0)
        Checkbutton(self.frame4).grid(row=1, column=0)
        Checkbutton(self.frame4).grid(row=2, column=0)

        Label(self.frame4, text="csv").grid(row=0, column=1)
        Label(self.frame4, text="txt").grid(row=1, column=1)
        Label(self.frame4, text="xls").grid(row=2, column=1)

        Label(self.frame4, text="File Name:").grid(row=0, column=2, padx=5)

        Entry(self.frame4).grid(row=0, column=3)

        Button(self.frame4, text="Export Data", width=26).grid(row=1, column=2, columnspan=3)

        self.frame5 = Frame(self, height=15, width=40)
        self.frame5.pack()

        Label(self.frame5, text="INFO:").grid(row=0, column=0)

        Label(self.frame5, text="asjdasjdkasd").grid(row=0, column=1)
    def select_file(self):

        # this funtion select exel file and read

        self.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        self.book = xlrd.open_workbook(self.filename)
        self.sheet = self.book.sheet_by_index(0)
        rows = self.sheet.nrows
        cols = self.sheet.ncols
        self.table = list()
        self.record = list()
        z = 0
        for x in range(rows-1):
            for y in range(cols):
                self.record.append(self.sheet.cell(x+1,y).value)
            self.tree.insert("", z, text="Line"+str(z), values=(int(self.record[0]), self.record[1], self.record[2]))
            z +=1
            self.table.append(self.record)
            self.record = []
            x +=1
    def select_person(self,event):

        # this function show student information in treeview

        for item in self.tree.selection():
            item_text = self.tree.item(item, "text")
        for i in str(item):
            try :
                i = int(i)
                Label(self.frame2_2_2_2, text=self.table[i][1]).grid(row=0, column=0, sticky=W)
                Label(self.frame2_2_2_2, text=self.table[i][2]).grid(row=1, column=0, sticky=W)
                Label(self.frame2_2_2_2, text=self.table[i][0]).grid(row=2, column=0, sticky=W)
                Label(self.frame2_2_2_2, text=self.table[i][3]).grid(row=3, column=0, sticky=W)
                Label(self.frame2_2_2_2, text=self.table[i][4]).grid(row=4, column=0, sticky=W)
                Label(self.frame2_2_2_4, text=self.table[i][5]).grid(row=0, column=0, sticky=W)
                Label(self.frame2_2_2_4, text=self.table[i][6]).grid(row=1, column=0, sticky=W)
                Label(self.frame2_2_2_4, text=self.table[i][7]).grid(row=2, column=0, sticky=W)
                Label(self.frame2_2_2_4, text=self.table[i][8]).grid(row=3, column=0, sticky=W)
                Label(self.frame2_2_2_4, text=self.table[i][9]).grid(row=4, column=0, sticky=W)
            except:
                pass
    def select_showdata(self):
        print "Show Data"
    def save_grades(self):
        ntext1 = self.entry1.get
        ntext2 = self.entry2.get
        ntext3 = self.entry3.get
        ntextmt = self.entrymt.get
        ntextf = self.entryf.get
        print str(ntext1)
        print ntext2
        print ntext3
        print ntextmt
        print ntextf




def main():
    root = Tk()
    root.title("Not Savar 3000")
    app = TeacherApp(root)
    root.mainloop()

main()