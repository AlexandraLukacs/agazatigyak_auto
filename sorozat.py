import random

randomszam_lista= []

def lottoszamok():
    print("II/A, B, C:")
    print(f"\t", end= "")
    for i in range(0, 5, 1):
        szamok: int= random.randint(0, 100)
        randomszam_lista.append(szamok)
        if i < 4:
            print(f"{szamok}", end= "; ")
        else:
            print(f"{szamok}", end= " ")

def konzol_kiir():
    print("II/D, E:")
    egyjegyuek_szama: int= 0
    for i in range(0, len(randomszam_lista), 1):
        if randomszam_lista[i] < 10:
            egyjegyuek_szama += 1
    return egyjegyuek_szama

def file_kiir(egyjegyuek_szama):
    
    f = open("szamok.txt", "w", encoding="utf-8")
    f.write(f"II/F:\n")
    f.write(f"\tAz egyjegyűek száma: {egyjegyuek_szama}")
    f.close()