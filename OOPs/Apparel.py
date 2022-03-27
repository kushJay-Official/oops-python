# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:02:32 2022

@author: Avita
"""

class Apparel:
    def __init__(self,brand,ptype,price,avail):
        self.brand=brand
        self.ptype=ptype
        self.price=price
        self.avail=avail #dictionary for size & qunatity
        
class Store:
    def __init__(self, aplList):
        self.aprlList=aplList
        
    def checkAvailability(self,gbrnd,gtype,gsize,gquan):
        
        for aprl in self.aprlList:
            if aprl.brand==gbrnd and aprl.ptype==gtype:
                
                #for dictionary traveseral 
                
                for key, ele in aprl.avail.items():
                    if key==gsize and ele==gquan:
                        aprl.avail[gsize]-=gquan
                        return True
        return False

if __name__=='__main__':
    count=int(input())
    
    aList=[]
    
    for i in range(count):
        b=input()
        t=input()
        p=int(input())
        
        n=int(input())
        avl={}
        
        for k in range(n):
            s=input().upper()
            q=int(input())
            
            avl[s]=q
            
        objApparel=Apparel(b,t, p, avl)
        aList.append(objApparel)
        
    objStore= Store(aList)
    
    gb=input()
    gt=input()
    gs=input()
    gq=int(input())
    
    checkAvl=objStore.checkAvailability(gb, gt, gs, gq)
    
    if checkAvl is True: print("Size is Available")
    else: print("Size is not Available")
    
    flag=0
    
    for i in aList:
        if i.brand==gb and i.ptype==gt:
            flag=1
            
            for k in i.avail:
                print(k,":",str(i.avail[k]))
    
    if flag == 0: print("Apparel not found")

    
