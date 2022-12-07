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
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        st.write("")

    with col2:
        st.image(
       # "https://giphy.com/embed/mGNO9zHJpV9JOVRz1L",
       "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAq1BMVEX///8jO5FBwPMAKIrLz+E1vfOu4vkWMo7J7Pt7hrj8/Pz5+fn19fUQL40fOJCXn8Pt7e0qQpYySJnX2unm5ubw8PDg4+/p6el30Pafp8ttebDe3t4AGocADITDxtvc3Nzx8vgAH4gAF4bx+v7n9v0AKosAJIno6vNTYqNndK1dyPS+5/rU7/uI1Pen3/m/6PsAAIK9wtqCjLpBU52PmMGutdJNXaG1utVzfrG4FGI8AAAEOUlEQVR4nO3b8VuaQBgHcBSMqTuM2Fg2c+ASq7VWZqv//y/bnQIeCAHjddex7+cXYS173m93x3v3mGEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICuvt99IPBddRmETm4HNG5/qC6FyF1/0KcyOFddDYkTukREKD9V10PgB2kkPJQ71RW1dkUcSRcGyjl1Jv2+6pLaIh8m3Eh1US3d/9+Z3J+nfvGldXdFn0j/VnWhDdymQ2Lw4SjrSPzmOq2x+xAGVzyhI0XSH5yoLrS+K6kF5/sboma+gEb9ydX9SYpnIt3Ruu/SRhAAylj/wkp1lY34D+bxPXiqy2xkbvaOzw5Ul9nIhDlvI4jEOVNdZTOv7tnbCDKxb1RXSYxgoLCJ6iJoBWH7TJaPqqugZRGswaavuooaRlzyKq5GpYxn1j4TZ6y64Gor23UZbxnWjuu69tTwmVuqfSI950l1wTVYkeOE/Hf3JJ61kWU8mkd9FNtD1QXXMGW7lmE7LaKVsSGYH29gU9UF13AzM2e8ZfAvI9OMZoZxHWZb8V1ELHv790xLdcE1+J7n8V1Z4G0ZhpezXVfZc+a2haVeO8Bi2xDCILmdtsvE6SkrhNDazlTyatcs3palq7NzrbAUMr95Pc5+j/JU7+GzvL6Qucl32RuFpVQZbyYlNuJ8Y5reutvfbnpfb5gsX7I/LUhmHHtWUm091oKVWPBMRvvb3ZDP3lZOnIPGrBcPFPM9Hyg9L8sKYgFvbsNatZdmchGsBPGDthd+8tPEm79bQ9MuxsR6Og+z/9g0FDYTIrEFDhfiKgnLVV33WybDdbGhaDTnua82jMReTwUWvhjB9uoinjodOlAaNxwoy2D7bR6bxUvqJn6DDh0oeQ3PTVzLsyzLN3xnNhFX3u9kie3OgdJLw+bVvuQe+JhYuQtxuUjaEy0OlFKB7/ur3cuB1brZ3LFfrTknHjuBuJinmyRbo08oGcbFLFrwHvN1FhVouJywXMeWzj0tDpT2zpzecl67da/IJH9GchOHqsWBUmrMnF7EJ3tIEInY1Uxl12lnr8OBUsrjrf7l7iXRZsTYmd1C+k5aHCjtjTIvAsUhfY4ZKKmNTsvTowKaLbEF6MeJmX8eaceLqqtsRP9hQvRcliLRq4ktNg9JI4n0euiU2ERkI8VZuh0YJcKjG7GSo6dGWNTrziHByJoMCUwtrfZ+AAAA783+U37jCtLnATsnl8BH2edimf+TT0l1PW3IUeQzOJV8yZK/dJoPSQpHdXmNSXlkwpBT+FRBjigTjZbBFCci5ZHW/TX2LRHfZ4ORc5FS0S+Uw1FSFEqaiuxTRSRaZmLIsRTNnor5k1tbymaOXonEMk+coofNaYnCh5DuaeQdtiQfqx00K6qrOLLyv9jocq8GAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACV/gAp/6F7PeSbgAAAAABJRU5ErkJggg==",
       width=600
       )

    with col3:
        st.write("")
   
    
    #st.sidebar.title("Welcome to CredPred!!")
        #st.title("<h1 style='text-align: center; color: red;'>Some title</h1>")

    st.title("Welcome to CredPred!")
    st.subheader("Improving your credit journey")
    st.markdown("**Introduction**")

    st.markdown(f"To make sure you get an awesome insight of your credit journey we have created an app that uses cutting-edge AI technology and huge oceans of data to provide you with quality insights!\n Navigate to these pages right away!\n    \n * **Fill Information** : use this page to input details about your profile that will be used to make suggestions and insights.\
    \n * **Credit Score**: Once your data is collected, this model will run it through a ML model to provide you with your predicted credit score for your current profile!\
    \n * **Credit Card Application**: You would now want to check out how confident can you be, the next time you apply for a credit card. With a simple click you shall recieve your chances of success right away!!\
    \n * **Suggestions**: Did your application fail to make it through? Fear not! Our app provides you with a way to deep-dive into what could be the potential reasons behind an application being rejected, simply slick on the Suggestions tab to explore the changes you could make on your profile to make your chances incease 10-folds instantly!*\n\n\n\
    *T&C apply")

if __name__ == "__main__":
    main()
