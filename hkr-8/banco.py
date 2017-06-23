from movimiento import movimiento
from stack import Stack
class banco:
    def __init__(self):
        self.banco=Stack()
        self.temp = None
        self.depo = Stack()
        self.reti = Stack()
        self.cuen = Stack()
    def entrada(self,fecha,noCu,monto,tipo):
        self.banco.push(movimiento(fecha,noCu,monto,tipo))
            # separa los depositos en depo y los retiros en reti
    def arreglo(self):
        while not self.banco.isEmpety():
            tipo = self.banco.pop()
            if tipo.tipo == 0:
                depo.push(self.banco.pop)
            else:
                reti.push(self.banco.pop)
        # calcula la suma total de los depositos hasta una fecha
    def totaldepo(self, day):
        depo = self.temp
        suma= none
        suma2 = none
        fech = self.temp.pop()
        while fech.fecha <= day and not self.temp.isEmpety():
            suma = self.temp.pop()
            suma.monto = suma2
            suma2 += suma2
        return suma2
        # regresa el numero de depositos realizados hasta una fecha
    def nodepo(self, day):
        self.temp = depo.pop()
        tool = Stack()
        while self.temp.fecha <= day and not self.temp.isEmpety():
            tool.push(depo.pop)
        tool.size()
        return tool
        # separa los movimientos echos en una cuenta los almacena en cuen
    def cuenta(self,n):
        while not self.banco.isEmpety():
            cu = self.banco.pop()
            if cu.nocuenta == n:
                cuen.push(sefl.banco.pop)
            else:
                none
        # con cuen calcula el total de deposito de una cuenta
    def saldocuenta(self):
        while not cuen.isEmpety()
            op = cuen.pop()
            if op.tipo == 0:
                depocuen = op.monto
                totaldepocuen += depocuen
            else:
                reticuen = op.monto
                totalreticuen += reticuen

        return totaldepocuen
p.banco
for i in 5:
    (i,i,i,0)
