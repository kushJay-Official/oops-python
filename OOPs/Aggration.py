# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:29:40 2022

@author: Avita
"""

class Salary:
    def __init__(self, pay, bounus):
        self.pay=pay
        self.bounus=bounus
    
    def annualSalary(self):
        return (self.pay*12)+self.bounus
    
class Empolyee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.objSalary=salary
        
    def totalSalary(self):
        return self.objSalary.annualSalary()
    
#main function
if __name__ == '__main__':
    salary=Salary(15000,10000)
    emp=Empolyee('test',25,salary)
    
    salary1=Salary(25000,10000)
    emp1=Empolyee('xtx',25,salary1)
    
    print(emp.totalSalary())
    print(emp1.totalSalary())
