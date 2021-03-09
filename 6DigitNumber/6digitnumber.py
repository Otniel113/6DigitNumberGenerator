from tkinter import *
import random

#Program utama
main = Tk()

#Function jika button di-klik
def dapat_kode():
    kode = random.randint(1,400000)         #Random Angka
    ent.delete(0, END)                      #Mengosongkan kotak Entry
    ent.insert(END, str(kode))              #Menulis kotak Entry
 
#Menulis label
label = Label(main, text="Selamat Datang di 6 Digit Number Generator \n Tekan 'Generate' untuk merandom kode nuklir")
label.pack()

#Membuat button
tombol = Button(main, text="Generate", command = dapat_kode)
tombol.pack()

#Membuat kotak Entry
ent = Entry(main)
ent.pack()

#Program loop (jalan) terus sampai diclose
main.mainloop()