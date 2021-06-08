# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:03:55 2021

@author: dusan
"""
#model number according to the bad bot types
IRC_detect_models = [1,2,3,4,9,10,11]
SPAM_detect_models = [1,2,5,9,13]
CF_detect_models = [1,2,9]
PS_detect_models = [3,6,8,13]
US_detect_models = [3,4,10]
HTTP_detect_models = [5,7,13]
DDOS_detect_models = [4,10,11]
P2P_detect_models = [12]

#accuracy of models

acc_model = [95.74, 96.85, 97.79, 94, 95.69, 87.4, 99.69, 93.29, 94.99, 98.21, 99.9, 90.29, 94.5]
threshold = 95.85