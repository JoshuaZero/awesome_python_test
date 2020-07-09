#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class lineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
     
    def total(self):
        return self.product * self.price


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total    

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount    

    def __repr__(self):    
        fmt = '<Order total: {:.2f}, due: {:.2f}>'
        return fmt.foramt(self.total(), self.due())


class Promotion(ABC):   #策略  抽象基类
    @abstractmethod
    def discount(self,order):
        """return discount order (+ value)"""


class FidelityPromo(Promotion):    
    """为积分1000以上的客户5%的折扣"""
    def discount(self, order):
        return self.total()*0.05 if order.customer.fidelity >= 1000

class BulkItemPromo(Promotion):
    """单个单品为20个以上是打10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += self.total()*0.1
        return discount        

class LargeOrderPromo(Promotion):
    """订单中不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        discount = 0
        distint_item = {item.product for item in order.cart}
        if len(distint_item) >= 10:
            discount = self.total()*0.07
        return discount    
