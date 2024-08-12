import logging
import os

# Crear el directorio 'logs' si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

def log_action(action):
    logging.info(f'Acción: {action}')
    with open('historial.txt', 'a') as file:
        file.write(f'{action}\n')
