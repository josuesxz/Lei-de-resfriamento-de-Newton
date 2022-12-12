quest = str(input("Permanecer em *"uniT )).upper()
    if(quest == "S"):
        print(Tcorp," *C")
        print(Tamb," *C")
        print("Ficara em *C")

    elif(quest == "N"):
        print("1 - *F")
        print("2 - K")
        temMenu = int(input("Qual medida deseja: ")) #uso do gráfico dinâmico
        if(temMenu == 1):
            fCorp = Tcorp*1.8 + 32
            fAmb = Tamb*1.8 + 32
            print(fCorp)
            print(fAmb)
        elif(temMenu == 2):
            kCorp = Tcorp + 273.15
            kAmb = Tamb + 273.15
            print(kCorp)
            print(kAmb)