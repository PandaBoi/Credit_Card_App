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

    # PAGES = {
    #     "Table": DataTable,
    #     "About": About,
    #     "Mainpage": Input_data,
    #     "Suggestions": Suggestions
    # }

    # # Select pages
    # # Use dropdown if you prefer
    # selection = st.sidebar.radio("Pages", list(PAGES.keys()))
    # sidebar_caption()

    # page = PAGES[selection]

    # DATA = {"base": fake_data()}

    # with st.spinner(f"Loading Page {selection} ..."):
    #     try:
    #         page(DATA)
    #     except:
    #         page()


if __name__ == "__main__":
    main()
