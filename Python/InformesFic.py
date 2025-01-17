from tkinter import *
import sqlite3
class Informes:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.title("Informes")
        self.root.columnconfigure([0, 1, 2, 3], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1) 
        self.root.configure(padx=50,pady=50)
        self.root.geometry("1500x600")
        self.crea_informes()
        self.setInfos()
        self.root.mainloop()


    def crea_informes(self):
        Label(self.root, text="EMPLEADOS\nALTA", font=("Arial",15,"bold"), pady=10).grid(row=0, column=0)
        Label(self.root, text="EMPLEADOS\nBAJA", font=("Arial",15,"bold"), pady=10).grid(row=0, column=1)
        Label(self.root, text="MEDIA\nEDADES", font=("Arial",15,"bold"), pady=10).grid(row=0, column=2)
        Label(self.root, text="RETRIBUCION\nMEDIA", fg="Blue", font=("Arial",15,"bold"), pady=10).grid(row=0, column=3)

        self.entri1 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        self.entri2 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        self.entri3 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        self.entri4 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",18))

        self.entri1.grid(row=1, column=0,ipady=25,ipadx=25)
        self.entri2.grid(row=1, column=1,ipady=25,ipadx=25)
        self.entri3.grid(row=1, column=2,ipady=25,ipadx=25)
        self.entri4.grid(row=1, column=3,ipady=30,ipadx=40)

        self.entri1.config(state="readonly")
        self.entri2.config(state="readonly")
        self.entri3.config(state="readonly")
        self.entri4.config(state="readonly")

        ###Segunda Row####
        Label(self.root, text="%MUJERES", font=("Arial",15),pady=20).grid(row=2, column=0)
        Label(self.root, text="%MUJERES", font=("Arial",15),pady=20).grid(row=2, column=1)
        Label(self.root, text="MUJERES", font=("Arial",15),pady=20).grid(row=2, column=2)
        Label(self.root, text="MUJERES", fg="#94B8FF", font=("Arial",15,"bold"),pady=20).grid(row=2, column=3)

        self.entri5 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri6 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri7 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri8 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")

        self.entri5.grid(row=3, column=0,ipady=25,ipadx=25)
        self.entri6.grid(row=3, column=1,ipady=25,ipadx=25)
        self.entri7.grid(row=3, column=2,ipady=25,ipadx=25)
        self.entri8.grid(row=3, column=3,ipady=25,ipadx=25)


        self.entri5.config(state="readonly")
        self.entri6.config(state="readonly")
        self.entri7.config(state="readonly")
        self.entri8.config(state="readonly")

        ###Segunda Row####
        Label(self.root, text="%HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=0)
        Label(self.root, text="%HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=1)
        Label(self.root, text="HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=2)
        Label(self.root, text="HOMBRES", fg="#94B8FF", font=("Arial",15,"bold"),pady=20).grid(row=4, column=3)

        self.entri9 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri10 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri11 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")
        self.entri12 =Entry(self.root,bd=1, relief="solid", font=("Arial",15), justify="center")

        self.entri9.grid(row=5, column=0,ipady=25,ipadx=25)
        self.entri10.grid(row=5, column=1,ipady=25,ipadx=25)
        self.entri11.grid(row=5, column=2,ipady=25,ipadx=25)
        self.entri12.grid(row=5, column=3,ipady=25,ipadx=25)


        self.entri9.config(state="readonly")
        self.entri10.config(state="readonly")
        self.entri11.config(state="readonly")
        self.entri12.config(state="readonly")

    def setInfos(self):
        try:
            ###EMPLEADOS
            self.conn = sqlite3.connect('empleados.db')
            self.cursor = self.conn.cursor() 
            self.cursor.execute('SELECT COUNT(*) FROM empleados')
            x = self.cursor.fetchone()[0]
            self.entri1.config(state="normal")
            self.entri1.delete(0, 'end')  
            self.entri1.insert(0, str(x))
            self.entri1.config(state=DISABLED)
            ####%MUJERES
            self.cursor.execute('''
                    SELECT (COUNT(CASE WHEN genero = 'm' THEN 1 END) * 100.0) / COUNT(*) 
                    FROM empleados
                ''')
            percentage_m = self.cursor.fetchone()[0]
            self.entri5.config(state="normal")
            self.entri5.delete(0, 'end')  
            self.entri5.insert(0, str(percentage_m)+"%")
            self.entri5.config(state=DISABLED)
            ####%HOMBRES
            self.cursor.execute('''
                    SELECT (COUNT(CASE WHEN genero = 'h' THEN 1 END) * 100.0) / COUNT(*) 
                    FROM empleados
                ''')
            percentage_h = self.cursor.fetchone()[0]
            self.entri9.config(state="normal")
            self.entri9.delete(0, 'end')  
            self.entri9.insert(0, str(percentage_h)+"%")
            self.entri9.config(state=DISABLED)

            ###BAJAS
            self.cursor.execute('SELECT COUNT(*) FROM bajas')
            y = self.cursor.fetchone()[0]
            self.entri2.config(state="normal")
            self.entri2.delete(0, 'end')  
            self.entri2.insert(0, str(y))
            self.entri2.config(state=DISABLED)
            ####%MUJERES
            self.cursor.execute('''
                    SELECT (COUNT(CASE WHEN genero = 'm' THEN 1 END) * 100.0) / COUNT(*) 
                    FROM bajas
                ''')
            percentage_mb = self.cursor.fetchone()[0]
            self.entri6.config(state="normal")
            self.entri6.delete(0, 'end')  
            self.entri6.insert(0, str(percentage_mb)+"%")
            self.entri6.config(state=DISABLED)
            ####%HOMBRES
            self.cursor.execute('''
                    SELECT (COUNT(CASE WHEN genero = 'h' THEN 1 END) * 100.0) / COUNT(*) 
                    FROM bajas
                ''')
            percentage_hb = self.cursor.fetchone()[0]
            self.entri10.config(state="normal")
            self.entri10.delete(0, 'end')  
            self.entri10.insert(0, str(percentage_hb)+"%")
            self.entri10.config(state=DISABLED)
        #################AGES########################33
            self.cursor.execute('''
                SELECT AVG(
                    CAST(STRFTIME('%Y', 'now') AS INTEGER) - CAST(STRFTIME('%Y', 
                        SUBSTR(fecha_nacimiento, 7, 4) || '-' || SUBSTR(fecha_nacimiento, 4, 2) || '-' || SUBSTR(fecha_nacimiento, 1, 2)
                    ) AS INTEGER)
                )
                FROM empleados
                WHERE fecha_nacimiento IS NOT NULL;
            ''')
            total_avg_age = self.cursor.fetchone()[0]
            self.entri3.config(state="normal")
            self.entri3.delete(0, 'end')  
            self.entri3.insert(0, str(total_avg_age))
            self.entri3.config(state=DISABLED)
        ################MUJEERES######################3
            self.cursor.execute('''
                    SELECT AVG(
                        CAST(STRFTIME('%Y', 'now') AS INTEGER) - CAST(STRFTIME('%Y', 
                            SUBSTR(fecha_nacimiento, 7, 4) || '-' || SUBSTR(fecha_nacimiento, 4, 2) || '-' || SUBSTR(fecha_nacimiento, 1, 2)
                        ) AS INTEGER)
                    )
                    FROM empleados 
                    WHERE genero = 'm' AND fecha_nacimiento IS NOT NULL;
                ''')
            avg_age_h = self.cursor.fetchone()[0]
            self.entri7.config(state="normal")
            self.entri7.delete(0, 'end')  
            self.entri7.insert(0, str(avg_age_h))
            self.entri7.config(state=DISABLED)
            ################HOMBRES######################3
            self.cursor.execute('''
                    SELECT AVG(
                        CAST(STRFTIME('%Y', 'now') AS INTEGER) - CAST(STRFTIME('%Y', 
                            SUBSTR(fecha_nacimiento, 7, 4) || '-' || SUBSTR(fecha_nacimiento, 4, 2) || '-' || SUBSTR(fecha_nacimiento, 1, 2)
                        ) AS INTEGER)
                    )
                    FROM empleados 
                    WHERE genero = 'h' AND fecha_nacimiento IS NOT NULL;
                ''')
            avg_age_m = self.cursor.fetchone()[0]
            self.entri11.config(state="normal")
            self.entri11.delete(0, 'end')  
            self.entri11.insert(0, str(avg_age_m))
            self.entri11.config(state=DISABLED)

            ########SALARIO
            self.cursor.execute('''
                SELECT AVG(salario)
                FROM empleados
                WHERE salario IS NOT NULL;
            ''')
            total_avg_salario = self.cursor.fetchone()[0]
            self.entri4.config(state="normal")
            self.entri4.delete(0, 'end')  
            self.entri4.insert(0, str(total_avg_salario))
            self.entri4.config(state=DISABLED)

            ###SALARIO MUJERES
            self.cursor.execute('''
                SELECT AVG(salario)
                FROM empleados 
                WHERE genero = 'm' AND salario IS NOT NULL;
            ''')
            avg_salario_m = self.cursor.fetchone()[0]
            self.entri8.config(state="normal")
            self.entri8.delete(0, 'end')  
            self.entri8.insert(0, str(avg_salario_m))
            self.entri8.config(state=DISABLED)

            ###SALARIO HOMBRES
            self.cursor.execute('''
                SELECT AVG(salario)
                FROM empleados 
                WHERE genero = 'h' AND salario IS NOT NULL;
            ''')
            avg_salario_h = self.cursor.fetchone()[0]
            self.entri12.config(state="normal")
            self.entri12.delete(0, 'end')  
            self.entri12.insert(0, str(avg_salario_h))
            self.entri12.config(state=DISABLED)

        except sqlite3.Error as e:
            print(f"Error: {e}")


        finally:
            self.conn.close()