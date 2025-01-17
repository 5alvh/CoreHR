from tkinter import *
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
class Nominas:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.title("Nominas")
        self.root.columnconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16], weight=0) 
        self.root.geometry("1300x600")
        self.root.configure(padx=30,pady=30)
        self.codigo = 0
        self.create_nomina()
        self.root.mainloop()

    def create_nomina(self):
        Label(self.root, text="Codigo", font=("Arial", 12,"bold")).grid(row=0, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Apellidos y Nombre", font=("Arial", 12,"bold")).grid(row=0, column=1,columnspan=7, sticky="nsew",padx=20,pady=5)
        self.entri1 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,))
        self.entri2 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10))
        self.entri1.grid(row=1, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri2.grid(row=1, column=1,columnspan=7, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri2.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")


        ##Second Row##
        Label(self.root, text="Fecha Inicio", font=("Arial", 12,"bold")).grid(row=2, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Fecha Nacimiento", font=("Arial", 12,"bold")).grid(row=2, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Direccion", font=("Arial", 12,"bold")).grid(row=2, column=2,columnspan=7, sticky="nsew",padx=20,pady=5)
        self.entri3 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri4 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri5 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        self.entri3.grid(row=3, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri4.grid(row=3, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri5.grid(row=3, column=2,columnspan=7, sticky="nsew",padx=20,pady=5,ipady=5) 

        self.entri3.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri4.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri5.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")


        ####Tercera Row####
        Label(self.root, text="NIF", font=("Arial", 12,"bold")).grid(row=4, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Datos Bancarios", font=("Arial", 12,"bold")).grid(row=4, column=1,columnspan=4, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Numero afiliacion SS", font=("Arial", 12,"bold")).grid(row=4, column=5,columnspan=3, sticky="nsew",padx=20,pady=5)
        self.entri6 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri7 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri8 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        self.entri6.grid(row=5, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri7.grid(row=5, column=1,columnspan=4, sticky="nsew",padx=20,pady=5,ipady=5) 
        self.entri8.grid(row=5, column=5,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 

        self.entri6.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri7.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri8.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        ####Quinto Row####
        Label(self.root, text="Salario Bruto", font=("Arial", 12,"bold")).grid(row=8, column=0,columnspan=1, sticky="nsew",padx=20,pady=20)
        Label(self.root, text="Numero Pagas", font=("Arial", 12,"bold")).grid(row=8, column=2,columnspan=1, sticky="nsew",padx=20,pady=20)
        self.entri9 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri10 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri9.grid(row=8, column=1,columnspan=1, sticky="nsew",padx=20,pady=20,ipady=5) 
        self.entri10.grid(row=8, column=3,columnspan=1, sticky="nsew",padx=20,pady=20,ipady=5) 

        self.entri9.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri10.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        hr = Frame(self.root, height=1, bg="black") 
        hr.grid(row=9, column=0, columnspan=8, sticky="ew", padx=20,pady=(0,10))  

        ####Sexto Row####
        Label(self.root, text="SALARIO MES", font=("Arial", 12,"bold")).grid(row=10, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="%IRPF", font=("Arial", 12,"bold")).grid(row=10, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Rentencion IRPF", font=("Arial", 12,"bold")).grid(row=10, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        self.entri11 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri12 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri13 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        self.entri11.grid(row=10, column=1,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        self.entri12.grid(row=10, column=3,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        self.entri13.grid(row=10, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 

        self.entri11.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        self.entri12.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        ####Septimo Row####
        Label(self.root, text="PRORROTA PAGAS", font=("Arial", 12,"bold")).grid(row=12, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="SEG. SOCIAL", font=("Arial", 12,"bold")).grid(row=12, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="DEDUCCION SS", font=("Arial", 12,"bold")).grid(row=12, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        self.entri14 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri15 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri16 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        self.entri14.grid(row=12, column=1,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        self.entri15.grid(row=12, column=3,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        self.entri16.grid(row=12, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 

        self.entri15.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        self.mensaje =Label(self.root, text="MENSAJES VALIDACION",fg="red", font=("Arial", 12,"bold"), bd=1, relief="solid", wraplength=650)
        self.mensaje.grid(row=14, column=0,columnspan=4, sticky="nsew",padx=20,pady=10,ipady=10)
        Label(self.root, text="A PERCIBIR", font=("Arial", 12,"bold")).grid(row=14, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        self.entri17 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        self.entri17.grid(row=14, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 
        self.entri17.config(state=DISABLED, disabledbackground="#838383",disabledforeground="black")

        Button(self.root, text="Cargar Empleado",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99",command=self.cargarEmpleado).grid(row=15, column=1,columnspan=2, sticky="nsew",padx=20,pady=10)
        Button(self.root, text="CALCULAR",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99", command=self.calcular).grid(row=15, column=5,columnspan=1, sticky="nsew",padx=20,pady=10)
        Button(self.root, text="IMPRIMIR",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99", command=self.create_pdf).grid(row=15, column=6,columnspan=1, sticky="nsew",padx=20,pady=10)
    def cargarEmpleado(self):

        for entry in [self.entri2, self.entri3, self.entri4, self.entri5, self.entri6, self.entri7, self.entri8, 
                      self.entri9, self.entri10, self.entri11, self.entri12, self.entri13, self.entri14, self.entri15, self.entri16, self.entri17]:
            entry.config(state="normal")
            entry.delete(0, 'end')
            entry.config(state=DISABLED)

        self.conn = sqlite3.connect('empleados.db')
        self.cursor = self.conn.cursor()

        self.codigo = self.entri1.get()

        self.cursor.execute("SELECT COUNT(*) FROM empleados WHERE id=?", (self.codigo,))
        existe = self.cursor.fetchone()[0]

        if existe == 0:
            from tkinter import messagebox
            messagebox.showerror("Error", "No employee found with this ID.")
            self.conn.close()
            return

        self.cursor.execute("select nombre from empleados where id=?",(self.codigo,))
        nombre = self.cursor.fetchone()[0]
        self.entri2.config(state="normal")
        self.entri2.delete(0, 'end')  
        self.entri2.insert(0, str(nombre))
        self.entri2.config(state=DISABLED)

        self.cursor.execute("select fecha_inicio from empleados where id=?",(self.codigo,))
        fecha_inicio = self.cursor.fetchone()[0]
        self.entri3.config(state="normal")
        self.entri3.delete(0, 'end')  
        self.entri3.insert(0, str(fecha_inicio))
        self.entri3.config(state=DISABLED)

        self.cursor.execute("select fecha_nacimiento from empleados where id=?",(self.codigo,))
        fecha_nacimiento = self.cursor.fetchone()[0]
        self.entri4.config(state="normal")
        self.entri4.delete(0, 'end')  
        self.entri4.insert(0, str(fecha_nacimiento))
        self.entri4.config(state=DISABLED)

        self.cursor.execute("select direccion from empleados where id=?",(self.codigo,))
        direccion = self.cursor.fetchone()[0]
        self.entri5.config(state="normal")
        self.entri5.delete(0, 'end')  
        self.entri5.insert(0, str(direccion))
        self.entri5.config(state=DISABLED)

        self.cursor.execute("select nif from empleados where id=?",(self.codigo,))
        nif = self.cursor.fetchone()[0]
        self.entri6.config(state="normal")
        self.entri6.delete(0, 'end')  
        self.entri6.insert(0, str(nif))
        self.entri6.config(state=DISABLED)

        self.cursor.execute("select iban from empleados where id=?",(self.codigo,))
        iban = self.cursor.fetchone()[0]
        self.entri7.config(state="normal")
        self.entri7.delete(0, 'end')  
        self.entri7.insert(0, str(iban))
        self.entri7.config(state=DISABLED)
    
        self.cursor.execute("select afiliacion_ss from empleados where id=?",(self.codigo,))
        afiliacion_ss = self.cursor.fetchone()[0]
        self.entri8.config(state="normal")
        self.entri8.delete(0, 'end')  
        self.entri8.insert(0, str(afiliacion_ss))
        self.entri8.config(state=DISABLED)

        self.cursor.execute("select salario from empleados where id=?",(self.codigo,))
        salario_base = self.cursor.fetchone()[0]
        self.entri9.config(state="normal")
        self.entri9.delete(0, 'end')  
        self.entri9.insert(0, str(salario_base))
        self.entri9.config(state=DISABLED)

        self.cursor.execute("select pagas_extra from empleados where id=?",(self.codigo,))
        pagas_extra = self.cursor.fetchone()[0]
        self.entri10.config(state="normal")
        self.entri10.delete(0, 'end')  
        self.entri10.insert(0, str(pagas_extra))
        self.entri10.config(state=DISABLED)

        self.cursor.execute("select irpf from empleados where id=?",(self.codigo,))
        irpf = int(self.cursor.fetchone()[0]) 
        self.entri12.config(state="normal")
        self.entri12.delete(0, 'end')  
        self.entri12.insert(0, str(irpf))
        self.entri12.config(state=DISABLED)

        self.cursor.execute("select seg_social from empleados where id=?",(self.codigo,))
        seg_social = int(self.cursor.fetchone()[0]) 
        self.entri15.config(state="normal")
        self.entri15.delete(0, 'end')  
        self.entri15.insert(0, str(seg_social))
        self.entri15.config(state=DISABLED)
        prorrata_pagas = (salario_base * pagas_extra) / 12
        self.salario_mensual = salario_base + prorrata_pagas
        self.entri11.config(state="normal")
        self.entri11.delete(0, 'end')
        self.entri11.insert(0, f"{self.salario_mensual:.2f}")
        self.entri11.config(state=DISABLED)
        self.conn.close()
        
    def calcular(self):
        
        if self.codigo ==0:
            self.mensaje.config(text="PRIEMRO CARGA UN EMPLEADO")
            return
        
        self.conn = sqlite3.connect('empleados.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select salario from empleados where id=?",(self.codigo,))
        salario_base = self.cursor.fetchone()[0]


        self.cursor.execute("select pagas_extra from empleados where id=?",(self.codigo,))
        pagas_extra = self.cursor.fetchone()[0]

        self.cursor.execute("select irpf from empleados where id=?",(self.codigo,))
        irpf = int(self.cursor.fetchone()[0]) 

        self.cursor.execute("select seg_social from empleados where id=?",(self.codigo,))
        seg_social = int(self.cursor.fetchone()[0])

        prorrata_pagas = (salario_base * pagas_extra) / 12
        retencion_irpf = self.salario_mensual * irpf / 100
        deduccion_ss = self.salario_mensual * seg_social / 100
        a_percibir = self.salario_mensual - retencion_irpf - deduccion_ss

        self.entri14.config(state="normal")
        self.entri14.delete(0, 'end')
        self.entri14.insert(0, f"{prorrata_pagas:.2f}")
        self.entri14.config(state=DISABLED)
        

        self.entri13.config(state="normal")
        self.entri13.delete(0, 'end')
        self.entri13.insert(0, f"{retencion_irpf:.2f}")
        self.entri13.config(state=DISABLED)

        self.entri16.config(state="normal")
        self.entri16.delete(0, 'end')
        self.entri16.insert(0, f"{deduccion_ss:.2f}")
        self.entri16.config(state=DISABLED)

        self.entri17.config(state="normal")
        self.entri17.delete(0, 'end')
        self.entri17.insert(0, f"{a_percibir:.2f}")
        self.entri17.config(state=DISABLED)
        self.conn.close()
        self.mensaje.config(text="CALCULANDO...")

    def create_pdf(self):
        if self.codigo ==0:
            self.mensaje.config(text="PRIEMRO CARGA UN EMPLEADO")
            return
        
        pdf = canvas.Canvas(f"Nomina_{self.entri2.get()}.pdf", pagesize=letter)
        pdf.setFont("Helvetica-Bold", 16)


        pdf.drawCentredString(300, 780, "Nómina de Empleado")  

        pdf.setFont("Helvetica", 12)
        y = 700  

        pdf.setStrokeColor(colors.grey)
        pdf.line(50, y + 20, 550, y + 20)

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Información del Empleado:")
        pdf.setFont("Helvetica", 12)
        y -= 20
        pdf.drawString(100, y, f"Nombre: {self.entri2.get()}")
        y -= 20
        pdf.drawString(100, y, f"Fecha Inicio: {self.entri3.get()}")
        y -= 20
        pdf.drawString(100, y, f"Fecha Nacimiento: {self.entri4.get()}")
        y -= 20
        pdf.drawString(100, y, f"Direccion: {self.entri5.get()}")
        y -= 20
        pdf.drawString(100, y, f"NIF: {self.entri6.get()}")

        y -= 40
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Detalles Financieros:")
        pdf.setFont("Helvetica", 12)
        y -= 20
        pdf.drawString(100, y, f"Datos Bancarios: {self.entri7.get()}")
        y -= 20
        pdf.drawString(100, y, f"Numero SS: {self.entri8.get()}")
        y -= 20
        pdf.drawString(100, y, f"Salario Bruto: {self.entri9.get()}")
        y -= 20
        pdf.drawString(100, y, f"Numero Pagas: {self.entri10.get()}")
        y -= 20
        pdf.drawString(100, y, f"Salario Mensual: {self.entri11.get()}")

        y -= 40
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Deducciones:")
        pdf.setFont("Helvetica", 12)
        y -= 20
        pdf.drawString(100, y, f"%IRPF: {self.entri12.get()}")
        y -= 20
        pdf.drawString(100, y, f"Retención IRPF: {self.entri13.get()}")
        y -= 20
        pdf.drawString(100, y, f"Prorrata Pagas: {self.entri14.get()}")
        y -= 20
        pdf.drawString(100, y, f"Seg. Social: {self.entri15.get()}")
        y -= 20
        pdf.drawString(100, y, f"Deducción SS: {self.entri16.get()}")

        y -= 40
        pdf.setFont("Helvetica-Bold", 14)
        pdf.setFillColor(colors.darkgreen)
        pdf.drawString(50, y, f"A Percibir: {self.entri17.get()}")

        y -= 50
        pdf.setFont("Helvetica-Oblique", 10)
        pdf.setFillColor(colors.grey)
        pdf.drawString(50, y, "Documento generado automáticamente")
        pdf.drawRightString(550, y, "Gracias por confiar en nuestra empresa.")

        pdf.save()
        self.mensaje.config(text="PDF creado con estilo.")