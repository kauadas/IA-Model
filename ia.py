import collections

import random
import json

def load_json(data):
    data=json.loads(data)
    return data

def dictia(db):
    cole_index=[]
    cole_od=[]
    groups={}
    
    with open(db) as td:
        trainerdata=td.read()
        trainerdata=load_json(trainerdata)
        for i in trainerdata:
            od=trainerdata[i]
            cole_index.append(i)
            cole_od.append(od)

        td.close()

    def iadef(data: dict):
        pontuação_total={}
        for i in range(0,len(cole_index)):
            points=0
            index=cole_index[i]
            objdata=cole_od[i]
            if str(type(data)) == "<class 'dict'>":
                for i2 in data:
                    d=data[i2]
                    if i2 in objdata:
                        if d == objdata[i2]:
                            points+=1

                
                pontuação_total[index]=points

        

                
            else:
                return "not a dict"

        maior=('a',0)
        for i in pontuação_total:
            if pontuação_total[i] > maior[1]:
                maior=(i,pontuação_total[i])

        if int(maior[1]) > int(len(data)/2):
            return maior

        else:
            return (None,0)

    return iadef
    

def recnoia(string1: str,string2: str):
    points=0
    maior=[string2,len(string2)]
    menor=[string1,len(string1)]
    for i in [string1,string2]:
        if len(i) < menor[1]:
            maior=menor
            menor=[i,len(i)]

    txt=menor[0]
    
    for i in range(0,len(maior[0])):
        
        if i >= len(menor[0]):
            
            txt+="°"
            
    
    menor=[txt,menor[1]]

    for i in range(0,maior[1]):
        d1=maior[0][i]
        d2=menor[0][i]

        if d1 == d2:
            points+=(1/(maior[1]))

    
        
            

    return ((points*100))