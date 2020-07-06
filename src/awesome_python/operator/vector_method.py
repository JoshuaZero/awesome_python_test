#!env python
#coding=utf-8
#Author:  joshua_zero@outlook.com


from math import hypot
import click
import bisect
import random


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)".format(self.x. self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        return Vector(self.x*scaler, self.y*scaler)

@click.command()
@click.option("--h", default="", help="how to use the params for this demo")

def  demo_test():
    v_op = Vector()
    
def demo2():
    size = 7
    random.seed(1729)
    my_list=[]
    for i in range(size):
        new_item = random.randrange(size*2)
        bisect.insort(my_list, new_item)
        print("{:2d}->{}".format(new_item, my_list))


if  __name__ == "__main__":
    #demo_test()
    demo2()
