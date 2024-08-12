import threading
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from datos.models import Base
from datos.database import engine

class HistorialImportacion(Base):
    """
    Clase que representa la tabla 'historial_importacion' en la base de datos.
    """
    __tablename__ = 'historial_importacion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    accion = Column(String(255))

Base.metadata.create_all(engine)

def import_historial(db: Session):
    """
    Importa todas las filas de 'historial.txt' y las guarda en la tabla 'historial_importacion' utilizando hilos.
    """
    # Leer todas las líneas del archivo 'historial.txt'
    with open('historial.txt', 'r') as file:
        lines = file.readlines()

    def insert_line(line):
        # Crear un nuevo registro de HistorialImportacion
        accion = HistorialImportacion(accion=line.strip())
        # Agregar el registro a la sesión de la base de datos
        db.add(accion)
        # Confirmar la transacción
        db.commit()

    # Crear una lista para almacenar los hilos
    threads = []
    for line in lines:
        # Crear un hilo para cada línea del archivo
        thread = threading.Thread(target=insert_line, args=(line,))
        threads.append(thread)
        # Iniciar el hilo
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
