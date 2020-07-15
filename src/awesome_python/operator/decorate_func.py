#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import os 


#test 1
def decorate(func):
    pass

@decorate
def target():
    print("current run func is target()! -----1.0")

def target_l():
    print("just run target() function!----2.0")

def demo0():
    tgt = decorate(target_l())
    print(tgt)

#test 2
def deco(func):
    def inner():
        print("current run function is inner() -----3.0")
    return inner    

@deco
def target_deco():
    print("current run function is target_deco()!-----3.1")

def demo1():
    target_deco()
    print(target_deco)


#test 3

register_list= []

def register(func):
    print("current runing funciton is {}".format(func))
    register_list.append(func)
    return func

@register
def func_1():
    print("currunt running funciton is func_1()")

@register 
def func_2():
    print("current running funciton is func_2()")


def func_3():
    print("current running function is func_3()")

def func_4():
    print("current running function is func_4()")

def demo2():
    print("******demo2 function*******")
    print("register_list current function -> {}".format(register_list))
    func_1()
    func_2()
    func_3()
    func_4()







if __name__ == "__main__":
    print("==========***demo0***==========")
    demo0()
    print("==========***demo1***==========")
    demo1()
    print("==========***demo2***==========")
    demo2()
    



