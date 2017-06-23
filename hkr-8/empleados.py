from stack import *
class Empleado:
Id = 0
    def __init__(self,cantidadtareas,tareas):
        self.Cantidad = cantidadtareas
        self.tareas = None

        global id
        id += 1
        self.id = id

    def Gettareas(self):
        return self.tareas

    def GetCantidadTareas(self):
        return self.Cantidad

    def GetCodigodeEmpleado(self):
        return self.id

class Tarea:

    def __init__(self,descripcion,Area):
        self.Descripcion=descripcion
        self.AreaSolicitante = Area

    def GetDescripcion(self):
        return self.Descripcion

    def GetAreaSolicitante(self):
        return self.AreaSolicitante

class Tareas:
    def __init__(self):
        self.listareas = Stack()

    def AgregarTarea(self,descripcion,Area):
        self.listareas.push(Tarea(descripcion,Area))

class Empleados:

    def __init__(self):
        self.Registro = Stack()
        self.Busca = []
    def AgregarEmpleado(self,cantidadtareas,tareas):
        self.Registro.push(Empleado(cantidadtareas,tareas))

    def BuscarEmpleado(self,inicio,fin):
        for i in range(self.Registro.size()):
            Emple = self.Registro.pop()
            if Emple.id >= inicio and Emple.id <= fin:
                self.Registro.push(Emple)
                self.Busca.append(Emple)
            else:
                self.Registro.push(Emple)
    def Busqueda(self):
        print self.Busca

    def AsignarTarea(self):
        emplea = None
        for i in range(self.Registro.size()):
            emplea = self.Registro.pop()
            if emplea.Cantidad == emplea.tareas:
                self.Registro.push(Emplea)
            else:
                emplea.tareas = []
                while is not self.listareas.isEmpty() and emplea.Cantidad =! len(emplea.tareas):
                    tare = self.listareas.pop()
                    emplea.tareas.append(tare)
        self.Registro.push(emplea)            
