import streamlit as st
import pandas as pd
from utils.page import Page
from models.suggestions import SuggestionModel
from millify import millify
import matplotlib.pyplot as plt
import numpy as np

st.session_state.update(st.session_state)

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(172, 56, 190, 0.61);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: white;
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   font-size: 10000px;
   color: rgba(247, 255, 10, 0.9);
   
}
</style>
"""
, unsafe_allow_html=True)
class Suggestions(Page):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.model = SuggestionModel(data_path="data/cleaner_cred_score_classificaiton.csv")

    def content(self):
        """Returns the content of the page"""

        # convert session state to dataframe
        pt = pd.DataFrame({k:[v] for k,v in st.session_state.items()})

        # retreive suggestions from model
        cand_suggest = self.model.get_suggestions(pt)

        # convert suggestions to dataframe
        df = pd.DataFrame.from_records(cand_suggest,index=[0])
        
        # display suggestions in metrics
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
        
        # display suggestions in plot
        difs.pop('Age')
        fig, ax = plt.subplots()
        colors = ['r' if difs[k] < 0 else 'g' for k in difs.keys()]
        bars = ax.barh(list(range(len(difs.values()))),np.array(list(difs.values()))/100,color=colors)
        ax.bar_label(bars)
        ax.set_yticks(list(range(len(difs.values()))), difs.keys())
        ax.set_xlim(-10,10)
        ax.set_xlabel('xtimes change from current value')
        ax.set_ylabel('Attribute')
        st.pyplot(fig)



        # st.bar_chart(dif_df.transpose())        

    def title(self):
        """Returns the title of the page"""
        st.header(f"Suggestions for Profile Improvement!")
        st.markdown("Please scroll to find suggestions made by our model based on your inputs in the previous two pages. If you would like to see how an input changes the suggestions, please head to \"Fill Information\" page to input your new data!")


if __name__ == '__main__':
    page = Suggestions()
    page()