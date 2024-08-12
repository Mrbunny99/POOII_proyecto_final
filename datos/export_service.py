import datetime
from sqlalchemy.orm import Session
from datos.models import Usuario, Publicacion

def export_table(db: Session, table_name: str):
    """
    Exporta todos los registros de una tabla a un archivo.
    """
    #Aqui se obtiene la fecha actual
    date_str = datetime.datetime.now().strftime("%d-%m-%Y")
    #Crea el nombre del archivo
    file_name = f'{table_name}-{date_str}.txt'
    
    #Consulta todos los registros de la tabla especifica
    if table_name == 'usuarios':
        records = db.query(Usuario).all()
    elif table_name == 'publicaciones':
        records = db.query(Publicacion).all()
    else:
        raise ValueError("Tabla no soportada")

    #Aqui escribe los registros en el archivo
    with open(file_name, 'w') as file:
        for record in records:
            file.write(f'{record}\n')

    print(f'Exportacion completada: {file_name}')