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

    st.sidebar.title("Welcome to our page")



if __name__ == "__main__":
    main()
