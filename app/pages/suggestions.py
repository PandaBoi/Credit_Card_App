import streamlit as st
import pandas as pd


class Suggestions(Page):
    def __init__(self, name, data, **kwargs):
        self.name = name
        self.data = data
        self.kwargs = kwargs

    def content(self):
        """Returns the content of the page"""

        raise NotImplementedError("Please implement this method.")

    def title(self):
        """Returns the title of the page"""
        st.header(f"{self.name}")
