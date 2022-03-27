# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:07:15 2022

@author: Avita
"""

class Employee:
    def __init__(self, id, name, age,gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        
class Organization:
    def __init__(self, name, empList):
        self.name=name
        self.empList=empList
        
    def addEmp(self, id, name, age, gender):
        empTemp=Employee(id, name, age, gender)
        self.empList.append(empTemp)
      
    def viewEmp(self):
        for i in self.empList:
            print("-------------")
            print(i.id)
            print(i.name)
            print(i.age)
            print(i.gender)
            print("-------------")
    
    def getEmpCount(self):
        return len(self.empList)
    
    def findAgeById(self,id):
        age=-1
        for i in self.empList:
            if i.id==id:
                age=i.age
                break
        return age;
    

if __name__=="__main__":
    empList=[]
    o=Organization("TCS", empList)
    
    #input 
    n=int(input())
    
    for i in range(n):
        id=int(input())
        name=input()
        age=int(input())
        gender=input()
        o.addEmp(id, name, age, gender)
        
        
    o.viewEmp()
    
    print(o.getEmpCount())
    
    
    print(o.findAgeById(int(input())))
    
  
    