from tkinter import *
from tkinter import ttk
import backend

class MyGUI:
    def __init__(self):
        # variables
        self.root = Tk()
        self.root.title("Motivation Script Generator")
        self.root.geometry("1000x610")
        self.root.resizable(False, False)

        self.frmTitle = ttk.Frame(self.root)
        self.frmTitle.pack(padx=10, pady=10, side=TOP)

        self.frm1 = ttk.Frame(self.root, width=500)
        self.frm1.pack(padx=10, pady=10, side=LEFT, anchor=N)

        self.frm2 = ttk.Frame(self.root, width=500)
        self.frm2.pack(padx=10,pady=10, side=RIGHT, anchor=N)

        self.frmFooter = ttk.Frame(self.root)
        self.frmFooter.pack(padx=10, pady=10, side=BOTTOM, fill=X)

        self.heading1 = ("Times New Roman Bold", 24)
        self.heading2 = ("Times New Roman Bold", 14)
        self.body = ("Times New Roman", 12)
        self.caption = ("Times New Roman Italic", 10)
        


        #create label
        self.lbl = ttk.Label(self.frmTitle, text="Motivation Script Generator", font = self.heading1).pack()

        #create input tema utama
        ttk.Label(self.frm1, text="Tema Utama", font = self.heading2).pack()
        ttk.Label(self.frm1, text = "Masukkan tema", font = self.body).pack()
        temaUtamaInfo = "contoh: Mengatasi Kegagalan, Mencapai Impian,\n Semangat Pantang Menyerah."
        ttk.Label(self.frm1, text=temaUtamaInfo,justify="center", font = self.caption).pack()
        self.temaUtamaValue = ttk.Entry(self.frm1, width = 70)
        self.temaUtamaValue.pack()

        #create input target audiens
        ttk.Label(self.frm1, text="Target Audiens", font = self.heading2).pack()
        ttk.Label(self.frm1, text = "Masukkan Target Audiens", font = self.body).pack()
        targetAudiensInfo = "Siapa yang ingin Anda jangkau?\n Contoh: Anak muda, profesional, ibu rumah tangga"
        ttk.Label(self.frm1, text=targetAudiensInfo,justify="center", font=self.caption).pack()
        self.targetAudiens = ttk.Entry(self.frm1, width = 70)
        self.targetAudiens.pack()

        #create input poin kunci
        ttk.Label(self.frm1, text="Poin Kunci", font = self.heading2).pack()
        ttk.Label(self.frm1, text = "Masukkan Poin Poin Kunci (max 3)", font = self.body).pack()
        poinKunciInfo = "contoh: Kegagalan adalah bagian dari proses"
        ttk.Label(self.frm1, text=poinKunciInfo,justify="center", font=self.caption).pack()
        ttk.Label(self.frm1, text="Poin 1",justify="center", font=self.caption).pack()
        self.poinKunci1 = ttk.Entry(self.frm1, width = 70)
        self.poinKunci1.pack(pady=5)
        ttk.Label(self.frm1, text="Poin 2",justify="center", font=self.caption).pack()
        self.poinKunci2 = ttk.Entry(self.frm1, width = 70)
        self.poinKunci2.pack(pady=5)
        ttk.Label(self.frm1, text="Poin 3",justify="center", font=self.caption).pack()
        self.poinKunci3 = ttk.Entry(self.frm1, width = 70)
        self.poinKunci3.pack(pady=5)

        #create input gaya bahasa
        ttk.Label(self.frm2, text="Gaya Bahasa", font = self.heading2).pack()
        ttk.Label(self.frm2, text = "Masukkan Gaya Bahasa", font = self.body).pack()
        gayaBahasaInfo = "Pilih gaya bahasa, contoh: Inspiratif, energik, menyentuh, bersemangat"
        ttk.Label(self.frm2, text=gayaBahasaInfo,justify="center", font=self.caption).pack()
        self.gayaBahasa = ttk.Entry(self.frm2, width = 70)
        self.gayaBahasa.pack()

        #create input Kalimat Pembuka
        ttk.Label(self.frm2, text="Kalimat Pembuka", font = self.heading2).pack()
        ttk.Label(self.frm2, text = "Masukkan Kalimat Pembuka", font = self.body).pack()
        kalimatPembukaInfo = "Sediakan opsi atau biarkan kosong\n contoh: \"Pernahkah kamu merasa jatuh dan sulit bangkit?\""
        ttk.Label(self.frm2, text=kalimatPembukaInfo,justify="center", font=self.caption).pack()
        self.kalimatPembuka = ttk.Entry(self.frm2, width = 70)
        self.kalimatPembuka.pack()

        #create input Kalimat Penutup
        ttk.Label(self.frm2, text="Kalimat Penutup", font = self.heading2).pack()
        ttk.Label(self.frm2, text = "Masukkan Kalimat Penutup", font = self.body).pack()
        kalimatPenutupInfo = "Apa yang Anda ingin audiens lakukan?\n contoh: \"Jangan menyerah, kejar mimpimu!\""
        ttk.Label(self.frm2, text=kalimatPenutupInfo,justify="center", font=self.caption).pack()
        self.kalimatPenutup = ttk.Entry(self.frm2, width = 70)
        self.kalimatPenutup.pack()

        #create input Kata kunci
        ttk.Label(self.frm2, text="Kata Kunci", font = self.heading2).pack()
        ttk.Label(self.frm2, text = "Masukkan Kata Kunci", font = self.body).pack()
        kataKunciInfo = "Contoh: Semangat, impian, sukses, bangkit, berani, jangan menyerah"
        ttk.Label(self.frm2, text=kataKunciInfo,justify="center", font=self.caption).pack()
        self.kataKunci = ttk.Entry(self.frm2, width = 70)
        self.kataKunci.pack()
        
        #create input Visualisasi yang dibayangkan
        ttk.Label(self.frm2, text="Visualisasi", font = self.heading2).pack()
        ttk.Label(self.frm2, text = "Masukkan Visualisasi", font = self.body).pack()
        visualisasiInfo = "Deskripsikan adegan atau gambar yang mendukung narasi.\nContoh: Seseorang yang mendaki gunung, orang yang tersenyum setelah berhasil"
        ttk.Label(self.frm2, text=visualisasiInfo,justify="center", font=self.caption).pack()
        self.visualisasi = ttk.Entry(self.frm2, width = 70)
        self.visualisasi.pack()



        self.submitBtn = ttk.Button(self.frm2, text="Generate", command=self.submitData).pack(fill=X, padx=20, pady=5)
        
        self.root.mainloop()                            

    # function
    def submitData(self):
        data = {
            "temaUtama" : self.temaUtamaValue.get(),
            "targetAudiens" : self.targetAudiens.get(),
            "poinKunci" : [self.poinKunci1.get(),self.poinKunci2.get(),self.poinKunci3.get()],
            "gayaBahasa" : self.gayaBahasa.get(),
            "kalimatPembuka" : self.kalimatPembuka.get(),
            "kalimatPenutup" : self.kalimatPenutup.get(),
            "kataKunci" : self.kataKunci.get(),
            "visualisasi" : self.visualisasi.get()
        }
        content = backend.Backend().generate(data);
        if content :
            self.open_secondary_window(content)
        else:
            content = "Error"

    def open_secondary_window(self, content):
        # Create secondary (or popup) window.
        secondary_window = Toplevel()
        secondary_window.title("Secondary Window")
        

        # Create a Label widget to display the content.
        content_label = Label(secondary_window, text=content)
        content_label.pack(padx=10, pady=10)
        
        def copy_text():
            secondary_window.clipboard_clear()
            secondary_window.clipboard_append(content)

        copy_button = Button(secondary_window, text="Copy to Clipboard", command=copy_text)
        copy_button.pack()
  

MyGUI()                       
