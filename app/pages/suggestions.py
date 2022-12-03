import streamlit as st
import pandas as pd
from utils.page import Page
from models.suggestions import SuggestionModel
from millify import millify
import matplotlib.pyplot as plt
import numpy as np
class Suggestions(Page):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        # self.train_data = pd.read_csv("app/data/clean_train.csv")
        self.model = SuggestionModel(data_path="data/cleaner_cred_score_classificaiton.csv")

    def content(self):
        """Returns the content of the page"""
        pt = pd.DataFrame({k:[v] for k,v in st.session_state.items()})
        # st.table(pt)
        # pt = self.data['base'].iloc[0]
        print(pt)
        cand_suggest = self.model.get_suggestions(pt)
        # print(cand_suggest)
        df = pd.DataFrame.from_records(cand_suggest,index=[0])
        print(f"content: {df.columns}")
        # st.table(df)
        i = 0
        difs = {}
        for col in list(df.columns):
            cols = st.columns(3)
            print("doing ",col)
            dif_per = (df[col].values[0] - pt[col].values[0])/pt[col].values[0]*100
            difs[col] =dif_per
            helper = f"user input: {pt[col].values[0]}\n\
                        Predicted value: {df[col].values[0]}"
            cols[i].metric(col, millify(df[col].values[0]),delta=f"{dif_per:.2f}%", help=helper)
            i += 1
            i %= 3
        
        difs.pop('Age')
        fig, ax = plt.subplots()
        colors = ['r' if difs[k] < 0 else 'g' for k in difs.keys()]
        bars = ax.barh(list(range(len(difs.values()))),np.array(list(difs.values()))/100,color=colors)
        ax.bar_label(bars)
        ax.set_yticks(list(range(len(difs.values()))), difs.keys())
        ax.set_xlim(-10,10)
        st.pyplot(fig)



        # st.bar_chart(dif_df.transpose())        

    def title(self):
        """Returns the title of the page"""
        st.header(f"Suggestions for Profile Improvement!")

if __name__ == '__main__':
    page = Suggestions()
    page()