# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 07:58:56 2021

@author: dusan
"""

import tensorflow as tf
import keras
import numpy as np
import pickle

import setting

#get predicted result of models(1~13) 
#return value: one-hot prediction value array
def get_result_models(_input_data):
    result = []
    for i in range(13):
        model_path = "../models/" + str(i+1)
        model = tf.keras.models.load_model(model_path)
        for z in range(9):
            if _input_data[:,z].std() == 0:
                _input_data[:,z] = 1
                
            else:
                _input_data[:,z] = (_input_data[:, z] - _input_data[:, z].mean()) / (_input_data[:, z].std())
        
        predict_val = model.predict(_input_data)
        predict_val = predict_val[:,0]
        _isbot = []
        for _x in predict_val:
            if _x >0.5:
                _isbot.append(1)
            else:
                _isbot.append(0)
        
        result.append(_isbot)
    return result

#get fusion model's prediction val

def predict(_models_result):
    acc_array = setting.acc_model
    result = []
    trans_m = np.transpose(_models_result)
    for x in trans_m:
        _temp = 0
        for z in setting.CF_detect_models:
            _temp += x[z-1] * acc_array[z-1]
            
        _threshold = _temp/3
        if _threshold >setting.threshold:
            result.append(1)
            continue
        
        _temp = 0
        for z in setting.DDOS_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/3
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.SPAM_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/5
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.HTTP_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/3
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.PS_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/4
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.P2P_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/1
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.US_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/3
        if _threshold >setting.threshold:
            result.append(1)
            continue

        _temp = 0
        for z in setting.IRC_detect_models:
            _temp += x[z-1] * acc_array[z-1]
        _threshold = _temp/7
        if _threshold >setting.threshold:
            result.append(1)
            continue
        else:
            result.append(0)
        
    return result

