from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class BaseDatosServices(ABC):
    """
    Clase abstracta base para definir los métodos CRUD.
    """

    @abstractmethod
    def insert(self, db: Session, entity):
        pass

    @abstractmethod
    def update(self, db: Session, entity_id, new_data):
        pass

    @abstractmethod
    def delete(self, db: Session, entity_id):
        pass

    @abstractmethod
    def select_all(self, db: Session):
        pass

    @abstractmethod
    def select_by_id(self, db: Session, entity_id):
        pass
