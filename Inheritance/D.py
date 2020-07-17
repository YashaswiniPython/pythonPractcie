# Python file Created By Bibhuti

from Inheritance.B import B
from Inheritance.C import C

class D(B,C):
    def __init__(self,a):
        print("Cons D", a);
        super(D,self).__init__(a);


D("TYSS");