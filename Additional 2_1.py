from Tkinter import *
import ttk
import tkFileDialog
import xlrd
from xlwt import Workbook
import datetime


class TeacherApp(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.Frame1 = Frame(self)
        self.pack()
        self.Frame1.pack(fill=X)

        Label(self.Frame1, text="SteelBox. INC. Calculator", font="Times 12 bold").pack()
        Button(self.Frame1, text="Import", width=12, command=self.import_data).pack(padx=50, pady=5, anchor=NW)

        self.Frame2 = Frame(self)
        self.Frame2.pack()

        self.Frame2_1 = Frame(self.Frame2, relief=GROOVE, borderwidth=1)
        self.Frame2_1.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

        Label(self.Frame2_1, text="Width").grid(row=2, column=0, padx=10, pady=5)
        Label(self.Frame2_1, text="Length").grid(row=3, column=0, padx=10, pady=5)
        Label(self.Frame2_1, text="Height").grid(row=4, column=0, padx=10, pady=5)
        Label(self.Frame2_1, text="Thickness").grid(row=5, column=0, padx=10, pady=5)
        self.entry_width_var = StringVar()
        self.entry_width = Entry(self.Frame2_1, width=10, textvariable= self.entry_width_var).grid(row=2, column=1, padx=10, pady=5)
        self.entry_length_var = StringVar()
        self.entry_length = Entry(self.Frame2_1, width=10, textvariable= self.entry_length_var).grid(row=3, column=1, padx=10, pady=5)
        self.entry_height_var = StringVar()
        self.entry_height = Entry(self.Frame2_1, width=10, textvariable= self.entry_height_var).grid(row=4, column=1, padx=10, pady=5)
        self.entry_thickness_var = StringVar()
        self.entry_thickness = Entry(self.Frame2_1, width=10, textvariable= self.entry_thickness_var).grid(row=5, column=1, padx=10, pady=5)

        self.Frame2_2_up = Frame(self.Frame2)
        self.Frame2_2_up.grid(row=0, column=1, padx=10, pady=10)

        Label(self.Frame2_2_up, text="Lid?").grid(row=0, column=0, padx=10, pady=2)
        Label(self.Frame2_2_up, text="Separator ?").grid(row=0, column=1, padx=10, pady=2)
        self.check_lid_var = IntVar()
        self.check_lid = Checkbutton(self.Frame2_2_up, variable=self.check_lid_var).grid(row=1, column=0)
        self.check_sep_var = IntVar()
        self.check_sep = Checkbutton(self.Frame2_2_up, variable=self.check_sep_var).grid(row=1, column=1)

        self.Frame2_2_down = Frame(self.Frame2, relief=GROOVE, borderwidth=1)
        self.Frame2_2_down.grid(row=1, column=1, padx=10, pady=10)

        Label(self.Frame2_2_down, text="Current \nSteel Price").grid(row=0, column=0, padx=10, pady=2)
        Label(self.Frame2_2_down, text="TRY/USD \nexhnage Rate").grid(row=1, column=0, padx=10, pady=2)
        self.entry_steel_price_var = StringVar()
        self.entry_steel_price = Entry(self.Frame2_2_down, width=10, textvariable= self.entry_steel_price_var).grid(row=0, column=1, padx=10, pady=2)
        self.entry_exhnage_rate_var = StringVar()
        self.entry_exhnage_rate = Entry(self.Frame2_2_down, width=10, textvariable= self.entry_exhnage_rate_var).grid(row=1, column=1, padx=10, pady=2)
        Button(self.Frame2_2_down, text="Get", width=10).grid(row=0, rowspan=2, column=2, padx=10, pady=2)

        self.Frame3 = Frame(self)
        self.Frame3.pack()

        Label(self.Frame3, text="Total Weight").grid(row=3, column=3, padx=10, pady=5)
        Label(self.Frame3, text="Total Price").grid(row=3, column=5, padx=10, pady=5)
        Button(self.Frame3, text="Calculate", width=10, command=self.calculate).grid(row=4, column=1, padx=10, pady=5)
        self.total_weight_var = StringVar()
        self.total_weight = Entry(self.Frame3, width=10, textvariable=self.total_weight_var).grid(row=4, column=3, padx=10, pady=5)
        self.total_price_var = StringVar()
        self.total_price = Entry(self.Frame3, width=10, textvariable=self.total_price_var).grid(row=4, column=5, padx=10, pady=5)
        Button(self.Frame3, text="Export", width=10, command=self.export).grid(row=4, column=6, padx=10, pady=5)
        self.total_volume_var = StringVar()
        self.total_area_var = StringVar()

    def import_data(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        self.book = xlrd.open_workbook(self.filename)
        self.sheet = self.book.sheet_by_index(0)
        rows = self.sheet.nrows
        cols = self.sheet.ncols
        self.lel = []

        for x in range(rows):
            a = 0
            for y in range(cols):
                if a != 0:
                    self.lel.append(self.sheet.cell(x,y).value)
                    a = 0
                else:
                    a = 1

        print self.lel

        self.entry_width_var.set(float(self.lel[0]))
        self.entry_length_var.set(float(self.lel[1]))
        self.entry_height_var.set(float(self.lel[2]))
        self.entry_thickness_var.set(float(self.lel[3]))

    def calculate(self):

        w = float(self.entry_width_var.get())
        l = float(self.entry_length_var.get())
        h = float(self.entry_height_var.get())
        t = float(self.entry_thickness_var.get())
        self.lid = int(self.check_lid_var.get())
        self.sep = int(self.check_sep_var.get())
        steel_price = float(self.entry_steel_price_var.get())
        d = 7.85

        self.surface_area = 2*(w*h + l*h)+w*l + self.lid*w*l + self.sep*w*h

        self.Volume = self.surface_area * t

        self.Weight = self.Volume * d

        self.Cost = self.Weight * steel_price


        self.total_price_var.set(int(self.Cost))
        self.total_weight_var.set(int(self.Weight))
        self.total_volume_var.set(int(self.Volume))
        self.total_area_var.set(int(self.surface_area))
    def export(self):
        x = datetime.date.today()
        wb = Workbook()
        sheet1 = wb.add_sheet('Sheet 1')

        sheet1.write(1, 0, str(x))
        sheet1.write(1, 1, 'Time')
        sheet1.write(1, 2, str(self.entry_width_var.get()))
        sheet1.write(1, 3, str(self.entry_length_var.get()))
        sheet1.write(1, 4, str(self.entry_height_var.get()))
        sheet1.write(1, 5, str(self.entry_thickness_var.get()))
        sheet1.write(1, 6, str(self.check_lid_var.get()))
        sheet1.write(1, 7, str(self.check_sep_var.get()))
        sheet1.write(1, 8, str(self.entry_steel_price_var.get()))
        sheet1.write(1, 9, str(self.entry_exhnage_rate_var.get()))
        sheet1.write(1, 10, str(self.total_area_var.get()))
        sheet1.write(1, 11, str(self.total_volume_var.get()))
        sheet1.write(1, 12, str(self.total_weight_var.get()))
        sheet1.write(1, 13, str(self.total_price_var.get()))

        sheet1.write(0, 0, 'Date')
        sheet1.write(0, 1, 'Time')
        sheet1.write(0, 2, 'Width')
        sheet1.write(0, 3, 'Length')
        sheet1.write(0, 4, 'Height')
        sheet1.write(0, 5, 'Thickness')
        sheet1.write(0, 6, 'Lid Exists')
        sheet1.write(0, 7, 'Seprator Exits')
        sheet1.write(0, 8, 'Steel Price')
        sheet1.write(0, 9, 'Usd/Try')
        sheet1.write(0, 10, 'Surface Area')
        sheet1.write(0, 11, 'Volume')
        sheet1.write(0, 12, 'Weight')
        sheet1.write(0, 13, 'Total Cost')

        wb.save('Output.xls')




def main():
    root = Tk()
    root.title("42")
    app = TeacherApp(root)
    root.mainloop()

main()