# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:44:25 2022

@author: Avita
"""

class Toy:
    def __init__(self, tId, Ttype, Tprice):
        self.ToyId=tId
        self.ToyType=Ttype
        self.Price=Tprice
        self.DiscountApplication=0
        
class Store:
    def __init__(self, toyList, toyDic):
        self.toyList=toyList
        self.toyDic=toyDic
        
    def calculateDiscount(self):
        for toy in self.toyList:
            if toy.ToyType.lower() in self.toyDic.keys():
                r=self.toyList[toy.ToyType.lower()]
                dis= toy.price*(r/100)
                toy.DiscountApplication=dis
                
if __name__=='__main__':
    count=int(input())
    
    toys=[]
    toyDic={}
    
    for i in range(count):
        tid=input()
        ttype=input()
        price=int(input())
        
        t=Toy(tid,ttype,price)
        
        toys.append(t)
        
    for i in range(3):
        toyType=input()
        amount= int(input())
        
        toyDic[toyType.lower()]=amount
        
    toyStore=Store(toys, toyDic)
    
    toyStore.calculateDiscount()
    
    toyStore.toyList.sort(key= lambda x: x.DiscountApplication, reverse=True)
    
    for toy in toyStore.toyList:
        dp=toy.Price-toy.DiscountApplication
        
        print(toy.ToyId, toy.Price, dp)
        
