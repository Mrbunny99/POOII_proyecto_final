from sqlalchemy.orm import Session
from models import Usuario, Publicacion

def crear_usuario(db: Session, nombre: str):
    nuevo_usuario = Usuario(nombre=nombre)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def leer_usuarios(db: Session):
    return db.query(Usuario).all()

def actualizar_usuario(db: Session, nombre_actual: str, nuevo_nombre: str):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre_actual).first()
    if usuario:
        usuario.nombre = nuevo_nombre
        db.commit()
        db.refresh(usuario)
    return usuario

def eliminar_usuario(db: Session, nombre: str):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario
