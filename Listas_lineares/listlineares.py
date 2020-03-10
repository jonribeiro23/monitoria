# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:12:45 2020

@author: lab53
"""


class Lista:
    def __init__(self, tamanho):
        self.tamanho=tamanho
        self.p = int(-1)
        self.lista=[]
        for i in range(tamanho):
            self.lista.append(None)
        
    
    def insere(self, x):
        self.p+=1
        print(self.p)
        self.lista[self.p]=x
        
    
    def remove(self):
        temporario=self.lista[self.p]
        self.lista[self.p] = None
        self.p-=1
        return temporario
    
    
    def listacheia(self):
        return self.p==self.tamanho-1
    
    
    def listavazia(self):
        return self.p==-1

    
    def mostralista(self):
        print(self.lista)





