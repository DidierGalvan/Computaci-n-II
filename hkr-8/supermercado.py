from stack import *
id = 0
class Producto:
    def __init__(self,precio,fecha):
        self.Precio = precio
        self.NoCambioPrecio = 0
        self.Fecha = fecha
        self.cambios = [[],[]]
        global id
        id +=1
        self.CodigodeProducto = id

    def Getfecha(self):
        return self.Fecha

    def Setfecha(self,new):
        self.fecha = new
        self.cambios[0].appennd(self.fecha)

    def Getprecio(self):
        return self.Precio

    def actualizarProducto(self,new,NewPrecio):
        self.Setprecio(NewPrecio)
        self.Setfecha(new)

    def Setprecio(self,NewPrecio):
        self.Precio = NewPrecio
        self.cambios[1].append(self.NewPrecio)

    def GetNoCambioPrecio(self):
        self.NoCambioPrecio = len(self.cambios[1])
        return self.NoCambioPrecio

    def GetCodigodeProducto(self):
        return self.CodigodeProducto

class Productos:
    def __init__(self):
        self.ListaProducts = Stack()
        self.MaxRe = Stack()
        self.Prom = []
    def agregarProducto(self,precio,fecha):
        self.ListaProducts.push(Producto(precio,fecha))

    def actualizar(self,newprecio,newfecha,id):
        for i in range(self.ListaProducts.size):
            Product = self.ListaProducts.pop()
            if Produc.CodigodeProducto = id:
                Produc.actualizarProducto(newfecha,newprecio)
                self.ListaProducts.push(Product)
            else:
                self.ListaProducts.puch(Product)
    def MaxRemarcados(self,n):
        for i in range(self.ListaProducts.size):
            Product = self.ListaProducts.pop()
            Cam = len(Product.cambios[1])
            if  Cam >= n:
                self.MaxRe.push(Product)
                self.ListaProducts.push(Product)
            else:
                self.ListaProducts.push(Product)
    def Promedio(self):
        for i in range(self.ListaProducts.size):
            Product = self.ListaProducts.pop()
            ids = Produc.CodigodeProducto
            nocambios = len(Product.cambios[0])
            Semi = 0
            for i in range(len(Product.cambios[1]))
                semi += Product.cambios[1][i]
            promedio = semi/nocambios
            list = [ids , nocambios, promedio]
            self.Prom.append(list)
            self.ListaProducts.push(Product)
            print self.Prom
