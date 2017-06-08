## GNA aplicando o metodo da congruencia
##Autores:Adrisson Galvão//Leandro Pereira//José Marcos  

import math
from datetime import datetime

now = datetime.now()##pegando a data atual

n= input("Digite quantos numeros deseja gerar:")##pegando quantidade de numeros aleatorios a serem gerados

if(n==0):## Verificando se n e valido
     print"Numero invalido"
     exit()

semente= ((math.pi*(n/2))*(now.second*now.day))/now.hour##Calculando a semente

a = now.microsecond##pegando a primeira constante

c = (now.hour*now.day)/now.second##pegndo a segunda costante

m=n*2 ##pegando a terceira constante

listaNumeros = []##lista para armazenar os numeros gerados

for x in range(0,n): ## for que vai de 0 a n

    if(len(listaNumeros)==0):##verificando se é o primeiro numero a ser gerado
        numeroAliatorio = (a*semente+c)%m ## calculando o numero aleatorio baseado na semente
    else:

        numeroAliatorio = (a*listaNumeros[len(listaNumeros)-1]+c)%m ## calculando o numero aleatorio baseado no ultimo numero gerado
        
    listaNumeros.append(numeroAliatorio)##adicionando o numero na lista
    
for x in listaNumeros: ##imprimindo a lista
    print x