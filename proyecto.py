""" PROGRAMACION III - Ing. Computacion - UNRN
Proyecto Integrador Final 2023 - Carriqueo, Mariela-  Linares, Lucas - Velazquez, Laura """

  
# Creacion de la base de datos
file = "Sqlite3.db"

from itertools import combinations_with_replacement
import sqlite3

  #Conexion a sqlite
conn = sqlite3.connect('Sqlite3.db')
  # Creacion del objeto cursor a través del método
cursor = conn.cursor()

  # Creacion de las tablas
tabla1='''CREATE TABLE PRESTAMOS (
    ID INTEGER PRIMARY KEY,
    FechaPrestamos DATE NOT NULL, 
    FechaDevolucion DATE NOT NULL,
    Estado CHAR(50) NOT NULL,
    USUARIO_ID INTEGER NOT NULL REFERENCES USUARIO(ID_USUARIO),
    EMPLEADO_ID INTEGER NOT NULL REFERENCES EMPLEADO(ID_EMPLEADO),
    EVENTO_ID INTEGER NOT NULL REFERENCES EVENTO(ID_EVENTO),
    SUCURSAL_ID INTEGER NOT NULL REFERENCES SUCURSAL(ID_SUCURSAL)
    )'''

cursor.execute(tabla1)
print("Tabla de PRESTAMOS creada")


tabla2='''CREATE TABLE PRESTAMO_LIBRO(
    ID_PRESTAMO INTEGER  REFERENCES PRESTAMOS(ID_PRESTAMO),
    ID_LIBRO INTEGER REFERENCES LIBRO(ID_LIBRO),
    PRIMARY KEY (ID_PRESTAMO, ID_LIBRO)
    )'''
    
cursor.execute(tabla2)
print("Tabla de PRESTAMOSLIBRO creada")


  # Alta de prestamo

 def alta_prestamo(self, ID, FechaPrestamo, FechaDevolucion, Estado, USUARIO_ID, EMPLEADO_ID, EVENTO_ID, SUCURSAL_ID, LIBRO_ID):
    try:
        self.cursor.execute("""
        INSERT INTO PRESTAMOS (ID, FechaPrestamo, FechaDevolucion, Estado, USUARIO_ID, EMPLEADO_ID, EVENTO_ID, SUCURSAL_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",(ID, FechaPrestamo, FechaDevolucion, Estado, USUARIO_ID, EMPLEADO_ID, EVENTO_ID, SUCURSAL_ID))
        self.conn.commit()

        self.cursor.execute("""
        INSERT INTO PRESTAMO_LIBRO (ID, LIBRO_ID)
        VALUES (%s, %s), (%s, %s) """, (ID,LIBRO_ID[0],ID,LIBRO_ID[1]))
        
        self.conn.commit()

        return True
    except sqlite3.IntegrityError:
        print("Error: No se pudo cargar.")
        return False

            

  # Modificación de prestamo            
  
  def modificacion_prestamo(self, ID):
        try:
          self.cursor.execute("""
          UPDATE FROM PRESTAMO SET FechaDevolucion = (?)    WHERE ID= (?) """, ("5/12/2023", "4")
          )
          
          self.conn.commit()
          
          return True
        except sqlite3.IntegrityError:
          print("Error: no se pudo modificar el registro")

  # Baja de prestamo
  
def baja_prestamo(self, ID):
        try:
            self.cursor.execute("""
            DELETE FROM PRESTAMO WHERE ID = %s """,(ID))
            
            self.conn.commit()

            return True
        except sqlite3.IntegrityError:
          print("Error: No se pudo borrar.")
          
          
# Commit cambios en la base de datos
conn.commit()

# Se cierra conexion
conn.close()
