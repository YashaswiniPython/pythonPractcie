#decorators
'''def amazon(Func):
    def login():
        print("your name")
        print("password")
        Func()
    return login
@ amazon
def home():
    print("welcome Yashu")
home()'''

#with parameters
'''def amazon(Func):
    def login(name,pwd):
        print("your name",name)
        print("password",pwd)
        Func(name,pwd)
    return login
@ amazon
def home(name,pwd):
    print("welcome Yashu")
home("yashu","123")'''

# second example for decoratores
'''def Eventmanagement(nimajji):
    def Birthday_party_menu():
        print("welcome drinks")
        print("welcome roses")
        nimajji()
    return Birthday_party_menu

@ Eventmanagement
def children():
    print("give bday caps for chidrens")
    print("engage with games")
children()'''

# def bigboss(season):
#     def s1_winner(name):
#         print("season1 winner is:",name)
#         season(name)
#     return s1_winner
# @bigboss
# def s2_winner(name):
#     print("s2 winner is",name)
# s2_winner("Pratham")

'''def sunnydecor(func):
    def inner(name):
        if name == "sunny":
            print("hello sunny")
            func(name)
        else:
            func(name)
    return inner
@sunnydecor
def outer(name):
    print("i love you",name)
outer("sunny")'''

# def decor(func):
#     def inner(a,b):
#         print("divde {} with {} and result is {}".format(a,b,(a/b)))
#         if b==0:
#            print("dont divide anything by 0")
#            return
#         else:
#            return func(a,b)
#     return inner
# @decor
# def division(a,b):
#     return a/b
# division(10,2)

#without decor

'''def decor(func):
    def inner(a,b):
        print("divde {} with {} and result is {}".format(a,b,(a/b)))
        if b==0:
           print("dont divide anything by 0")
           return
        else:
           return func(a,b)
    return inner

def division(a,b):
    return a/b
division_result=decor(division) # assigning decorator for variable and acheieving.
print(division(10,2))
print(division(10,0))'''

#decorator chanining

'''def decor2(func):
    def inner2():
        print("hello")
    return inner2

def decor1(func):
    def inner1():
        print("yashu")
    return inner1


@decor1
@decor2
def outer():
    print("original function")
outer()'''

#decorator chaining

'''def decor(func):
    def inner():
        x=func()
        return 2+x
    return inner
def decor1(func):
    def inner1():
        x=func()
        return 10*x
    return inner1
@decor1
@decor
def num():
    return 10
print(num())'''








