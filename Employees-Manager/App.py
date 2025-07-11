from tkinter import *
from AltasFich import Altas 
from BajasFic import Bajas
from InformesFic import Informes
from NominasFich import Nominas


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("APP")

        self.root.columnconfigure([0, 1], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3], weight=1) 
        try:
            image = PhotoImage(file="Face.png").subsample(8)
        except TclError:
            print("Error: No se pudo cargar la imagen 'Face.png'.")
            image = None 
        image_label = Label(self.root, image=image)
        image_label.grid(row=1, column=0, columnspan=2, sticky="nsew") 

        self.root.geometry("500x500")
        self.root.resizable(0, 0)

        self.crearApp()

        self.root.mainloop()
        
    def crearApp(self):

        header_label = Label(self.root, text="Nominator+", font=("Arial", 16))
        header_label.grid(row=0, column=0, columnspan=2)  

        button1 = Button(self.root, text="ALTAS")
        button2 = Button(self.root, text="BAJAS")
        button3 = Button(self.root, text="INFORMES")
        button4 = Button(self.root, text="NOMINAS")


        button1.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=self.launch_altas)
        button2.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=self.launch_bajas)
        button3.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=self.launch_informes)
        button4.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=self.launch_nominas)

        button1.grid(row=2, column=0,ipadx=75,ipady=10) 
        button2.grid(row=2, column=1,ipadx=75,ipady=10) 
        button3.grid(row=3, column=0,ipadx=60,ipady=10)  
        button4.grid(row=3, column=1,ipadx=60,ipady=10) 

    def launch_altas(self):
        Altas(self.root)

    def launch_bajas(self):
        Bajas(self.root)
    
    def launch_informes(self):
        Informes(self.root)

    def launch_nominas(self):
        Nominas(self.root)


