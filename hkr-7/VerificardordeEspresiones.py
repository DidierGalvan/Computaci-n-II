#-*- coding:utf -8 -*-
from stack import *
from calculadoraHP import *
import re
num = []
x = ''
o = ''
p = ''
y = ''
def verificaParentesis(symbolString):
    s = Stack()
    balanced = True
    index = 0
    sim = Stack()
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif re.match("[0-9]", symbol):
            num.append(symbol)
        elif symbol == "+" or symbol == "-" or symbol== "/" or symbol== "*" or symbol == "%":
            num.append(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
         k = str(symbolString).replace('(',' ')
         h = str(k).replace(')',' ')
         j = h.split()
         return True
    else:
        return False
q = raw_input("Dame una expresión del tipo ((+)-(*)%(/)-(+)): ")
f = "(((2234679*3)+(300/5)-(2334+6546)-(265*3)))"
if verificaParentesis(q) == True:
    sus = 0
    for i in range(len(num)):
        a = num[i]
        if re.match("[0-9]",a):
            x +=a
            if i+1 < len(num):
                b = num[i+1]
                if not re.match("[0-9]",b):
                    o += x +" "
                    x = ''
                    sus += 1
                    if sus == 2:
                        o += p + " "+ y +" "
                        print o
                        sus =0
            else:
                o += x +" "
                x = ''
                sus += 1
                if sus == 2:
                    o += p +" "+ y +" "
                    print o
                    sus =0
                    p = ''
                    y = ''
        else:
            if p == '':
                p = a
                print p
            else:
                y = a
                p = ''
                print y
    pato = str(o).split()
    calculadora_polaca(pato)
else:
    print "TU EXPRESION ESTA MAL ESCRITA"
