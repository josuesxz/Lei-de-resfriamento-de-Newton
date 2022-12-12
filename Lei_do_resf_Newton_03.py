from ast import Break
from tkinter import Label
import matplotlib.pyplot as graph
import matplotlib.lines
import numpy as np
import math

graph.ion() #permite o dinamismo do gráficos
graph.style.use("dark_background") #altera o tema usado do gráfico: https://matplotlib.org/devdocs/gallery/style_sheets/style_sheets_reference.html

print(" ")
print("\tBem vindo")


print(" ")
    
print("Defina alguns parametros")
Tamb = float(input("Temperatura ambiente  : "))
Tcorp = float(input("Temperatura do corpo : "))
t1 = float(input("Diga um tempo em minuto: "))
T1 = float(input("Qual a temperatura em {} minuto(s): ".format(t1)))
uniT = str(input("Qual unidade de temperatura C, F ou K: ")).upper()

A = Tcorp - Tamb #Para t == o
DT = T1 - Tamb
paraLog = DT/A
k = - math.log(paraLog)/t1

while(True):
    print(" ")
    print("1 - Monitoramento de temperatura")
    print("2 - Tempo para buscar o equilibrio do corpo")
    print("3 - Sair")
    
    questMenu = int(input("Qual opcao deseja: "))
    print("Opcao selecionada: ", questMenu)

    if(questMenu == 1):
        print(" ")
        print("\tOPCAO DE MONITORAMENTO DA TEMPERATURA")

        graph.plot(':', color = "r", label = "dT/dt")
        graph.rcParams['figure.figsize'] = (11, 7)
        graph.xlabel("Tempo(min)", color = "g")
        graph.ylabel("Temperatura(" +uniT+")" , color = "#FF00FF")
        graph.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
       # graph.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
        graph.legend()
        graph.title("Lei do resfriamento de Newton", color = "#FF4500")

        print("Constante k = {}". format(k))
        Tempo = []
        Temperatura = []
        for x in np.arange(0,60,1):
            Tempo.append(x)
            Temperatura.append(A*np.exp(-k*x)+Tamb)
            graph.scatter(Tempo, Temperatura, marker = ",", color = "r")
            graph.plot(Tempo, Temperatura)
            print("No tempo de {} minutos, a temperatura e de {} {}".format(Tempo[x], round(Temperatura[x], 2), uniT))
            if(Temperatura[x] <= Tamb):
                graph.ioff()
                graph.show()
                print("O corpo chegou a temperatura ambiente!")
                break

            graph.pause(2) #pausa no uso do gráfico de 2s

            graph.show()

        print("FIM")

    elif(questMenu == 2):
        print(" ")
        print("\tOPCAO DE CAULCULO DO TEMPO")
        Td = float(input("Qual a temperatura final: "))
        if(Td == Tamb or Td <= Tamb):
            print(" ")
            print("ERROR!!")
            print(" ")
            print("Defina um número maior que a temperatura ambiente, nao pode ser menor tambem")
            print(" ")
        else:
            X = (Td - Tamb)/A
            tf = - math.log(X)/k
            print("Aproximadamente {} Minutos".format(round(tf, 2)))
            print(" ")

    elif(questMenu == 3): 
        print("FIM")
        break
