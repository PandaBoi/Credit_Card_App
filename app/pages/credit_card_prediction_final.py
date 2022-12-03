import pandas as pd
import streamlit as st
from utils.page import Page
#from pages.first_page import Input_data
import numpy as np
#import sklearn.datasets
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import math
import pycaret
from pycaret.regression import *

data = pd.read_csv('data/crx.data', header = None)
#pressed = False
class CreditCardApp(Page):
    def __init__(self, data, **kwargs):
        name = "Credit Card Prediction"
        print('innit mate')
        super().__init__(name, data, **kwargs)
        self.name = name
        self.data = data
        self.kwargs = kwargs
        #self.buttonStatus = False
        #st.title('Credit Card Application Predictor')
        
    def title(self):
        #print('start')
        st.title(f"{self.name}")
        
    def content(self):
        st.header("This is my page content")
    
    #def defineVariables(self):
        
    
    def inputs(self):
        st.header('Inputs')
        st.write('session state age', st.session_state['Age'])
        st.write('session state debt', st.session_state['Outstanding_Debt'])
        st.write('session state prior default', st.session_state['prior_default'])
        st.write('session state employed', st.session_state['employed'])
        st.write('session state credit score', st.session_state['Credit_Score'])
        st.write('session state income', st.session_state['Annual_Income'])
        pt = pd.DataFrame({k:[v] for k,v in st.session_state.items()})
        #print('credit score', pt['Credit_Score'])
        #st.write(pt)
        #print('pt', pd)
        #self.age = st.number_input('Age', min_value=0)
       # self.age = st.session_state['Age']
        self.age = pt['Age'][0]
        #self.debt = st.session_state['Outstanding_Debt']
        self.debt = pt['Outstanding_Debt'][0]
        #self.creditScore = st.session_state['Credit_Score']
        self.creditScore = pt['Credit_Score'][0]
        #self.income = st.session_state['Annual_Income']
        self.income = pt['Annual_Income'][0]
        #priorD = st.session_state['prior_default']
        priorD = pt['prior_default'][0]
        #emp = st.session_state['employed']
        emp = pt['employed'][0]
        #self.age = Input_data.age
        #self.debt = st.number_input('Debt', min_value=0)
        #self.
        #priorD = st.checkbox('Check if you have defaulted in the past')
        if priorD:
            self.priorDefault = 0
        else:
            self.priorDefault = 1
        #emp = st.checkbox('Check if you are employed')
        if emp:
            self.employed = 0
        else:
            self.employed = 1
        inps = [self.age, self.debt, self.creditScore]
        #print('inputs made')
        #print('inputs', inps)
        #self.creditScore = st.number_input('Credit Score', min_value=300, max_value=850)
        #self.income = st.number_input('Income', min_value=0)
        self.calculate = st.button('Predict Application Outcome')
        if self.calculate:
            print('calculating...')
           # st.write('session state age', st.session_state['Age'])
           # st.write('session state debt', st.session_state['Outstanding_Debt'])
           # st.write('session state prior default', st.session_state['prior_default'])
           # st.write('session state employed', st.session_state['employed'])
           # st.write('session state credit score', st.session_state['Credit_Score'])
           # st.write('session state income', st.session_state['Annual_Income'])
            self.buildModel()
            self.predict()
           
        
    def cleanData(self):
        #print('printing data')
       # print(self.data)
        tempData = self.data
        
        tempData.columns = ['Gender', 'Age', 'Debt', 'Married', 'Bank Customer', 'Education Level', 
                'Ethnicity', 'Years Employed', 'Prior Default', 'Employed', 'Credit Score', 
                 'Drivers License', 'Citizen', 'Zip Code', 'Income', 'Approval Status']

        cleanData = tempData.drop(labels = ['Gender', 'Married', 'Bank Customer', 'Education Level', 
                                            'Ethnicity', 'Years Employed', 'Drivers License', 
                                            'Citizen', 'Zip Code'], axis = 1)
        self.data = cleanData
       
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


    def buildModel(self):
        tempData = self.data
        xData = tempData.drop(labels=["Approval Status"], axis=1)
        yData = tempData["Approval Status"].to_frame()

        tempData.drop(tempData.tail(1).index, inplace=True)
        yData.drop(yData.tail(1).index, inplace=True)
        cat_cols = ['Age', 'Debt', 'Prior Default',
                    'Employed', 'Credit Score', 'Income']
        print('before settings')
        settings = setup(data=tempData,
                         target='Approval Status',
                         session_id=123,
                         normalize=True,
                         numeric_features=cat_cols,
                         normalize_method='minmax'
                         )

        print('done setup')
        top1 = compare_models(n_select=1)
        save_model(top1, "best_model.pkl")
        self.applicationModel = load_model("best_model.pkl")
        #return applicationModel
    
    def predict(self):
        
        inputList = [self.age, self.debt, self.priorDefault, self.employed, self.creditScore, self.income]
        
        d = {'Age': [self.age], 'Debt': [self.debt], 'Prior Default': [self.priorDefault], 'Employed': [self.employed],
             'Credit Score': [self.creditScore], 'Income': [self.income]}
        print('d', d)
        testData = pd.DataFrame(data=d)
        print('testData', testData)
        prediction = predict_model(self.applicationModel, testData)
        outcome = prediction["Label"][0]
        #print("test data", testData)
        print('dataFrame Made')
        print('outcome', outcome)
        #prediction = predict_model(applicationModel, testData)
        if outcome < 0.5:
            out = 'Not Approved'
        elif outcome >= 0.5:
            out = 'Approved'    
        st.text_area('Application Prediction', out)
    
    
testPage = CreditCardApp(data, test='testing')

testPage.title()
testPage.content()
testPage.cleanData()
testPage.convertData()
#testPage.buildModel()
testPage.inputs()
#applicationModel = testPage.buildModel()
#testPage.predict()
