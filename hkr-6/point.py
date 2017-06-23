#Python
import math
class point:
    def __init__(self,xs,ys):
        self.x=xs
        self.y=ys
        self.gu= None
    def Move(self,xs,ys):
        self.x=xs
        self.y=ys
    def calculate_distance(self, B):
        y1 = B.y
        x1 = B.x
        y2= self.y
        x2=self.x

        d= math.sqrt(((y1 - y2)**2)+((x1 - x2)**2))
        print d
    def reset(self):
        self.gu=point(self.x,self.y)
        self.x=0
        self.y=0
    def regresa(self):
        self.x=gu.x
        self.y=gu.y
list=[]
n = raw_input("")
g = int(n)
for i in range(g):
    A = raw_input("")
    a = A.split(" ")
    x=int(a[0])
    y=int(a[1])
    z = point(x,y)
    list.append(z)
for i in range((len(list)-1)):
    f = list[i*2]
    t = list[(i*2)+1]
    t.calculate_distance(f)
