import pandas as pd
import streamlit as st
from utils.page import Page
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import math
import pycaret
from pycaret.regression import *
st.session_state.update(st.session_state)
data = pd.read_csv('data/crx.data', header = None)

class CreditCardApp(Page):
    def __init__(self, data, **kwargs):
        name = "Credit Card Prediction"
        print('innit mate')
        super().__init__(name, data, **kwargs)
        self.name = name
        self.data = data
        self.kwargs = kwargs
        
    def title(self):
        st.title(f"{self.name}")
        
    #runs all page functions
    def content(self):
        testPage.cleanData()
        testPage.convertData()
        testPage.inputs()
    
        
    #pulls all the inputs needed from the session state 
    def inputs(self):
        print('starting inputs')
        st.header('Inputs')
        st.markdown('If the inputs are wrong, please go back to the fill information page')
        col11, col12, col13 = st.columns(3)
        col21, col22, col23 = st.columns(3)
        col11.metric('Age', st.session_state['Age'])
        col12.metric('Debt', st.session_state['Outstanding_Debt'])
        col13.metric('Have you previously been defaulted?', st.session_state['prior_default'])
        col21.metric('Are you employed?', st.session_state['employed'])
        col22.metric('Credit Score', st.session_state['Credit_Score'])
        col23.metric('Income', st.session_state['Annual_Income'])
        pt = pd.DataFrame({k:[v] for k,v in st.session_state.items()})
        self.age = pt['Age'][0]
        self.debt = pt['Outstanding_Debt'][0]
        self.creditScore = pt['Credit_Score'][0]
        self.income = pt['Annual_Income'][0]
        priorD = pt['prior_default'][0]
        emp = pt['employed'][0]
        if priorD:
            self.priorDefault = 0
        else:
            self.priorDefault = 1
        if emp:
            self.employed = 0
        else:
            self.employed = 1
        inps = [self.age, self.debt, self.creditScore]
        self.calculate = st.button('Predict Application Outcome')
        if self.calculate:
            self.buildModel()
            self.predict()
           
    #cleans the raw data so that only the useful columns for the model are kept
    def cleanData(self):
        st.header('Cleaning your data...')
        tempData = self.data
        
        tempData.columns = ['Gender', 'Age', 'Debt', 'Married', 'Bank Customer', 'Education Level', 
                'Ethnicity', 'Years Employed', 'Prior Default', 'Employed', 'Credit Score', 
                 'Drivers License', 'Citizen', 'Zip Code', 'Income', 'Approval Status']

        cleanData = tempData.drop(labels = ['Gender', 'Married', 'Bank Customer', 'Education Level', 
                                            'Ethnicity', 'Years Employed', 'Drivers License', 
                                            'Citizen', 'Zip Code'], axis = 1)
        self.data = cleanData
    
    #converts the data into useable data
    def convertData(self):
        cleanData = self.data
        n = len(cleanData["Approval Status"])-1
        tempData = pd.DataFrame(index=pd.RangeIndex(n+1), columns = ['Age', 'Debt', 'Prior Default', 'Employed', 'Credit Score', 'Income', 'Approval Status'])
        for col in cleanData:
            if type(cleanData[col][0]) == np.float64:
                tempData[col] = cleanData[col]
            elif type(cleanData[col][0]) == np.int64:
                tempData[col] = cleanData[col]
                # tempData[col].astype(float)
                for i in range(n):
                    tempData[col][i] = tempData[col][i].astype(np.float64)
            else:
                for i in range(n):
                    uVals = cleanData[col].unique()
                    uVals = uVals.tolist()
                    tempData[col][i] = uVals.index(cleanData[col][i]) + 0.0

                tempData[col].astype(float)

        for i in range(n):
            if tempData['Credit Score'][i] == 0:
                tempData['Credit Score'][i] = np.nan

        tempData['Credit Score'].fillna(tempData['Credit Score'].mean(), inplace=True)
        inspectData = tempData['Credit Score']
        for i in range(n):
            if tempData['Credit Score'][n] == np.nan:
                tempData['Credit Score'][n] = 300
            elif tempData['Credit Score'][n] != 0:
                tempData['Credit Score'][n] = np.log10(tempData['Credit Score'][n])
                tempData['Credit Score'][n] = tempData['Credit Score'][n]*850
            else:
                tempData['Credit Score'][n] = 300
        self.data = tempData

    #builds the model using PyCaret
    def buildModel(self):
        st.header('Building your model...')
        tempData = self.data

        tempData.drop(tempData.tail(1).index, inplace=True)
        cat_cols = ['Age', 'Debt', 'Prior Default',
                    'Employed', 'Credit Score', 'Income']
        print('before settings')
        settings = setup(data=tempData,
                         target='Approval Status',
                         session_id=123,
                         normalize=True,
                         numeric_features=cat_cols,
                         normalize_method='minmax',
                         silent=True
                         )

        print('done setup')
        top1 = compare_models(n_select=1)
        save_model(top1, "best_model")
        self.applicationModel = load_model("best_model")
    
    #uses model that was build to predict the outcome of the application
    def predict(self):
        inputList = [self.age, self.debt, self.priorDefault, self.employed, self.creditScore, self.income]
        d = {'Age': [self.age], 'Debt': [self.debt], 'Prior Default': [self.priorDefault], 'Employed': [self.employed],
             'Credit Score': [self.creditScore], 'Income': [self.income]}
        print('d', d)
        testData = pd.DataFrame(data=d)
        print('testData', testData)
        prediction = predict_model(self.applicationModel, testData)
        outcome = prediction["Label"][0]
        print('dataFrame Made')
        print('outcome', outcome)
        if outcome < 0.5:
            out = 'Not Approved'
            st.header('You are unlikely to be approved. Check suggestions page for recommendations')
        elif outcome >= 0.5:
            out = 'Approved'   
            st.header('Congratulations! You are likely to be approved!')
        self.prediction = out
    
        
testPage = CreditCardApp(data, test='testing')

testPage()
