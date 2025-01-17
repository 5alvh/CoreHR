from tkinter import *
from tkinter import messagebox
from funcionesPy import validar
from datetime import datetime
import re
import sqlite3


class Altas:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Altas")
        self.root.columnconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10], weight=0) 
        self.root.resizable(1, 0)
        self.crear_altas()
        self.valid = validar()
        self.root.mainloop()
        
    def crear_altas(self):
        ####Primera Row####
        Label(self.root, text="Apellidos y Nombre", font=("Arial", 12,"bold")).grid(row=0, column=0,columnspan=8, sticky="nsew",padx=20,pady=5)
        self.entri1 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri1.grid(row=1, column=1,columnspan=6, sticky="nsew",padx=20,pady=5,ipady=5) 

    
        ####Segunda Row####
        Label(self.root, text="Fecha Inicio", font=("Arial", 12,"bold")).grid(row=2, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Fecha Nacimiento", font=("Arial", 12,"bold")).grid(row=2, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Direccion", font=("Arial", 12,"bold")).grid(row=2, column=3,columnspan=4, sticky="nsew",padx=20,pady=5)
        self.entri2 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri3 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri4 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri2.grid(row=3, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri3.grid(row=3, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri4.grid(row=3, column=3,columnspan=4, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Tercera Row####
        Label(self.root, text="NIF/NIE", font=("Arial", 12,"bold")).grid(row=4, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Datos Bancarios", font=("Arial", 12,"bold")).grid(row=4, column=2,columnspan=3, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Numero afiliacion SS", font=("Arial", 12,"bold")).grid(row=4, column=5,columnspan=2, sticky="nsew",padx=20,pady=5)
        self.entri5 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri6 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri7 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri5.grid(row=5, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri6.grid(row=5, column=2,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri7.grid(row=5, column=5,columnspan=2, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Cuarta Row####
        Label(self.root, text="Genero: H/M", font=("Arial", 12,"bold")).grid(row=6, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Departarmento", font=("Arial", 12,"bold")).grid(row=6, column=2,columnspan=3, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Puesto", font=("Arial", 12,"bold")).grid(row=6, column=5,columnspan=2, sticky="nsew",padx=20,pady=5)
        self.entri8 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri9 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri10 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri8.grid(row=7, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri9.grid(row=7, column=2,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri10.grid(row=7, column=5,columnspan=2, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Quinto Row####
        Label(self.root, text="Telefono", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Salario Mensual", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=3,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="IRPF", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        self.entri11 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri12 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri13 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"), justify="center")
        self.entri11.grid(row=8, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri12.grid(row=8, column=4,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri13.grid(row=8, column=6,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 


        ####Sexto Row####
        Label(self.root, text="Email", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Pagas Extra", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=3,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Seg. Social", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        self.entri14 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri15 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        self.entri16 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"), justify="center")
        self.entri14.grid(row=9, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri15.grid(row=9, column=4,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri16.grid(row=9, column=6,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Septimo Row####
        self.mensaje = Label(self.root, text="MENSAJES VALIDACION",fg="red", font=("Arial", 12,"bold"), bd=1, relief="solid")
        self.mensaje.grid(row=10, column=1,columnspan=4,rowspan=2, sticky="nsew",padx=20,pady=10,ipady=10)
        Button(self.root, text="Guardar", bd=1, relief="solid", background="#FFFF99", font=("Arial",12, "bold"),command=self.check_entry).grid(row=10, column=5,columnspan=2, rowspan=1,sticky="nsew",padx=20,pady=5,ipady=10)

    def check_entry(self):
        print(self.validate())
        entries = [self.entri1, self.entri2, self.entri3, self.entri4, self.entri5, self.entri6,
                   self.entri7, self.entri8, self.entri9, self.entri10, self.entri11, self.entri12,
                   self.entri13, self.entri14, self.entri15, self.entri16]
        
        for i, entry in enumerate(entries, 1): 
            if entry.get().strip() == "":
                messagebox.showerror(f"Entry {i} NO PUEDE ESTAR VACIA!")
                entry.config(bg="red")
                break
            else:
                entry.config(bg="white")

        if all(entry.get().strip() != "" for entry in entries) and self.validate() == True:
            id = self.guardarEnBasesDeDatos()
            messagebox.showinfo("Success", "Empleado Regitrado con exito!")
            self.mensaje.config(text=f"ID DE NUEVO EMPLEADO REGISTRADO: {id}",fg="green")

            
    def guardarEnBasesDeDatos(self):
        
        self.conn = sqlite3.connect('empleados.db') 
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                fecha_inicio TEXT,
                fecha_nacimiento TEXT,
                direccion TEXT,
                nif TEXT,
                iban TEXT,
                afiliacion_ss TEXT,
                genero TEXT,
                departamento TEXT,
                puesto TEXT,
                telefono TEXT,
                salario REAL,
                irpf REAL,
                email TEXT,
                pagas_extra INTEGER,
                seg_social REAL
            )
        ''')

        nombre = self.entri1.get().strip()
        fecha_inicio = self.entri2.get().strip()
        fecha_nacimiento = self.entri3.get().strip()
        direccion = self.entri4.get().strip()
        nif = self.entri5.get().strip()
        iban = self.entri6.get().strip()
        afiliacion_ss = self.entri7.get().strip()
        genero = self.entri8.get().strip()
        departamento = self.entri9.get().strip()
        puesto = self.entri10.get().strip()
        telefono = self.entri11.get().strip()
        salario = float(self.entri12.get().strip())
        irpf = float(self.entri13.get().strip())
        email = self.entri14.get().strip()
        pagas_extra = int(self.entri15.get().strip())
        seg_social = float(self.entri16.get().strip())
        
        self.cursor.execute('''
            INSERT INTO empleados (
                nombre, fecha_inicio, fecha_nacimiento, direccion, nif, iban, afiliacion_ss,
                genero, departamento, puesto, telefono, salario, irpf, email, pagas_extra, seg_social
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, fecha_inicio, fecha_nacimiento, direccion, nif, iban, afiliacion_ss,
            genero, departamento, puesto, telefono, salario, irpf, email, pagas_extra, seg_social))

        self.conn.commit()
        
        new_id = self.cursor.lastrowid

        self.conn.close()
        
        return new_id
####################################################################################################################################3
    def validate(self):
        ###NOMBRE COMPLETO VALIDAR
        nombreCompleto = self.entri1.get().replace(" ", "")
        if not nombreCompleto.isalpha():
            mensaje = self.mensaje
            mensaje.config(text="Nombre contiene solo alfabetos",fg="red")
            return False
        elif len(nombreCompleto) < 5 or len(nombreCompleto) > 50:
            mensaje = self.mensaje
            mensaje.config(text="El campo de nombre no puede estar vacío",fg="red")
            return False
        
        
        ##FECHA INICIO VALIDACION 
        fechaInicio = self.entri2.get().replace(" ", "")
        if not self.validar_fecha_inicio(fechaInicio):
            mensaje = self.mensaje
            mensaje.config(text="Fecha no valida\n La forma correcta es: dd-mm-aa",fg="red")
            return False
        
        ##FECHA NACIMIENTO VALIDACION 
        fechaNacimiento = self.entri3.get()
        if not self.validar_fecha_nacimiento(fechaNacimiento):
            mensaje = self.mensaje
            mensaje.config(text="Fecha no valida\nLa forma correcta es: dd-mm-aa\nFecha no puede ser en el futuro",fg="red")
            return False
        
        ##Direccion
        direccion = self.entri4.get().replace(" ", "")
        if len(direccion) < 10 or len(direccion) > 100:
            mensaje = self.mensaje
            mensaje.config(text="Direccion contiene al menos 10 caracteres",fg="red")
            return False

        nife = self.entri5.get().replace(" ", "")
        if not self.valid.validarNIE(nife) and not self.valid.validarNIF(nife):
            mensaje = self.mensaje
            mensaje.config(text="NIF/ NIE NO VALIDO",fg="red")
            return False
        
        datosBancarios = self.entri6.get()
        if not self.valid.validar_iban(datosBancarios):
            mensaje = self.mensaje
            mensaje.config(text="IBAN NO VALIDO",fg="red")
            return False
        
        numeroAfiliacionSS = self.entri7.get()
        if not self.valid.validarNAF(numeroAfiliacionSS):
            mensaje = self.mensaje
            mensaje.config(text="NAF NO VALIDO",fg="red")
            return False
        
        genero = self.entri8.get().replace(" ", "")
        if not genero.lower() == "h" and not genero.lower() == "m":
            mensaje = self.mensaje
            mensaje.config(text="CAMPO GENERO NO VALIDO\nH/M",fg="red")
            return False
        
        departamento = self.entri9.get().replace(" ", "")
        if len(departamento) < 2:
            mensaje = self.mensaje
            mensaje.config(text="DEPARTAMENTO NO VALIDO",fg="red")
            return False
        
        puesto = self.entri10.get().replace(" ", "")
        if len(puesto) < 3:
            mensaje = self.mensaje
            mensaje.config(text="PUESTO NO VALIDO",fg="red")
            return False

        telefono = self.entri11.get().replace(" ", "")
        if len(telefono) < 9 or not telefono.isdigit():
            mensaje = self.mensaje
            mensaje.config(text="TELEFONO DE 9 DIGITOS, SIN +",fg="red")
            return False
        
        salarioMensual = self.entri12.get().replace(" ", "")
        if len(salarioMensual) < 2 or not salarioMensual.isdigit():
            mensaje = self.mensaje
            mensaje.config(text="SALARIO NO VALIDO",fg="red")
            return False
        
        irpf = self.entri13.get().replace(" ", "")
        if not self.is_decimal(irpf) or len(irpf) == 0:
            mensaje = self.mensaje
            mensaje.config(text="IRPF NO VALIDO",fg="red")
            return False

        email = self.entri14.get()
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            mensaje = self.mensaje
            mensaje.config(text="EMAIL NO VALIDO",fg="red")
            return False
            

        pagasEstras = self.entri15.get().replace(" ", "")
        if not pagasEstras.isdigit():
            mensaje = self.mensaje
            mensaje.config(text="PAGAS EXTRAS NO VALIDO",fg="red")
            return False
        
        
        
        segSocial = self.entri16.get().replace(" ", "")
        if not self.is_decimal(segSocial) or len(irpf) == 0:
            mensaje = self.mensaje
            mensaje.config(text="NUM SEG SOCIAL NO VALIDO",fg="red")
            return False
        
        return True
    def validar_fecha_inicio(self, fecha):
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            return True 
        except ValueError:
            return False

    def validar_fecha_nacimiento(self, fecha):
        try:
            if datetime.strptime(fecha, "%d-%m-%Y") > datetime.now():
                return False  
            return True
        except ValueError:
            return False
        
    def is_decimal(self,value):
        try: 
            float(value)
            return True
        except ValueError:
            return False

        
