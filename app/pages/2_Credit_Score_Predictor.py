import streamlit as st
from utils.page import Page
import numpy as np
import autokeras
import tensorflow
tensorflow.config.experimental_run_functions_eagerly(True)

import tensorflow.keras.models
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import gradio as gr
import math

data = pd.read_csv("data/cleaner_cred_score_classifier.csv")
data = data.drop_duplicates(subset="Customer_ID", keep = 'first', inplace=False)

st.session_state.update(st.session_state)
class creditScore(Page):
    def __init__(self, data, **kwargs):
        name = "Credit Score"
        super().__init__(name, data, **kwargs)
        self.name = name
        self.data = data
        self.kwargs = kwargs
        self.modelBuilt = False
        self.score = ['Poor','Standard','Good']

    def content(self):
        
        st.markdown("Credit Score Prediction")

    def title(self):
        """Returns the title of the page"""
        st.header(f"{self.name}")

    def input(self):
        
        st.header('Inputs')
        pt = pd.DataFrame({k:[v] for k,v in st.session_state.items()})

        self.occupation = pt['Occupation'][0]
        self.age = pt['Age'][0]
        self.annualIncome = pt['Annual_Income'][0]
        self.numBankAcc = pt["Num_Bank_Accounts"][0]
        self.numCreditCards = pt['Num_Credit_Card'][0]
        self.numDelPay = pt["Num_of_Delayed_Payment"][0]
        self.inquiries = pt["Num_Credit_Inquiries"][0]
        self.debt = pt["Outstanding_Debt"][0]
        self.history = pt["Credit_History_Age"][0]
        self.inputValues = [self.occupation, self.age, self.annualIncome, self.numBankAcc, self.numCreditCards,
                            self.numDelPay, self.inquiries, self.debt, self.history]
        pt = pt.transpose()
        st.table(pt)
        
        self.buttonPressed = st.button("Calculate Score")
        
    @st.cache(suppress_st_warning=True)
    def buildModel(self):
        self.modelBuilt = True
        cleanData = self.data.drop(labels = ["Interest_Rate","Num_of_Loan","Delay_from_due_date", "Changed_Credit_Limit","Credit_Utilization_Ratio","Total_EMI_per_month","Amount_invested_monthly","Monthly_Balance","debtconsolidation","payday","notspecified","nodata","mortgage","credit-builder","auto","personal","homeequity","Credit_Score", "student"], axis = 1)
        #Defines what the outputs may be

        # Initialize the structured data classifier.
        clf = autokeras.StructuredDataClassifier(
            max_trials=1, # We will do 10 iterations of model improvement
            overwrite=True, # Overwrite prior training attempts
        ) 

        # Fit the model to the data that we used earlier
        clf.fit(
            x = cleanData, # Measurements of cleanData2 dimensions
            y = data['Credit_Score'], # fico score
            epochs=5 # The number of iterations to train each attempted model
        )


        # Save the model
        scoreModel = clf.export_model()
        scoreModel.save("score_model_autokeras", save_format = 'tf')


    def predict(self):
        self.loaded_model = tensorflow.keras.models.load_model("models/score_model_autokeras", custom_objects=autokeras.CUSTOM_OBJECTS)
        # Make a prediction using the model. This returns a numeric integer output (e.g., 1)
        prediction = self.loaded_model.predict(self.inputValues)
        print('prediction', prediction)
        # Return the answer
        maxIndex = np.where(prediction == np.amax(prediction))[1][0]
        print(maxIndex)
        score_prediction = self.score[maxIndex]
        percent = round(prediction[0][maxIndex] * 100, 2)
        print(percent)
        # Return the answer
        if score_prediction == 'Poor':
            self.scoreRange = "There is a " + str(percent) + "% chance that your score falls between 300 - 629"
        elif score_prediction == "Standard":
            self.scoreRange = "There is a " + str(percent) + "% chance that your score falls between 630 - 719"
        elif score_prediction == "Good":
            self.scoreRange = "There is a " + str(percent) + "% chance that your score falls between 720 - 850"
        st.text_input(label = "Credit Score Range", value = self.scoreRange)


    
page = creditScore(data, test = 'testing')
page.title()
page.content()
page.input()
# page.buildModel() # can use pre-trained model after first use
if page.buttonPressed:
    page.predict()
