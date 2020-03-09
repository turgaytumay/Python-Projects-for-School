from Tkinter import *
import tkFileDialog
from recommendations import *
import os

class Functionality():
    def __init__(self,id,name):
        id = self.id
        name = self.name

class Evidence():
    def __init__(self,evidence_code_acronym,numeric_value):
        evidence_code_acronym = self.evidence_code_acronym
        numeric_value = self.numeric_value

class Annotation():
    def __init__(self):
        pass

class Protein():
    def __init__(self,id,name,annotations):
        id = self.id
        name = self.name
        annotations = {}

class DataCenter():
    def __init__(self,proteins,evidence_codes):
        proteins = {}
        evidence_codes = {}

class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.frame1 = Frame(self)
        self.pack()
        self.frame1.grid()
        self.frame1.grid(row=0, column=0)

        self.sign1 = Label(self.frame1, text="Protein Function Prediction Tool", bg="spring green", fg="white", font="Times 25 bold", height=1)
        self.sign1.pack(fill=X)

        self.frame2 = Frame(self)
        self.frame2.grid(row=1, column=0)

        # These buttons for selecting file

        self.upload_ann = Button(self.frame2, text="Upload\nAnnotations", width=10, command=self.select_protein1)
        self.upload_ann.grid(row=0, column=0, pady=20, padx=20)

        self.upload_evidance = Button(self.frame2, text="Upload Evidence\nCode Values", width=15, command=self.select_protein2)
        self.upload_evidance.grid(row=0, column=1, pady=20, padx=20)

        self.upload_go = Button(self.frame2, text="Upload GO File", width=12, command=self.select_go_file)
        self.upload_go.grid(row=0, column=2, pady=20, padx=20)

        # frame for listboxes and scrollbars

        self.frame3 = Frame(self)
        self.frame3.grid(row=2, column=0)

        self.sign_proteins = Label(self.frame3, text="Proteins", height=1)
        self.sign_proteins.grid(row=0, column=0)

        self.sign_similarty = Label(self.frame3, text="Similarity Metric", height=1)
        self.sign_similarty.grid(row=0, column=1)

        self.sign_similar_protein = Label(self.frame3, text="Similar Protein", height=1)
        self.sign_similar_protein.grid(row=0, column=2)

        self.sign_predicted = Label(self.frame3, text="Predicted Function", height=1)
        self.sign_predicted.grid(row=0, column=3)

        self.proteins_listbox = Listbox(self.frame3, selectmode="single", height=13, width=40)
        self.proteins_listbox.grid(row=1, column=0, padx=10)

        self.scollbar1 = Scrollbar(self.frame3, orient="vertical", command=self.proteins_listbox.yview)
        self.scollbar1.grid(row=1, column=0, sticky='nsew')

        self.frame3_metric = Frame(self.frame3, borderwidth=1, relief=GROOVE)
        self.frame3_metric.grid(row=1, column=1, padx=10)

        self.checkbutton1 = Checkbutton(self.frame3_metric)
        self.checkbutton1.grid(row=0, column=0)
        self.checkbutton2 = Checkbutton(self.frame3_metric)
        self.checkbutton2.grid(row=1, column=0)

        self.sign_pearson = Label(self.frame3_metric, text="Pearson", height=1)
        self.sign_pearson.grid(row=0, column=1)
        self.sign_euclidean = Label(self.frame3_metric, text="Euclidean", height=1)
        self.sign_euclidean.grid(row=1, column=1)

        self.similar_proteins_listbox = Listbox(self.frame3, selectmode="single", height=13, width=40)
        self.similar_proteins_listbox.grid(row=1, column=2, padx=10)

        self.scollbar1 = Scrollbar(self.frame3, orient="vertical", command=self.similar_proteins_listbox.yview)
        self.scollbar1.grid(row=1, column=2, sticky='nsew')

        self.predicted_func_listbox = Listbox(self.frame3, selectmode="single", height=13, width=60)
        self.predicted_func_listbox.grid(row=1, column=3, padx=10)

        self.scollbar1 = Scrollbar(self.frame3, orient="vertical", command=self.predicted_func_listbox.yview)
        self.scollbar1.grid(row=1, column=3, sticky='nsew')

    #     this function showing go file in list box

    def select_protein1(self):
        self.filename = open(tkFileDialog.askopenfilename(initialdir="/", title="Select Annotation File", filetypes=(("gaf files", "*.gaf"), ("all files", "*.*"))))
        lines = self.filename.readlines()
        for i in range(len(lines)):
            line = lines[i]
            line = line.split("\t")
            if len(line)<2:
                continue
            self.proteins_listbox.insert(END, line[2])

    def select_protein2(self):
        self.filename = open(tkFileDialog.askopenfilename(initialdir="/", title="Select Annotation File",
                                                filetypes=(("txt files", "*.txt"), ("all files", "*.*"))))



    def select_go_file(self):
        self.filename = open(tkFileDialog.askopenfilename(initialdir="/", title="Select Annotation File",
                                                filetypes=(("obo files", "*.obo"), ("all files", "*.*"))))









def main():
    root = Tk()
    root.title("Not Savar 3000")
    app = GUI(root)
    root.mainloop()

main()