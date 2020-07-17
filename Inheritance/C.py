# Python file Created By Bibhuti

from Inheritance.A import A

class C(A):
    def __init__(self,c):
        print("DEF")
        super(C,self).__init__(c);
        print("Cons C");
