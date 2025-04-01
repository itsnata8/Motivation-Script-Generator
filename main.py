from tkinter import *
from tkinter import ttk

class MyGUI:
    def __init__(self):
        # variables
        self.root = Tk()
        self.root.title("Motivation Script Generator")

        self.frm = ttk.Frame(self.root, width=500)
        self.frm.pack(padx=10)
        


        #create label
        self.lbl = ttk.Label(self.root, text="Motivation Script Generator", font = ("Times New Roman Bold", 24)).pack()

        #create input tema utama
        ttk.Label(self.root, text="Tema Utama", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan tema", font = ("Times New Roman", 12)).pack()
        temaUtamaInfo = "contoh: Mengatasi Kegagalan, Mencapai Impian,\n Semangat Pantang Menyerah."
        ttk.Label(self.root, text=temaUtamaInfo,justify="center", font = ("Times New Roman Italic", 10)).pack()
        self.temaUtamaValue = ttk.Entry(self.root, width = 70)
        self.temaUtamaValue.pack()

        #create input target audiens
        ttk.Label(self.root, text="Target Audiens", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan Target Audiens", font = ("Times New Roman", 12)).pack()
        targetAudiensInfo = "Siapa yang ingin Anda jangkau?\n Contoh: Anak muda, profesional, ibu rumah tangga"
        ttk.Label(self.root, text=targetAudiensInfo,justify="center", font=("Times New Roman Italic", 10)).pack()
        self.targetAudiens = ttk.Entry(self.root, width = 70)
        self.targetAudiens.pack()

        #create input poin kunci
        ttk.Label(self.root, text="Poin Kunci", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan Poin Poin Kunci (max 3)", font = ("Times New Roman", 12)).pack()
        poinKunciInfo = "contoh: Kegagalan adalah bagian dari proses"
        ttk.Label(self.root, text=poinKunciInfo,justify="center", font=("Times New Roman Italic", 10)).pack()
        ttk.Label(self.root, text="Poin 1",justify="center", font=("Times New Roman Italic", 10)).pack()
        self.poinKunci1 = ttk.Entry(self.root, width = 70)
        self.poinKunci1.pack(pady=5)
        ttk.Label(self.root, text="Poin 2",justify="center", font=("Times New Roman Italic", 10)).pack()
        self.poinKunci2 = ttk.Entry(self.root, width = 70)
        self.poinKunci2.pack(pady=5)
        ttk.Label(self.root, text="Poin 3",justify="center", font=("Times New Roman Italic", 10)).pack()
        self.poinKunci3 = ttk.Entry(self.root, width = 70)
        self.poinKunci3.pack(pady=5)

        #create input gaya bahasa
        ttk.Label(self.root, text="Gaya Bahasa", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan Gaya Bahasa", font = ("Times New Roman", 12)).pack()
        gayaBahasaInfo = "Pilih gaya bahasa, contoh: Inspiratif, energik, menyentuh, bersemangat"
        ttk.Label(self.root, text=gayaBahasaInfo,justify="center", font=("Times New Roman Italic", 10)).pack()
        self.gayaBahasa = ttk.Entry(self.root, width = 70)
        self.gayaBahasa.pack()

        self.submitBtn = ttk.Button(self.root, text="Generate", command=self.submitData).pack(pady=10)
        
        self.root.mainloop()                            

    # function
    def submitData(self):
        data = {
            "temaUtama" : self.temaUtamaValue.get(),
            "targetAudiens" : self.targetAudiens.get(),
            "poinKunci" : [self.poinKunci1.get(),self.poinKunci2.get(),self.poinKunci3.get()]
        }
        print(data)
        

MyGUI()                       
