# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:52:42 2024

@author: Sushant
"""

import numpy as np
import pickle

kmeans= pickle.load(open('C:/Users/Sushant/OneDrive/Desktop/PROJECT/ML/finalized_model (1).sav', 'rb'))

input_data= [[77,74]]

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = kmeans.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
    print('The customer belongs to Cluster 1')
elif (prediction[0] == 1):
    print('The customer belongs to Cluster 2')
elif (prediction[0] == 2):
    print('The customer belongs to Cluster 3')
elif (prediction[0] == 3):
    print('The customer belongs to Cluster 4')
elif (prediction[0] == 4):
    print('The customer belongs to Cluster 5')

else:
    print('Error')