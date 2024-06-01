# Generador de Email Unico
from random import randint

print('*** Bienvenido al sistema de generación de email ***')

nombre = input('Ingresa tu Nombre: ')

apellido = input('Ingresa tu Apellido: ')

aleatorio = randint(0, 99)

email_generado = f'{nombre.lower()}.{apellido.lower()}{aleatorio}@tuemail.com'

print(f'''\nTu nuevo email generado por el sistema es:
    {email_generado}
    *** Felicidade ***''')