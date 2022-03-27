# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:14:41 2022

@author: Avita
"""

class Professor:
    def __init__(self, pid, pname, pdic):
        self.profId=pid
        self.profName=pname
        self.subjectDict=pdic
    
class University:
    
    def getTotalExperience(self,plist,pid):
        total=0
        for prof in plist:
            if prof.profId==pid:
                for years in prof.subjectDict.values():
                    total+=years
        return total
    
    def selectSeniorsProfessorBySubject(self, plist, name):
        maxR=0
        presult=None
        
        for prof in plist:
            for name, exp in prof.subjectDict.items():
                if name.lower() == name.lower():
                    if exp>maxR:
                        maxR=exp
                        presult=prof
        return presult
    
if __name__=="__main__":
    count=int(input())
    plist=[]
    
    for i in range(count):
        pid=int(input())
        pname=input()
        
        nos=int(input())
        pdic={}
        for j in range(nos):
            sub= input()
            exp=int(input())
            pdic[sub]=exp
        
        prof= Professor(pid, pname, pdic)
        plist.append(prof)
    
    univ=University()
    
    inpid=int(input())
    name=input()
    
    totalExp=univ.getTotalExperience(plist, inpid)
    profResult=univ.selectSeniorsProfessorBySubject(plist, name)
    
    print(totalExp)
    
    if profResult is None:
        print("No Professor")
    else:
        print(profResult.profId, profResult.profName, profResult.subjectDict)
        
