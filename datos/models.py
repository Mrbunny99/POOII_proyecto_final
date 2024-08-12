from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    publicaciones = relationship('Publicacion', back_populates='usuario', cascade='all, delete-orphan')

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'))
    usuario = relationship('Usuario', back_populates='publicaciones')

    def __init__(self, titulo, contenido, usuario_id):
        self.titulo = titulo
        self.contenido = contenido
        self.usuario_id = usuario_id
