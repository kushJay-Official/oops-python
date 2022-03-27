# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:25:11 2022

@author: Avita
"""

'''
player has maximun wicket & min run

'''

class Player:
    def __init__(self, name, country, age, matches, runs, wickets):
        self.name=name
        self.country=country
        self.age=age
        self.matches=matches
        self.runs=runs
        self.wickets=wickets
        
class Team:
    def __init__(self, playerList):
        self.playerList=playerList
    
    def minRun(self):
        min=self.playerList[0].runs
        objPlayer=self.playerList[0]
        
        for player in self.playerList:
            if player.runs<min:
                min=player.runs
                objPlayer=player
        
        return objPlayer
    
    def maxWickets(self):
        max= self.playerList[0].wickets
        objPlayer=self.playerList[0]
        
        for player in self.playerList:
            if player.wickets>max:
                max=player.wickets
                objPlayer=player
                
        return objPlayer
    
if __name__=='__main__':
    count= int(input())
    
    playerList=[]
        
    for i in range(count):
        n=input()
        c=input()
        a=int(input())
        m=int(input())
        r=int(input())
        w=int(input())
        
        newPlayer=Player(n, c, a, m, r, w)
        
        playerList.append(newPlayer)
        
    newTeam=Team(playerList)
    
    playerMinRuns=newTeam.minRun()
    playerMaxWickets=newTeam.maxWickets()
    
    print(playerMinRuns.name)
    print(playerMinRuns.country)
    print(playerMinRuns.runs)
    
    print(playerMaxWickets.name)
    print(playerMaxWickets.country)
    print(playerMaxWickets.wickets)


    
