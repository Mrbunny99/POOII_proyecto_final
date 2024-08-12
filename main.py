import logging
from sqlalchemy.orm import Session
from datos.database import SessionLocal
from datos.models import Usuario, Publicacion
from aplicacion.usuario_service import UsuarioService
from aplicacion.publicacion_service import PublicacionService
from datos.export_service import export_table
from datos.import_service import import_historial
from aplicacion.logger import log_action

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

def main():
    db: Session = SessionLocal()
    usuario_service = UsuarioService()
    publicacion_service = PublicacionService()

    while True:
        print("-----Seleccione una opcion------")
        print("1. Crear Usuario")
        print("2. Leer Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Crear Publicación")
        print("6. Leer Publicaciones")
        print("7. Actualizar Publicación")
        print("8. Eliminar Publicación")
        print("9. Exportar Tabla")
        print("10. Importar Historial")
        print("11. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            logging.info(f'Intentando crear usuario con nombre: {nombre} y email: {email}')
            nuevo_usuario = Usuario(nombre=nombre, email=email)
            usuario_service.insert(db, nuevo_usuario)
            log_action('C: Usuario creado')
            with open('registro.txt', 'a') as file:
                file.write(f'Usuario creado: {nombre}, Email: {email}\n')

        elif opcion == '2':
            usuarios = usuario_service.select_all(db)
            for usuario in usuarios:
                print(usuario.nombre)
            log_action('R: Usuarios leídos')
            with open('registro.txt', 'a') as file:
                file.write('Usuarios leídos\n')

        elif opcion == '3':
            entity_id = int(input("Ingrese el ID del usuario: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
            usuario_service.update(db, entity_id, {'nombre': nuevo_nombre})
            log_action('U: Usuario actualizado')
            with open('registro.txt', 'a') as file:
                file.write(f'Usuario actualizado: {entity_id} a {nuevo_nombre}\n')

        elif opcion == '4':
            entity_id = int(input("Ingrese el ID del usuario a eliminar: "))
            usuario_service.delete(db, entity_id)
            log_action('D: Usuario eliminado')
            with open('registro.txt', 'a') as file:
                file.write(f'Usuario eliminado: {entity_id}\n')

        elif opcion == '5':
            titulo = input("Ingrese el título de la publicación: ")
            contenido = input("Ingrese el contenido de la publicación: ")
            usuario_id = int(input("Ingrese el ID del usuario: "))
            nueva_publicacion = Publicacion(titulo=titulo, contenido=contenido, usuario_id=usuario_id)
            publicacion_service.insert(db, nueva_publicacion)
            log_action('C: Publicación creada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación creada: {titulo}\n')

        elif opcion == '6':
            publicaciones = publicacion_service.select_all(db)
            for publicacion in publicaciones:
                print(f'Título: {publicacion.titulo}, Contenido: {publicacion.contenido}')
            log_action('R: Publicaciones leídas')
            with open('registro.txt', 'a') as file:
                file.write('Publicaciones leídas\n')

        elif opcion == '7':
            entity_id = int(input("Ingrese el ID de la publicación: "))
            nuevo_titulo = input("Ingrese el nuevo título de la publicación: ")
            nuevo_contenido = input("Ingrese el nuevo contenido de la publicación: ")
            publicacion_service.update(db, entity_id, {'titulo': nuevo_titulo, 'contenido': nuevo_contenido})
            log_action('U: Publicación actualizada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación actualizada: {entity_id} a {nuevo_titulo}\n')

        elif opcion == '8':
            entity_id = int(input("Ingrese el ID de la publicación a eliminar: "))
            publicacion_service.delete(db, entity_id)
            log_action('D: Publicación eliminada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación eliminada: {entity_id}\n')

        elif opcion == '9':
            table_name = input("Ingrese el nombre de la tabla a exportar: ")
            export_table(db, table_name)
            log_action(f'Exportación de tabla: {table_name}')

        if opcion == '10':
            print("Importación de historial iniciada...")
            log_action('Importación de historial iniciada')
            import_historial(db)
            print("Importación de historial completada.")
            log_action('Importación de historial completada')

        elif opcion == '11':
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
