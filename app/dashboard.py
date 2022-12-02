"""Main module for the streamlit app"""
import os

import numpy as np
import pandas as pd
import streamlit as st
from loguru import logger
from pages.first_page import Input_data
from pages.about import About
from pages.datatable import DataTable
from pages.suggestions import Suggestions
from utils.sidebar import sidebar_caption

# Config the whole app
st.set_page_config(
    page_title="A Dashboard Template",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache()
def fake_data():
    """some fake data"""

    df = pd.read_csv("data/cleaner_cred_score_classificaiton.csv")

    return df


def main():
    """A streamlit app template"""

    st.sidebar.title("Tools")

    PAGES = {
        "Table": DataTable,
        "About": About,
        "Mainpage": Input_data,
        "Suggestions": Suggestions
    }

    # Select pages
    # Use dropdown if you prefer
    selection = st.sidebar.radio("Pages", list(PAGES.keys()))
    sidebar_caption()

    page = PAGES[selection]

    DATA = {"base": fake_data()}

    with st.spinner(f"Loading Page {selection} ..."):
        page = page(DATA)
        page()


if __name__ == "__main__":
    main()
