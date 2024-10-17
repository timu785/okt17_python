import random

def ermedobas():
    lista=[]
    i:int=1
    while(i<=10):
        ran:int=int(random.random()*2)
        if(ran==0): lista.append("fej")
        if(ran==1): lista.append("írás")
        i+=1
    return lista

def fejdb(lista):
    db:int=0
    i:int=1
    while(i<=len(lista)):
        if(lista[i-1]=="fej"): db+=1
        i+=1
    return db

def kockadobas():
    i:int=1
    lista=[]
    while(i<=200):
        lista.append(int(random.random()*6+1))
        i+=1
    return lista

def dobasdb(lista):
    db1:int=0; db2:int=0; db3:int=0; db4:int=0; db5:int=0; db6:int=0
    i:int=1
    while(i<=len(lista)):
        if(lista[i-1]==1): db1+=1
        if(lista[i-1]==2): db2+=1
        if(lista[i-1]==3): db3+=1
        if(lista[i-1]==4): db4+=1
        if(lista[i-1]==5): db5+=1
        if(lista[i-1]==6): db6+=1
        i+=1
    return [db1, db2, db3, db4, db5, db6]

def dobasdb2(lista):
    db=[0, 0, 0, 0, 0, 0]
    i:int=1
    while(i<=len(lista)):   
        db[lista[i-1]-1]+=1
        i+=1
    return db

def cinkelt():        
    i:int=1
    lista=[]
    while(i<=200):
        ran:int=int(random.random()*13+1)
        if(ran>6):ran=6
        lista.append(ran)
        i+=1
    return lista
