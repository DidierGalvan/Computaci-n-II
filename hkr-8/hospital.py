from Queue import *
class Medico:
id = 0
    def __init__(self,especialidad,fecha,turnoslibres,turnosocupados):
        self.Especialidad = especialidad
        self.NoTurnosLibres = turnoslibres
        self.NoturnosOcupados = turnosocupados
        self.FechaDeAtencion = fecha
        global id
        id +=1
        self.CodigodeMedico = id

    def GetNoTurnoslibres(self):
        return self.NoTurnosLibres

    def GetNoturnosOcupados(self):
        return self.NoturnosOcupados

    def SetNoturnosOcupados(self,n):
        self.NoturnosOcupados = n

    def GetFechaAtencion(self):
        return self.FechaDeAtencion

    def GetCodigodeMedico(self):
        return self.CodigodeMedico

    def GetEspecialidad(self):
        return self.Especialidad

class Medicos:

    def __init__(self):
        self.Docs= Queue()

    def AgregarMedico(self,especialidad,fecha,turnoslibres,turnosocupados):
        self.Docs.push(Medico(especialidad,fecha,turnoslibres,turnosocupados))
    def Verificar_Turno(self,codigo,fecha):
        g = True
        K = False
        for i in range(self.size):
            Doc=self.Docs.dequeue()
            if Doc.GetCodigodeMedico() = codigo:
                if Doc.GetFechaAtencion()= fecha:
                    if Doc.GetNoTurnoslibres() < Doc.GetNoturnosOcupados():
                        print g
                        self.Docs.enqueue(Doc)
                else:
                    print k
                    self.Docs.enqueue(Doc)
            else:
                self.Docs.enqueue(Doc)

class Agendas:

    def __init__(self):
        self.Gral = Queue()
        self.Especialidad = Queue()

    def Agendar(self,Medicos,fechaini,fechafin,turnosdisp):
        turOcupados = 0
        for i in range(Medicos.size())
            Medic = Medicos.dequeue()
            if Medic.GetFechaAtencion >= fechaini and Medic.GetFechaAtencion <= fechafin:
                if turnOcupados <= turnosdisp:
                    Disponibilidad = (Medic.GetNoTurnoslibres)-(Medic.GetNoturnosOcupados)
                    if Disponibilidad > 0:
                        turOcuapados += Disponibilidad
                        self.Gral.enqueue(Medic)
                        Medicos.enqueue(Medic)
    def AgendarEspecial(self,especialidad,Medicos,fechaini,fechafin,turnosdisp):
        turOcupados = 0
        for i in range(Medicos.size())
            Medic = Medicos.dequeue()
            if Medic.GetEspecialidad() == especialidad:
                if Medic.GetFechaAtencion >= fechaini and Medic.GetFechaAtencion <= fechafin:
                    if turnOcupados <= turnosdisp:
                        Disponibilidad = (Medic.GetNoTurnoslibres)-(Medic.GetNoturnosOcupados)
                        if Disponibilidad > 0:
                            turOcuapados += Disponibilidad
                            self.Especialidad.enqueue(Medic)
                            Medicos.enqueue(Medic)
