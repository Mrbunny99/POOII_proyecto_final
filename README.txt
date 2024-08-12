Proyecto Final de POO II

Descripcion
Este proyecto es un sistema CRUD implementado en Python utilizando 
principios de programación orientada a objetos (OOP) y SQLAlchemy para 
la persistencia de datos. El sistema maneja usuarios y publicaciones, y 
permite exportar e importar datos.

Requisitos
- Python
- SQLAlchemy
- PyMySQL
- MySQL Workbanch
- Docker

Instalacion
Clona el repositorio
    git clone https....

Navega al directorio del proyecto
    cd proyecto_final

Crea y activa un entorno virtual
    .\myenv\Scripts\activate

Instala las dependecias
    pip install -r requeriments.txt

ESTRUCTURA DEL PROYECTO

proyecto_final/
│
├── aplicacion/
│   ├── usuario_service.py
│   ├── loggers.py
│   └── publicacion_service.py
│
├── datos/
│   ├── models.py
│   ├── base_service.py
│   ├── crud.py
│   ├── database.py
│   ├── export_service.py
│   └── import_service.py
│
│
├── logs/
│   └── app.log
│── main.py
├── historial.txt
├── README.txt
└── .gitignore
