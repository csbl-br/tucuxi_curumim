#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computational Systems Biology Laboratory
@authors: 
    Deney Araujo   (deneyaraujo@gmail.com)
    Juan Silva     (juancss99@gmail.com)
    André Martins  (agcostamartins@gmail.com)
    Helder Nakaya  (hnakaya@gmail.com) - Coordinator

Tucuxi-Curumim [v. 0.1]
"""
import pandas as pd
import random
import datetime
import argparse

def setOptions():
    option = argparse.ArgumentParser(description = '''Tucuxi-Curumim [v. 0.1]''')
    option.add_argument('-n','--number',      nargs='?', required=True, help='*Number of records to be created')
    option.add_argument('-s','--sep',      nargs='?', default='\t', help='Column delimiter')
    option.add_argument('-o','--output',     nargs='?', required=True, help='*Output file name')   
    return option.parse_args()

def cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
        cpf.append(11 - val if val > 1 else 0)                                  
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

setup = setOptions()
n = setup.number
s = setup.sep
output = setup.output

nRegister = int(n)
outPut = output
dataNames = pd.read_csv('data/names_gender.txt', encoding='utf-8', dtype=str, header=None)
dataSurNames = pd.read_csv('data/surnames.txt', encoding='utf-8', dtype=str, header=None)
dataNamesFem = pd.read_csv('data/names_fem.txt', encoding='utf-8', dtype=str, header=None)

opcoes =['simple','double','triple'] #weights
start=1

with open(outPut, 'w') as save:
    save.write('Id'+s+'Name'+s+'Mother'+s+'date of birth'+s+'Sex'+s+'CPF\n')
    for i in range(nRegister):
        x = random.choices(opcoes, weights=[0.05,0.8,0.15], k=1)
        nome = random.choice(dataNames[0])
        surname = random.choice(dataSurNames[0])
        date_birth = datetime.date(random.randint(1900,2019), random.randint(1,12),random.randint(1,28)).strftime("%d-%m-%Y")
        if 'simple' in x:
            save.write(f'ID_{str(start).zfill(9)}'+s+nome.rsplit('-',1)[0]+' '+surname+
                           s+random.choice(dataNamesFem[0])+' '+random.choice(dataSurNames[0])+' '+surname+
                           s+str(date_birth)+
                           s+nome.rsplit('-',1)[1]+
                           s+cpf()+'\n')
        elif 'double' in x:
            save.write(f'ID_{str(start).zfill(9)}'+s+nome.rsplit('-',1)[0]+' '+surname+' '+random.choice(dataSurNames[0])+
                           s+random.choice(dataNamesFem[0])+
                           ' '+random.choice(dataSurNames[0])+' '+surname+
                           s+str(date_birth)+
                           s+nome.rsplit('-',1)[1]+
                           s+cpf()+'\n')
        else:
            save.write(f'ID_{str(start).zfill(9)}'+s+nome.rsplit('-',1)[0]+' '+random.choice(dataSurNames[0])+' '+surname+' '+random.choice(dataSurNames[0])+
                           s+random.choice(dataNamesFem[0])+' '+random.choice(dataSurNames[0])+
                           ' '+random.choice(dataSurNames[0])+' '+surname+
                           s+str(date_birth)+
                           s+nome.rsplit('-',1)[1]+
                           s+cpf()+'\n')
        start+=1
