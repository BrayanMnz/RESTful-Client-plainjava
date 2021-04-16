#!/usr/bin/env python

from suds.client import Client

url = "http://localhost:7000/ws/EstudianteWebServices?wsdl"
client = Client(url)
#Printeando 
print (client)
# #Ejecutando la salida del estudiante.
# estudiante=client.service.getEstudiante(201000000)
# print (estudiante.nombre)
# #Profesor
# print (client.service.getProfesor('123123').nombre)

# print (len(client.service.getListaEstudiante()))

def ListaEstudiantes():
    print('Listado de estudiantes: ')
    list_Est = client.service.getListaEstudiante()
    
    for x in list_Est:
        print(x)
        


def consultarEstudiante(matricula):
    print('Estudiante Consultado: ')
    print(client.service.getEstudiante(matricula))
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
    

ListaEstudiantes()
consultarEstudiante(20170770)
CrearEstudiante('ITT','20170770','Brayan')
ListaEstudiantes()
EliminarEstudiante(20011136)
ListaEstudiantes()






