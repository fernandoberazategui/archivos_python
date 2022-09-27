# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from dataclasses import dataclass
from tkinter.filedialog import Open
from webbrowser import get


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    csvfile= open (archivo, 'r')
    data=list(csv.DictReader(csvfile))
    contador_tornillos=0
    for articulo in data:
        contador_tornillos += int(articulo ['tornillos'])
    print("la cantidad de tornillos es: ",contador_tornillos)
    csvfile.close


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    csvfile=open(archivo,'r')
    data=list(csv.DictReader(csvfile))

    cantidad_dptos=len(data)
    contador_2ambientes=0
    contador_3ambientes=0
        
    for dpto in range(cantidad_dptos):
        fila=data[dpto]
        
        try:
            cantidad_ambientes=int(fila.get('ambientes'))
            if cantidad_ambientes==2:
                contador_2ambientes += 1
            elif cantidad_ambientes==3:
                contador_3ambientes += 1

        except:
            continue
    print('En la cantidad total de dptos: ', cantidad_dptos)
    print('Hay', contador_2ambientes, 'dptos de 2 hambientes')
    print('Y', contador_3ambientes, 'dptos de 3 hambientes')
    csvfile.close
        









    



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
