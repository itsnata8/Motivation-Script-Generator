from tkinter import *
from tkinter import ttk

class MyGUI:
    def __init__(self):
        # variables
        self.root = Tk()
        self.root.title("Motivation Script Generator")
        self.root.geometry("500x500")

        self.frm = ttk.Frame(self.root, padding=30)
        #create label
        self.lbl = ttk.Label(self.root, text="Motivation Script Generator", font = ("Times New Roman Bold", 24)).pack()

        #create input tema utama
        ttk.Label(self.root, text="Tema Utama", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan tema", font = ("Times New Roman", 12)).pack()
        temaUtamaInfo = "contoh: Mengatasi Kegagalan, Mencapai Impian, Semangat Pantang Menyerah."
        ttk.Label(self.root, text=temaUtamaInfo, font = ("Times New Roman Italic", 10)).pack()
        self.temaUtamaValue = ttk.Entry(self.root, width = 70)
        self.temaUtamaValue.pack()

        #create input target audiens
        ttk.Label(self.root, text="Target Audiens", font = ("Times New Roman Bold", 14)).pack()
        ttk.Label(self.root, text = "Masukkan Target Audiens", font = ("Times New Roman", 12)).pack()
        temaUtamaInfo = "Siapa yang ingin Anda jangkau?\n Contoh: Anak muda, profesional, ibu rumah tangga"
        ttk.Label(self.root, text=temaUtamaInfo,justify="center", font=("Times New Roman Italic", 10)).pack()
        self.targetAudiens = ttk.Entry(self.root, width = 70)
        self.targetAudiens.pack()

        self.submitBtn = ttk.Button(self.root, text="Generate", command=self.submitData).pack(pady=10)
        
        self.root.mainloop()                            

    # function
    def submitData(self):
        data = {
            "temaUtama" : self.temaUtamaValue.get(),
            "targetAudiens" : self.targetAudiens.get()
        }
        print(data)
        

MyGUI()                       
