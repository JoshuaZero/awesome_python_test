#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from sklearn import datasets
from skimage import io
import click

class svd_test:
    def __init__(self):
        print("init the svd_test instance!")

    def getImgAsMat(self,index):
        ds = datasets.fetch_olivetti_faces()
        return np.mat(ds.images[index])

    def getImgAsMatFromFile(self,filename):
        img = io.imread(filename, as_grey=True)
        return np.mat(img)

    def plotImg(self, imgMat):
        plt.imshow(imgMat, cmap=plt.cm.get_cmap())
        plt.show()
    
    def recoverBySVD(self,imgMat, k):
        U,s,V = la.svd(imgMat)
        Uk = U[:,0:k]
        Sk = np.diag(s[0:k])
        Vk = V[0:k, :] 
        imgMat_new = Uk*Sk*Vk
        return imgMat_new


@click.command()
@click.option("--img_file",default="./img.jpg", help="the original img file")
@click.option("--k", default=30, help="the svd param ")

def svd_demo(img_file, k):
    svd_op = svd_test()
    img = svd_op.getImgAsMatFromFile(img_file)
    svd_op.plotImg(img)
    img_new = svd_op.recoverBySVD(img, k)
    svd_op.plotImg(img_new)


if __name__ =="__main__":
    svd_demo()
