# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:44:24 2022

@author: Avita
"""

class Account:
  def __init__(self,ac,acn,acb):
    self.accntNo=ac
    self.accntName=acn
    self.accntBalance=acb
    
class AccountDemo:
  def __init__(self):
    pass
  def depositAmnt(self,Account, amount):
    dep=Account.accntBalance=Account.accntBalance+amount
    return dep
  def withdrawAmnt(self,Account, amount):
    res= Account.accntBalance=Account.accntBalance-amount
    if res<1000:
      return "No Adequate balance"
    else:
      return res



#Sample main section. 
#Do not remove the below portion of code. 
if __name__ == '__main__':
    acno=int(input())
    acname=input()
    acntbal=int(input())
    depamnt=int(input())
    withamnt=int(input())
    
    acnt=Account(acno,acname,acntbal)
    acntdemoobj=AccountDemo()
    
    
    print(acntdemoobj.depositAmnt(acnt,depamnt))
    print(acntdemoobj.withdrawAmnt(acnt,withamnt))
            