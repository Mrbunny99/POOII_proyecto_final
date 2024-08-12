from sqlalchemy.orm import Session
from datos.models import Publicacion
from datos.base_service import BaseDatosServices

class PublicacionService(BaseDatosServices):
    """
    Clase que implementa los métodos CRUD para la entidad Publicacion.
    """

    def insert(self, db: Session, entity: Publicacion):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, entity_id: int, new_data: dict):
        publicacion = db.query(Publicacion).filter(Publicacion.id == entity_id).first()
        if publicacion:
            if 'titulo' in new_data:
                publicacion.titulo = new_data['titulo']
            if 'contenido' in new_data:
                publicacion.contenido = new_data['contenido']
            db.commit()
            db.refresh(publicacion)
        return publicacion

    def delete(self, db: Session, entity_id: int):
        publicacion = db.query(Publicacion).filter(Publicacion.id == entity_id).first()
        if publicacion:
            db.delete(publicacion)
            db.commit()
        return publicacion

    def select_all(self, db: Session):
        return db.query(Publicacion).all()

    def select_by_id(self, db: Session, entity_id: int):
        return db.query(Publicacion).filter(Publicacion._id == entity_id).first()
