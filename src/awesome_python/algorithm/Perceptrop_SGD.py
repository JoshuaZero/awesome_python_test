#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import numpy as np
import pandas as pd
import sklearn 
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

class Model():
    def __init__(self):
        self.w = np.ones(len(data[0])-1, dtype=np.float32)
        self.b = 0
        self.l_rate = 0.1
        #self.data = data
    
    def sign(self, x, w, b):
        y = np.dot(x,w)+b
        return y

    def fit(self, X_traing, y_train):
        is_Wrong = False
        while  not is_Wrong:
            wrong_count = 0
            for d in range(len(X_train)):
                x = X_train[d]
                y = y_train[d]
                if y*sign(x, self.w, self.b) <= 0:
                    self.w = self.w + self.l_rate * np.dot(y,x)
                    self.b = self.b + self.l_rate * y
                    wrong_count += 1
            if wrong_count ==0:
                is_Wrong = True
        return "Preceptron Model!"    
    def score(self):
        pass


def load_data():
    #load data
    irdata = load_iris()
    df = pd.DataFrame(irdata.data, columns=irdata.feature_names)
    df['lable'] = irdata.target

    df.columns['sepal lenth','sepal width','petal lenth','petal width','label']
    df.label.value_counts()
    
    #show 
    plt.scatter(df[:50]['sepal lenth'], df[:50]['sepal width'], label='0')
    plt.scatter(df[50:100]['sepal lenth'], df[50:100]['sepal width'], label='1')
    plt.xlabel('sepal lenth')
    plt.ylabel('sepal width')
    plt.legend()
    plt.show()
    
    data = np.array(df.iloc[:100, [0,1,-1]])
    x,y = data[:,:-1], data[:,-1]
    y = [1 if i==1 else -1 for i in y]
    return x,y

def demo_test():
    x_data, y_data = load_data()
    
    perceptron = Model()
    perceptron.fit(x_data, y_data)
    x_points = np.linspace(4, 7, 10)
    y_ = -(perceptron.w[0] * x_points + perceptron.b) / perceptron.w[1]
    plt.plot(x_points, y_)

    plt.plot(data[:50, 0], data[:50, 1], 'bo', color='blue', label='0')
    plt.plot(data[50:100, 0], data[50:100, 1], 'bo', color='orange', label='1')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.legend()
    plt.show()


def demo_sklearn():
    print(sklearn.__version__)
    X_data, y_data = load_data()
    clf = Perceptron(fit_intercept=True, max_iter=1000, shuffle=True)
    clf.fit(X_data, y_data)
    print(clf.coef_)
    print(clf.intercept_)

    #show
    plt.figure(figsize=(10,10))

    # 中文标题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('鸢尾花线性数据示例')
    
    plt.scatter(data[:50, 0], data[:50, 1], c='b', label='Iris-setosa',)
    plt.scatter(data[50:100, 0], data[50:100, 1], c='orange', label='Iris-versicolor')
    
    # 画感知机的线
    x_ponits = np.arange(4, 8)
    y_ = -(clf.coef_[0][0]*x_ponits + clf.intercept_)/clf.coef_[0][1]
    plt.plot(x_ponits, y_)
    
    # 其他部分
    plt.legend()  # 显示图例
    plt.grid(False)  # 不显示网格
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    demo_sklearn()
    demo_test()
