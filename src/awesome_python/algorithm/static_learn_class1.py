#!env python
#coding=utf-8
#Author:  joshua_zero@outlook.com



import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib 
"""
class static_learn_cls1():
    def __init__(self):
        print("init") 

    def real_func(self, x):
        return np.sin(2*np.pi*x)

    def fit_func(self, p, x):
        f = np.ploy1d(p)
        return f(x)

    def residuals_func(self, p, x, y):
        ret = fit_func(p,x) - y
        return ret
"""

def real_func(x):
    return np.sin(2*np.pi*x)

def fit_func(p, x):
    f = np.ploy1d(p)
    return f(x)

def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret


def fitting(x, y, points, M=0):
    """
      M 为多项式的次数
    """
    #随机初始化多项式参数
    p_init = np.random.rand(M+1)
    #最小二乘法
    p_lsq = leastsq(residuals_func,p_init,args=(x,y)）
    print("Fitting Parameters: {}".format(p_lsq[0]))

    #show 
    plt.plot(points, real_func(points), label='real')
    plt.plot(points, fit_func(p_lsq[0], points), label='fitted curve') 
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    plt.show()                
    return p_lsq

def demo_test1():
    x = np.linspace(0,1,10)
    x_points = np.linspace(0,1,1000) 
    y_ = real_func(x)
    y = [np.random.normal(0,0.1) + y1 for y1 in y_ ]
    """
      M 为多项式的次数
    """
    #随机初始化多项式参数
    p_init = np.random.rand(M+1)
    #最小二乘法
    p_lsq = leastsq(residuals_func,p_init,args=(x,y)）
    print("Fitting Parameters: {}".format(p_lsq[0]))

    #show 
    plt.plot(points, real_func(points), label='real')
    plt.plot(points, fit_func(p_lsq[0], points), label='fitted curve') 
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    plt.show()                
    return p_lsq
    #fitting(x,y,x_points, 0)   

if __name__ == "__main__":
    demo_test1()
