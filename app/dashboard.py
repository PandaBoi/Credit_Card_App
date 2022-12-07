"""Main module for the streamlit app"""
import os


import streamlit as st
st.set_page_config(
    page_title="A Dashboard Template",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

import numpy as np
import pandas as pd

from loguru import logger
# from pages.first_page import Input_data
# from pages.about import About
# from pages.datatable import DataTable
# from pages.suggestions import Suggestions
# from utils.sidebar import sidebar_caption

# Config the whole app

st.session_state.update(st.session_state)

inputs = {
            'Age': 23,
            'Annual_Income': 50000,
            'Num_Bank_Accounts': 1,
            'Num_Credit_Card': 1,
            'Num_of_Delayed_Payment': 1,
            'Num_Credit_Inquiries': 1,
            'Outstanding_Debt': 5000,
            'Credit_History_Age': 200,
            'Occupation': 'Scientist',
            'prior_default': False,
            'employed': False,
            'Credit_Score': 0
        }

st.session_state.update(inputs)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

@st.cache()
def fake_data():
    """some fake data"""

    df = pd.read_csv("data/cleaner_cred_score_classificaiton.csv")

    return df


def main():
    """A streamlit app template"""

    st.sidebar.title("Welcome to CredPred!!")
    st.title("Welcome to CredPred")
    st.subheader("Our product is focused on helping you navigate the credit card score/application journey.")
    col1, col2, col3 = st.columns   ([1,1,1])

    with col1:
        st.write("")

    with col2:
        st.image(
        "https://media.giphy.com/media/3o6Mb3OomPa9u6s7IY/giphy.gif",
        width=400
    )

    with col3:
        st.write("")
    

    st.markdown(f"# Guide\n To make sure you get an awesome insight of your credit journey we have created an app that uses cutting-edge AI technology and huge oceans of data to provide you with quality insights!\n Navigate to these pages right away!:\n    1. **Fill Information** : use this page to input details about your profile that will be used to make suggestions and insights.\
    * **Credit Score** : Once your data is collected, this model \will run it through a ML model to provide you with your predicted credit score for your current profile!\
    * **Credit Card Application**: You would now want to check out how confident can you be, the next time you apply for a credit card. With a simple click you shall recieve your chances of success right away!!\
    * **Suggestions**: Did your application fail to make it through? Fear not! Our app provides you with a way to deep-dive into what could be the potential reasons behind an application being rejected, simply slick on the Suggestions tab to explore the changes you could make on your profile to make your chances incease 10-folds instantly!*\n\n\n\
    *T&C apply")

if __name__ == "__main__":
    main()
