# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 01:13:41 2021

@author: dusan
"""


#imports
from __future__ import division
import os, sys
from sklearn.linear_model import *
from sklearn.svm import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from keras.models import *
from keras.layers import Dense, Activation
from keras.optimizers import *
import threading
import numpy as np

class ANNModel(threading.Thread):
    """Threaded Neural Network Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None, save_modelname=''):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel
        self.save_modelname = save_modelname

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        for i in range(9):
            if X[:, i].std() == 0:
                X[:, i] = 1
            else:
                X[:, i] = (X[:, i] - X[:, i].mean()) / (X[:, i].std())
        #for i in range(9):
            #XT[:, i] = (XT[:, i] - XT[:, i].mean()) / (XT[:, i].std())

        model = Sequential()
        model.add(Dense(10, input_dim=9, activation="sigmoid"))
        model.add(Dense(10, activation='sigmoid'))
        model.add(Dense(1))
        sgd = SGD(lr=0.01, decay=0.000001, momentum=0.9, nesterov=True)
        model.compile(optimizer=sgd, loss='mse')
        model.fit(X, Y, validation_steps=100, batch_size=100)
        sd = model.predict(X)
        sd = sd[:, 0]
        sdList = []
        for z in sd:
            if z>=0.5:
                sdList.append(1)
            else:
                sdList.append(0)
        sdList = np.array(sdList)
        acc = (sum(sdList == Y) / len(Y) * 100)
        print("Accuracy of ANN Model: %.2f" % acc+" %")
        print('=' * 100)
        if self.accLabel: self.accLabel.set("Accuracy of Model: %.2f" % (acc)+" %")
        model.save("../models/" + self.save_modelname)
        print("success saved model")
