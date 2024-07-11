# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:46:24 2024

@author: Sushant
"""

import numpy as np
import pickle
import streamlit as st

kmeans= pickle.load(open('C:/Users/Sushant/OneDrive/Desktop/PROJECT/ML/finalized_model (1).sav', 'rb'))

def customer_seg(input_data):
    
    input_data= [[77,74]]

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = kmeans.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The customer belongs to Cluster 1'
    elif (prediction[0] == 1):
        return 'The customer belongs to Cluster 2'
    elif (prediction[0] == 2):
        return 'The customer belongs to Cluster 3'
    elif (prediction[0] == 3):
        return 'The customer belongs to Cluster 4'
    elif (prediction[0] == 4):
        return 'The customer belongs to Cluster 5'

    else:
        return 'Error'
    
def main():
    
    
    st.title('Customer Segmentation web')
    
    # CustomerID,Genre,Age,Annual Income (k$),Spending Score (1-100)
    
    CustomerID = st.text_input('CustomerID')
    Genre = st.text_input('Genre')
    Age = st.text_input('Age')
    Annual_Income = st.text_input('Annual Income ')
    Spending_Score = st.text_input('Spending Score (1-100)')
    
    customer = ''
    
    
    if st.button('custseg text result'):   
        customer = customer_seg([CustomerID,Genre,Age,Annual_Income,Spending_Score])
        
        
        
    st.success(customer)
    
    
if __name__=='__main__':
    main()