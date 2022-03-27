# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:44:24 2022

@author: Avita
"""

class Book:
    def __init__(self, name,tech, ed, auth):
        self.bookName=name;self.bookTechnology=tech
        self.bookEdition=ed;self.bookAuthor=auth
        
class BookStore:
    def __init__(self, directory):
        self.bookDb=directory
        
    #given fucntion 1
    def searchByTechnology(self, technology):
        resdir=[]
        flag=0
        
        for book in self.bookDb.keys():
            if technology==self.bookDb[book].bookTechnology:
                resdir.append(self.bookDb[book])
                flag=1
            
        if flag==0:
            return None
        else:
            return resdir
    
    #given function 2
    def calculateBookWithEditionMoreThanTwo(self):
        count=0
        
        for book in self.bookDb.keys():
            if self.bookDb[book].bookEdition>=2:
                count+=1
            
        return count
    
if __name__=="__main__":
    bookdata={}
    
    bookCount=int(input())
    
    for i in range(bookCount):
        name=input()
        tech=input()
        edition=int(input())
        author=input()
        
        bookObj=Book(name, tech, edition, author)
        bookdata.update({i:bookObj})
        
    bookStoreObj= BookStore(bookdata)
    
    bts=input()
    
    count=bookStoreObj.calculateBookWithEditionMoreThanTwo()
    
    resbook=bookStoreObj.searchByTechnology(bts)
    
    if resbook==None:
        print("Book not found!")
    else:
        for k in resbook:
            print(k.bookName)
    
        
    if count==0:
        print("No book more than two editions")
    else:
        print (count)
