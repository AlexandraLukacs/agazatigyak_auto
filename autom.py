from Autok import Autok

auto_lista=[]
fajl = open("auto.txt", "r", encoding='utf-8')
fajl.readline()
lista=fajl.readlines()
fajl.close()
for i in range(0, len(lista), 1):
    aktsor:str=lista[i].strip()
    print(aktsor)
    sor_lista=aktsor.split("$")
    print(sor_lista[0])
    print(sor_lista[1])
    autok=Autok(sor_lista[0], int(sor_lista[1]))
    auto_lista.append(autok)

for i in range(0, len(auto_lista), 1):
    print(f"{auto_lista[i].nev}, {auto_lista[i].gyart_datum}")

def flotta():
    print("III/Flotta:")
    db: int= 0
    for i in range(0, len(auto_lista), 1):
        db += i
    return db