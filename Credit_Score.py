import streamlit as st
from utils.page import Page
import numpy as np
import autokeras
import tensorflow
import tensorflow.keras.models
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import gradio as gr
import math

data = pd.read_csv(r"C:\Users\mtnag\Documents\CMU\AI_ML\Project2\cleaner_cred_score_classifier.csv")

class creditScore(Page):
    def __init__(self, data, **kwargs):
        name = "Credit Score"
        super().__init__(name, data, **kwargs)
        self.name = name
        self.data = data
        self.kwargs = kwargs
        self.modelBuilt = False

    def content(self):

        st.markdown("This is my about page.")

    def title(self):
        """Returns the title of the page"""
        st.header(f"{self.name}")

    def input(self):
        """Returns a text input"""
        self.occupation= st.text_input(label = "Occupation")
        self.age = st.text_input(label = "Age", value="0")
        self.annualIncome = st.text_input(label = "Annual Income", value="0")
        self.numBankAcc= st.text_input(label = "Number of Bank Accounts", value="0")
        self.numCreditCards = st.text_input(label = "Number of Credit Cards", value="0")
        self.numDelPay = st.text_input(label = "Number of Delayed Payments", value="0")
        self.inquiries = st.text_input(label = "Number of Credit Inquiries", value="0")
        self.debt = st.text_input(label = "Outstanding Debt", value="0")
        self.history = st.text_input(label = "Days with credit", value="0")
        self.student = st.text_input(label = "Student", value="0")
        self.inputValues = [self.occupation, self.age, self.annualIncome, self.numBankAcc, self.numCreditCards,
                            self.numDelPay, self.inquiries, self.debt, self.history, self.student]
        self.buttonPressed = st.button("Calculate Score")
        
    @st.cache(suppress_st_warning=True)
    def buildModel(self):
        self.modelBuilt = True
        cleanData = self.data.drop(labels = ["Interest_Rate","Num_of_Loan","Delay_from_due_date", "Changed_Credit_Limit","Credit_Utilization_Ratio","Total_EMI_per_month","Amount_invested_monthly","Monthly_Balance","debtconsolidation","payday","notspecified","nodata","mortgage","credit-builder","auto","personal","homeequity","Credit_Score"], axis = 1)
        #Defines what the outputs may be
        self.score = ['Poor','Standard','Good']

        # Initialize the structured data classifier.
        clf = autokeras.StructuredDataClassifier(
            max_trials=5, # We will do 10 iterations of model improvement
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

        self.loaded_model = tensorflow.keras.models.load_model("score_model_autokeras", custom_objects=autokeras.CUSTOM_OBJECTS)


    def predict(self):
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
page.buildModel()
if page.buttonPressed:
    page.predict()