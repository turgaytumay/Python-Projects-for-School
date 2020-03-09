from Tkinter import *
from ttk import Combobox
import tkFileDialog

# from clusters import *

# class for showing info about districts

class District():
    def __init__(self,name,election_results):
        self.name = name
        election_results = {}

# class for showing info about political parties

class PoliticalParties():
    def __init__(self,acronym,election_results):
        self.acronym = acronym
        election_results = {}

# class for gathering data from party class and districts class

class DataCenter():
    def __init__(self,districts,parties):
        districts = {}
        parties = {}

# class for interface

class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.initUI()

    def initUI(self):

        # first frame
        self.frame1 = Frame(self)
        self.pack()
        self.frame1.grid()
        self.frame1.grid(row=0, column=0)

        self.sign = Label(self.frame1, text="Election Data Analysis Tool v.1.0", bg="red", fg="white", font="Times 15 bold", width=108, height=2)
        self.sign.pack(fill=X, anchor=N)

        self.load_election = Button(self.frame1, text="Load Election Data", width=50, height= 3, command= self.load_election_data)
        self.load_election.pack(pady=10)

        # second frame

        self.frame2 = Frame(self)
        self.frame2.grid(row=1, column=0)

        self.cluster_dis = Button(self.frame2, text="Cluster Districts", width=50, height= 3, command= self.cluster_dis)
        self.cluster_dis.grid(row=1, column=0, pady=10, padx=20)

        self.cluster_political = Button(self.frame2, text="Cluster Political Parties", width=50, height= 3, command= self.cluster_political)
        self.cluster_political.grid(row=1, column=1, pady=10, padx=20)

        # these frames for canvas and other things

        self.frame3 = Frame(self)
        self.frame3.grid(row=2, column=0)

        self.frame4 = Frame(self)
        self.frame4.grid(row=3, column=0)


    def load_election_data(self):

        # listing data from text

        self.filename = open(tkFileDialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*"))))

        self.lines = [line for line in self.filename]
        self.results = {}
        district_list = []
        self.party_list = []
        party = False
        c = 0
        name = ""
        value = 0
        for line in self.lines[0:]:
            c += 1
            p = line.split('\t')

            if (p[0].find("Kaynak") > -1):
                party = False
                value = c + 1

            if (value == c):
                name = p[0].replace("\n", "")

                if name not in district_list:
                    district_list.append(name)

            if (p[0] == "Toplam"):
                party = False

            if (p[0].find("Kis.") > -1):
                vote_rate_in_districts = {}
                party = True

            if (party == True and p[0].find("Kis.") < 0 and p[0] != "BGMSZ"):
                vote_rate_in_districts[p[0].replace("\n", "")] = p[4].replace("%", "").replace("\n", "")

                if p[0] not in self.party_list:
                    self.party_list.append(p[0].replace("\n", ""))

            if (p[0] == "Toplam"):
                self.results[name] = vote_rate_in_districts


    def cluster_dis(self):

        # canvas and listbox

        self.canvas1 = Canvas(self.frame3, bg='#FFFFFF', width=1100, height=300)
        self.canvas1.grid(row=0, column=0)

        self.scollbary = Scrollbar(self.frame3, orient="vertical", command=self.canvas1.yview)
        self.scollbary.grid(row=0, column=0, sticky='nsew')

        self.scollbarx = Scrollbar(self.frame3, orient="horizontal", command=self.canvas1.xview)
        self.scollbarx.grid(row=0, column=0, sticky='nsew')

        Label(self.frame4, text="Districts :").grid(row=0, column=0)

        self.districts_listbox = Listbox(self.frame4, selectmode="multiple", height=13, width=20)
        self.districts_listbox.grid(row=0, column=1)

        # adding districts to listbox

        for i in self.results.keys():
            self.districts_listbox.insert(END,i)

        self.scollbary_listbox = Scrollbar(self.frame4, orient="vertical", command=self.districts_listbox.yview)
        self.scollbary_listbox.grid(row=0, column=1, sticky='nsew')

        Label(self.frame4, text="Threshold :").grid(row=0, column=2)

        self.combobox = Combobox(self.frame4, state="readonly", values=["%0", "%1", "%10", "%20", "%30", "%40", "%50"])
        self.combobox.grid(row=0, column=3)

        self.refine_button = Button(self.frame4, text="Refine Analysis", width=45, height=2, command=self.cluster_dis)
        self.refine_button.grid(row=0, column=4)

    def cluster_political(self):

        # canvas and listbox

        self.canvas1 = Canvas(self.frame3, bg='#FFFFFF', width=1100, height=300)
        self.canvas1.grid(row=0, column=0)

        self.scollbary = Scrollbar(self.frame3, orient="vertical", command=self.canvas1.yview)
        self.scollbary.grid(row=0, column=0, sticky='nsew')

        self.scollbarx = Scrollbar(self.frame3, orient="horizontal", command=self.canvas1.xview)
        self.scollbarx.grid(row=0, column=0, sticky='nsew')

        Label(self.frame4, text="Districts :").grid(row=0, column=0)

        self.districts_listbox = Listbox(self.frame4, selectmode="multiple", height=13, width=20)
        self.districts_listbox.grid(row=0, column=1)

        # adding districts to listbox

        for i in self.results.keys():
            self.districts_listbox.insert(END,i)

        self.scollbary_listbox = Scrollbar(self.frame4, orient="vertical", command=self.districts_listbox.yview)
        self.scollbary_listbox.grid(row=0, column=1, sticky='nsew')

        Label(self.frame4, text="Threshold :").grid(row=0, column=2)

        self.combobox = Combobox(self.frame4, state="readonly")
        self.combobox.grid(row=0, column=3)

        self.refine_button = Button(self.frame4, text="Refine Analysis", width=45, height=2, command=self.cluster_dis)
        self.refine_button.grid(row=0, column=4)



def main():
    root = Tk()
    root.title("Clustering")
    root.geometry("1300x800+10+10")
    app = GUI(root)

    root.mainloop()

main()