import math
from datetime import datetime
now = datetime.now()
n= input("Digite quantos numeros deseja gerar:")
if(n==0):
     print"Numero invalido"
     exit()
semente= ((math.pi*(n/2))*(now.second*now.day))/now.hour

a = now.microsecond
c = (now.hour*now.day)/now.second
m=n*2

listaNumeros = []
for x in range(0,n):
    if(len(listaNumeros)==0):
        numeroAliatorio = (a*semente+c)%m
    else:
        numeroAliatorio = (a*listaNumeros[len(listaNumeros)-1]+c)%m
    listaNumeros.append(numeroAliatorio)
    
for x in listaNumeros:
    print x