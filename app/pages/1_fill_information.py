import streamlit as st 
from utils.page import Page
st.session_state.update(st.session_state)

class Input_data(Page):
    def __init__(self, **kwargs):

        self.kwargs = kwargs
    
    
    def content(self):
        """Returns the content of the page"""

        
        #Initializes the session state
        "st.session_state object:", st.session_state
        
        #Initializes the user input fields that are subsequently used in the next pages
        
        st.number_input("Age", min_value = 0, max_value = 100, step = 1, key = "Age")
        st.number_input("Annual Income", min_value = 0, max_value = 10000000, step = None, key = 'Annual_Income')
        st.number_input("Number of Bank Accounts", min_value = 0, max_value = 100, step = 1, key = 'Num_Bank_Accounts')
        st.number_input("Number of Credit Cards", min_value = 0, max_value = 100, step = 1, key = 'Num_Credit_Card')
        st.number_input("Number of Delayed Payments", min_value = 0, max_value = 1000, step = 1, key = 'Num_of_Delayed_Payment')
        st.number_input("Number of Credit Inquiries", min_value = 0, max_value = 1000, step = 1, key = 'Num_Credit_Inquiries')
        st.number_input("Outstanding Debt", min_value = 0, max_value = 10000000, step = None, key = 'Outstanding_Debt')
        st.number_input("Length of Credit History (Days)", min_value = 0, max_value = 10000000, step = None, key = 'Credit_History_Age')
        
        st.selectbox("Occupation", ('Student', 'Scientist', 'Accountant','Architect', 'Developer', \
                'Doctor', 'Engineer', 'Entrepreneur', 'Journalist', 'Lawyer','Manager', 'Mechanic','Media_Manager',\
                    'Musician','Teacher','Writer'), key = 'Occupation')

        st.checkbox("Number of Prior Defaults", key = 'prior_default') 
        st.checkbox("Are you employed ?", key = 'employed')
        st.number_input("Credit Score", min_value = 0, max_value = 800, step = 1, key = 'Credit_Score')

        #Once the user has input their data, the session state is automatically updated

    def title(self):
        """Returns the title of the page"""
        st.title("Welcome to CredPred")
        st.subheader("Our product is focused on helping you navigate the credit card score/application journey.")
        st.markdown("Follow the prompts below to input your data which our model will subsequently use.")

    def __call__(self):
        self.title()
        self.content()

if __name__ == "__main__":
    page = Input_data()
    page()
