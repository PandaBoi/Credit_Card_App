import streamlit as st 
from utils.page import Page
st.title("Welcome to Credit Card Predictor")

class Input_data(Page):
    def __init__(self, name, data, **kwargs):
        self.name = name
        self.data = data
        self.kwargs = kwargs

    def content(self):
        """Returns the content of the page"""

        st.header("Welcome to CredPred")
        st.subheader("Our product is focused on helping you navigate the credit card score/application journey.")
        st.markdown("Follow the prompts below to input your data which our model will subsequently use.")

        "st.session_state object:", st.session_state

        age = st.number_input("Age", min_value = 0, max_value = 100, step = 1, key = "age")
        annual_income = st.number_input("Annual Income", min_value = 0, max_value = 10000000, step = None, key = 'income')
        bank_accounts = st.number_input("Number of Bank Accounts", min_value = 0, max_value = 100, step = 1, key = 'bank_accounts')
        credit_cards = st.number_input("Number of Credit Cards", min_value = 0, max_value = 100, step = 1, key = 'credit_cards')
        delayed_pay = st.number_input("Number of Delayed Payments", min_value = 0, max_value = 1000, step = 1, key = 'delayed')
        credit_inq = st.number_input("Number of Credit Inquiries", min_value = 0, max_value = 1000, step = 1, key = 'inquiries')
        out_debt = st.number_input("Outstanding Debt", min_value = 0, max_value = 10000000, step = None, key = 'debt')
        credit_history = st.number_input("Length of Credit History (Days)", min_value = 0, max_value = 10000000, step = None, key = 'credit_history')
        
        occupation = st.selectbox("Occupation", ('Student', 'Scientist', 'Accountant','Architect', 'Developer', \
                'Doctor', 'Engineer', 'Entrepreneur', 'Journalist', 'Lawyer','Manager', 'Mechanic','Media_Manager',\
                    'Musician','Teacher','Writer'), key = 'occupation')

        prior_default = st.checkbox("Number of Prior Defaults", key = 'prior_default') 
        employed = st.checkbox("Are you employed ?", key = 'employed')
        credit_score_input = st.number_input("Credit Score", min_value = 0, max_value = 800, step = 1, key = 'credit_score')

        # st.write(st.session_state.age)
        # st.write(st.session_state.income)
        # st.write(st.session_state.bank_accounts)
        # st.write(st.session_state.credit_cards)
        # st.write(st.session_state.delayed)
        # st.write(st.session_state.inquiries)
        # st.write(st.session_state.debt)
        # st.write(st.session_state.credit_history)
        # st.write(st.session_state.occupation)

        # st.write(st.session_state.debt_2)
        # st.write(st.session_state.prior_default)
        # st.write(int(st.session_state.employed))
        # st.write(st.session_state.credit_score)

    def title(self):
        """Returns the title of the page"""
        st.header(f"{self.name}")

    def __call__(self):
        self.title()
        self.content()