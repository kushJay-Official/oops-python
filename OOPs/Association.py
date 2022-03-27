class A:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def addNums(self):
        return self.b+self.c

class B:
    def __init__(self, b,c):
        self.b=b
        self.c=c

    def addAllNums(self,a,b):
        return self.b+self.c+a+b


if __name__=="__main__":
    ting=A('yo',5,6)
    ling=B(3,4)
    print(ling.addAllNums(ting.b,ting.c))

