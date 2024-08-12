from sqlalchemy.orm import Session
from datos.models import Usuario
from datos.base_service import BaseDatosServices

class UsuarioService(BaseDatosServices):
    """
    Clase que implementa los métodos CRUD para la entidad Usuario.
    """

    def insert(self, db: Session, entity: Usuario):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, entity_id: int, new_data: dict):
        usuario = db.query(Usuario).filter(Usuario.id == entity_id).first()
        if usuario:
            if 'nombre' in new_data:
                usuario.nombre = new_data['nombre']
            db.commit()
            db.refresh(usuario)
        return usuario

    def delete(self, db: Session, entity_id: int):
        usuario = db.query(Usuario).filter(Usuario.id == entity_id).first()
        if usuario:
            db.delete(usuario)
            db.commit()
        return usuario

    def select_all(self, db: Session):
        return db.query(Usuario).all()

    def select_by_id(self, db: Session, entity_id: int):
        return db.query(Usuario).filter(Usuario._id == entity_id).first()
