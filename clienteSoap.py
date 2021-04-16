#!/usr/bin/env python

from suds.client import Client
from welcome import welcome

url = "http://localhost:7000/ws/EstudianteWebServices?wsdl"
client = Client(url)


def ListaEstudiantes():
    print('Listado de estudiantes: ')
    list_Est = client.service.getListaEstudiante()
    
    for x in list_Est:
        print(x) 

def consultarEstudiante(matr):
    print('Estudiante Consultado: ')
    print(client.service.getEstudiante(matr))
    print('\n')


def CrearEstudiante(carr, mat, nomb):
    estudiante = {
    "carrera": carr,
    "matricula": mat,
    "nombre": nomb
}
    client.service.crearEstudiante(estudiante)
    print('Estudiante creado correctamente! ')



def EliminarEstudiante(matricula):
    client.service.EliminarEstudiante(matricula)
    print('Estudiante eliminado correctamente! ')
    



def main():
    while True:
      
        print(welcome("BrayanMnz"))
        print("\nSeleccione uno de los incisos de la práctica : ")
        print("""
        1 : Listar todos los Estudiantes.
        2 : Consultar Estudiante.
        3 : Crear un nuevo estudiante.
        4 : Borrar un estudiante.
        
        0: Salir
       """  )
        choice = input("\nInserte su selección : ")

        if choice == '1':
            ListaEstudiantes()
        elif choice == '2':
            matr = input("\nInserte matricula a consultar: ")
            consultarEstudiante(matr)
        elif choice == '3':
            mat = input("\nInserte matricula del Estudiante : ")
            nomb = input("\nInserte Nombre del Estudiante : ")
            carr = input("\nInserte carrera del Estudiante : ")
    
            CrearEstudiante(carr, mat, nomb)
        elif choice == '4':
            mat = input("\nInserte matricula del Estudiante a Eliminar : ")
            EliminarEstudiante(mat)
        elif choice == '0':
	    print('\n\nCLIENTE SOAP REALIZADO POR BRAYAN MUÑOZ V.  2017-0770 \n')
            exit()



if __name__ == "__main__":
    main()



