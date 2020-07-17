# Python file Created By Bibhuti

from Inheritance.A import A

class B(A):
    def __init__(self,b):
        print("ABC")
        super(B,self).__init__(b);
        print("Cons B");
