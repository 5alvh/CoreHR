from datetime import datetime
from tkinter import *
import sqlite3
import re
from tkinter import messagebox

class Bajas:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Bajas")
        self.root.columnconfigure([0, 1], weight=1)
        self.root.rowconfigure([0, 1, 2, 3], weight=0)
        self.root.geometry("500x350")
        self.root.resizable(1,0)
        self.create_bajas()
        self.root.mainloop()
        
    def create_bajas(self):
        Label(self.root, text="Codigo Empleado", font=("Arial",12, "bold")).grid(row=0, column=0, columnspan=1, sticky="nsew",pady=(50,10))
        self.entri1= Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri1.grid(row=1, column=0, columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5)

        Label(self.root, text="Fecha Baja", font=("Arial",12, "bold")).grid(row=0, column=1, columnspan=1, sticky="nsew",pady=(50,10))
        self.entri2= Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri2.grid(row=1, column=1, columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5)

        self.mensaje = Label(self.root, text="MENSAJES VALIDACION", font=("Arial",12, "bold"),fg="red", bd=1, relief="solid")
        self.mensaje.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=60,pady=20,ipady=20)

        Button(self.root, text="Confirmar", bd=1, relief="solid",background="#FFFF99", font=("Arial",12, "bold"), command=self.baja_empleado).grid(row=3, column=0, columnspan=2,pady=5,ipadx=30,ipady=10)
    
    def baja_empleado(self):
        try:
            self.conn = sqlite3.connect('empleados.db')
            self.cursor = self.conn.cursor()

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS bajas (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    nif TEXT,
                    fecha_baja TEXT,
                    genero TEXT
                )
            ''')

            codigo_empleado = self.entri1.get()
            fecha_baja = self.entri2.get()
            if not self.validate_fecha_baja(fecha_baja):
                return
            
            if not codigo_empleado or not fecha_baja:
                self.mensaje.config(text="NO VALIDO", fg="red")
                return

            self.cursor.execute("SELECT * FROM empleados WHERE id=?", (codigo_empleado,))
            empleado = self.cursor.fetchone()

            if empleado:

                empleado_id = empleado[0]
                empleado_nombre = empleado[1]
                empleado_nif = empleado[5]
                empleado_genero = empleado[8]

                self.cursor.execute('''
                    INSERT INTO bajas (id, nombre, nif, fecha_baja, genero)
                    VALUES (?, ?, ?, ?, ?)
                ''', (empleado_id, empleado_nombre, empleado_nif, fecha_baja, empleado_genero))

                self.cursor.execute("DELETE FROM empleados WHERE id=?", (codigo_empleado,))

                self.conn.commit()

                self.mensaje.config(text=f"Empleado con código {codigo_empleado} ha sido eliminado de la base de datos.", fg="green")
            else:

                self.mensaje.config(text=f"No se encontró el empleado con código {codigo_empleado}.", fg="red")
        
        finally:
            
            if self.conn:
                self.conn.close()

    def validate_fecha_baja(self,fecha_baja):

        if not re.match(r"^\d{2}-\d{2}-\d{4}$", fecha_baja):
            self.mensaje.config(text="La fecha debe estar en el formato dd-mm-yyyy")
            return False
        
        return True
            