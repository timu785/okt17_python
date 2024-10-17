'''
adott egy lista
lista=[12, 21, 56, 32, -5, -23, 35]
Az alábbi metódusok paraméterként kapják a fenti listát.
1. Hány pozitív szám van benne?
2. Mennyi a negatív számok összege?
3. Mennyi az öttel osztható számok átlaga?
'''

def egy(lista):
    db:int=0
    i:int=1
    while(i<=len(lista)):
        if(lista[i-1]>0): db+=1
        i+=1
    return db

def ketto(lista):
    ossz:int=0
    i:int=1
    while(i<=len(lista)):
        if(lista[i-1]<0): ossz+=lista[i-1]
        i+=1
    return ossz

def harom(lista):
    ossz:int=0
    db:int=0
    i:int=1
    while(i<=len(lista)):
        if(lista[i-1]%5==0):
            ossz+=lista[i-1]
            db+=1
        i+=1
    return (ossz/db)



