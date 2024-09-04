import os 
import datetime
from numpy import indices 

class indices:
#Constructor
    def __init__(self):
        #Atributos de la clase indice :)
        self.__pot_d=0
        self.__pot_b=0
        self.__pot_a1=0
        self.__pot_a2=0
        self.__pot_t=0
        self.__pot_g=0
#Metodos para acceder 
    def VerPotencia_D(self):
        return self.__pot_d 
    def AsignarPotencia_D(self,var):
        self.__pot_d=var

    def VerPotencia_B(self):
        return self.__pot_d    
    def AsignarPotencia_B(self,var):
        self.__pot_d=var
    
    def VerPotencia_T(self):
        return self.__pot_d
    def AsignarPotencia_T(self,var):
        self.__pot_d=var

    def VerPotencia_A1(self):
        return self.__pot_d
    def AsignarPotencia_A1(self,var):
        self.__pot_d=var
    
    def VerPotencia_A2(self):
        return self.__pot_d
    def AsignarPotencia_A2(self,var):
        self.__pot_d=var

    def VerPotencia_G(self):
        return self.__pot_d
    def AsignarPotencia_G(self,var):
        self.__pot_d=var

class visita:
    def __init__(self):
        self.__registro= datetime.datetime.now().strftime("%x")
        self.__fecha=''
        self.__nota=''
        self.__indice= indices()
    
    #Metodos 
    def VerRegistro(self):
        return self.__registro
    def AsignarRegistro(self,var):
        self.__registro=var
    
    def VerFecha(self):
        return self.__fecha
    def AsignarFecha(self,var):
        self.__fecha=var
    
    def VerNota(self):
        return self.__nota
    def AsignarNota(self,var):
        self.__nota=var

    def VerIndice(self):
        return self.__indice
    def AsignarIndices(self,var):
        self.__indice=var
    
    
    
class Paciente:
    def __init__(self):
        self.__nombre=''
        self.__cedula=0
        self.__genero=''
        self.__visitas={} #Clave-> Fecha Valor->visita/// Los pacientes tienen muchas visitas, por lo tanto lo trataremos como diccionarios

#Metodos para acceder a la clase
    def VerNombre(self):
        return self.__nombre
    def AsignarNombre(self,var):
        self.__nombre=var
    
    def VerCedula(self):
        return self.__cedula
    def AsignarCedula(self,var):
        self.__cedula=var

    def VerGenero(self):
        return self.__genero
    def AsignarGenero(self,var):
        self.__genero=var

    def VerVisitasListado(self):
        return self.__visitas
    def AsignarVisitas(self,var):
        self.__visitas[var.VerFecha()]=var
    def VerVisita(self,var):
        return self.__visitas.get(var)
    
    #Verificar si existe alguna visita 
    def ExisteVisita(self,var):
        return var in self.__visitas
    def EliminarVisita(self,var):
        del self.__visitas[var]

class sistema:
    def __init__(self):
        self.__pacientes={} #La llave es la cedula y el valor es el paciente 

    def VerListadoPacientes(self):
        return self.__pacientes
    def AgregarPaciente(self,var):
        self.__pacientes[var.verCedula()]=var
    def VerificarSiExiste(self,var):
        return var in self.__pacientes
    def EliminarPacientes(self,var):
        del self.__pacientes[var]
    def RecuperarPacientes(self,var):
        return self.__pacientes[var]
    def CargarGuardarPacientes(self,var):
        pass


def validar(msj):
    while True:
        try:
            valor=int(input(msj))
            break
        except ValueError:
            print('Por favor ingrese valores numericos')
    return valor

def validarf(msj):
    while True:
        try:
            valor=float(input(msj))
            break
        except ValueError:
            print('Por favor ingrese valores numericos')
    return valor

def main():
    sis=sistema
    while True:
        print('''
Ingrese
1. Agregar paciente
2. Editar paciente
3. Eliminar paciente 
4. Guardar y cargar paciente
5. Ver cantidad de pacientes  
6. Salir del sistema. ''')
        menu=validar('Ingrese opcion')
        if menu == 1: #Agregar paciente
            #Verificar si exite el paciente 
            p=Paciente()
            cedula=validar('Ingresar cedula del paciente')
            if sis.VerificarSiExiste(cedula)== True:
                print('El paciente ya existe, verifique con otro paciente')
                continue
            else:
                p.AsignarNombre(input('Ingrese Nombre'))
                p.AsignarGenero(input('Ingrese el genero del paciente'))
                p.AsignarCedula(cedula)
                NumeroVisitantes=validar('Ingrese el numero de visiantes del paciente')
                for i in range(0,NumeroVisitantes):
                    dia=validar('Ingrese dia de la visita')
                    mes=validar('Ingrese el mes')
                    año=validar('Ingrese el año ')
                    f=datetime.datetime(dia,mes,año).strftime('%x')
                    if p.VerificarSiExiste(f) == True:
                        print('Ya existe visita , ingresa otra nuevamente')
                        continue
                    else:
                        v=visita()
                        v.AsignarFecha(f)
                        v.AsignarNota(input('Ingrese observaciones'))
                        v.AsignarRegistro(os.getcwd()+f'/Pacientes_{p.verCedula()}')              
                        ind = v.VerIndice()
                        ind.AsignarPotencia_A1(validarf('Ingrese potenica A1'))
                        ind.AsignarPotencia_A2(validarf('Ingrese potencia A2'))
                        ind.AsignarPotencia_T(validarf('Ingrese potencia T'))
                        ind.AsignarPotencia_B(validarf('Ingrese potencia B'))
                        ind.AsignarPotencia_D(validarf('Ingrese potencia D'))
                        ind.AsignarPotencia_G(validarf('Ingrese potencia G'))
                        p.AsignarVisitas(v)
                sis.AsignarPaciente(p)
            
        if menu == 2:
            #Editar Pacientes 
            
        if menu == 3:
            pass
        if menu == 4:
            pass
        if menu == 5:
            pass
        if menu == 6:
            break
        else:
            print('EL numero que ingresaste no es el correcto intente nuevamente')



