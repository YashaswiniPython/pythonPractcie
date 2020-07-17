# #writing
# # f=open("file.txt","w")
# # f.write("read\n")
# # f.write("write\n")
# # f.write("append\n")
# # f.close()
#
# # reading full data
# # f=open("file.txt","r")
# # data=f.read(8)
# # print(data)
# # f.close()
#
# # reading with n number of characters
# # f=open("file.txt","r")
# # data=f.read(8)
# # print(data)
# # f.close()
#
# # reading line by line
# # f=open("file.txt","r")
# # print(f.readline(),end='') # end will not allow one space between
# # print(f.readline(),end='')
# # print(f.readline(),end='')
# # f.close()
#
# #print data in list
# # f=open("file.txt","r")
# # list=f.readlines()
# # print(list)
# # f.close()
#
# #print data in list
# # f=open("file.txt","r")
# # list=f.readlines()
# # for line in list:
# #     print(line,end="")
# # f.close()
#
# # s= "hello python"[::-1]
# # print(s)
#
# # fibonacci series
# # def fibonacci(n):
# #     if n<0:
# #         print("incorrect option")
# #     elif n==1:
# #         return 0
# #     elif n==2:
# #         return 1
# #     else:
# #         return fibonacci(n-1)+fibonacci(n-2)
# # print(fibonacci(9))
#
# # fibonacci using generators:
# # def fib(num):
# #     a,b=0,1
# #
# #     while True:
# #         yield a
# #         a,b=b,a+b
# # values=fib(20)
# # for f in values:
# #     print(f)
#
# def countdown(num):
#     # print("countdown starts now")
#     while(num>0):
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x)
#
# # def first_n(num):
# #     n=1
# #     while n<=num:
# #         yield n
# #         n=n+1
# # values=first_n(5)
# # for i in values:
# #     print(i)
#
#
# # random name
# # from random import *
# # import time
# # def random_name():
# #     alphabets="abcdefghijklm"
# #     while True:
# #         name=""
# #         for i in range(5):
# #             name+=choice(alphabets)
# #         yield name
# # for i in random_name():
# #     time.sleep(2)
# #     print(i)
# #     break
#
# # def last_num(num):
# #     n=6
# #     while n<=num:
# #         yield n
# #         n=n+1
# # for i in last_num(10):
# #     print(i)
#
# def countdown(num):
#     print("count down starts")
#     num=1
#     while num>0:
#         yield num
#         num=num-1
# for i in countdown(10):
#     print(i)

# from random import *
# names=['sun','moon','saturn','jupitor']
# subjects=['english','hindi','python','physics']
# def people_list(num):
#     results=[]
#     for i in range(num):
#         person={'id',i,'names',choice(names),'subjects',choice(subjects)}
#         results.append(person)
#     return results
# print(people_list(9))

# def Bigboss(func):
#     def list_contestants():
#         print('#'*20)
#         func()
#         print("Kuri pratap")
#         print("Raju")
#         print("Kishan")
#         print("Deepika")
#         print("chandana")
#         print('#'*20)
#     return list_contestants
# @Bigboss
# def Bigboss():
#     print("Bigboss welcomes contestants")
# Bigboss()

'''def decor(func):
    def inner(a,b):
        print("division of two numbers is")
        print("divide {} with {}".format(a,b,a/b))
        if b==0:
            print("zero number is not divisible")
        else:
            func()
    return inner
@decor
def division(a,b):
    print(a/b)

division(10,0)'''

'''def countdown(num):
    num=1
    while(num>0):
        yield num
        num=num-1
values=countdown(10)
for i in values:
    print(i)'''

'''def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    if f<10:
        print(f)
    else:
      break'''

# def decor(f1):
#     def inner(name):
#         if name=="anu":
#             print("please come fast for taking class")
#             print("timings 9.30")
#         else:
#             f1(name)
#     return inner
# @decor
# def wish(name):
#     print("good morning")
# wish("yashu")

# def decor(func):
#     def inner(a,b):
#         print("*"*50)
#         print("insert first number a:",a)
#         print("insert first number b:", b)
#         print("Addition of a + b =",a+b)
#         print("*" * 50)
#     return inner
#
# def sum(a,b):
#     print(a+b)
# values=decor(sum)
#
# values(20,30)

# def decor(func):
#     def inner(a,b):
#         if b==0:
#             print("zero cannot be divided")
#         else:
#             print("result is:")
#             return func(a,b)
#     return inner
#
# def division(a,b):
#     print(a/b)
# values=decor(division)
# division(10,2)

# def decor1(func):
#     def inner1():
#         x=func()
#         return x*x
#     return inner1
# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
# @decor1
# @decor
# def maths():
#     return 10
# print(maths())


