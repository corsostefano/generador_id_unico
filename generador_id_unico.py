# Generador ID Unico

from random import randint

print('*** Sistema de Generador ID Unico ***')

nombre = input('Cual es tu nombre: ')

iniciales_nombre = nombre[0:2].upper()


apellido = input('Cual es tu apellido: ')

iniciales_apellido = apellido[0:2].upper()

anio_nacimiento = input('cual es tu año de nacimiento (YYYY): ')

numeros_fecha = anio_nacimiento[2:4]

# Generar un valor de 4 digitos aleatorio

aleatorio = randint(0, 9999)

id_unico = f'{iniciales_nombre}{iniciales_apellido}{numeros_fecha}{aleatorio}'

print(f'''\nHola {nombre}, habitante de la ciudad! 
    tu numero de identificacion (ID) generado por el sistema es:
    {id_unico}
    Felicidades!''')