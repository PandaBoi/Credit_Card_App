import streamlit as st
import pandas as pd
from utils.page import Page
from models.suggestions import SuggestionModel
class Suggestions(Page):
    def __init__(self, data, **kwargs):
        self.data = data
        self.kwargs = kwargs
        # self.train_data = pd.read_csv("app/data/clean_train.csv")
        self.model = SuggestionModel(data_path="data/cleaner_cred_score_classificaiton.csv")

    def content(self):
        """Returns the content of the page"""
        pt = self.data['base'].iloc[0]
        pt['Occupation'] = 'Scientist'
        cand_suggest = self.model.get_suggestions(pt)
        # print(cand_suggest)
        df = pd.DataFrame.from_records(cand_suggest,index=[0])
        print(f"content: {df.columns}")
        st.table(df)

        

    def title(self):
        """Returns the title of the page"""
        st.header(f"Suggestions for Profile Improvement!")
