# Welcome to CredPred!

<p align="center">
  <img width="460" height="300" src="cred.gif">
</p>
CredPred is an app created to help users on their credit journey. It is a simple light-weight interface to get instant estimates of how likely is you profile to succeed in a credit card application. It also provides you with insights into improving your profile to continue on your credit journey being more informed and confident!


## Requirements

The basic requirements for the app are:
```
autokeras
gradio
loguru
matplotlib
millify
numpy
pandas
scikit-learn==0.23.2
pycaret
streamlit
```

## How to run

After cloning and installing the necessary packages listed above, run the following commands
```
cd app
streamlit run dashboard.py
```
you should be able to see the url generated for the streamlit app launched, clicking on the link would provide you access to play with this app!

## Data

To build the ML models we used two datasets namely:

1. [UCI ML Repository: Credit Approval Data Set](https://archive.ics.uci.edu/ml/datasets/credit+approval)
2. [Kaggle Credit Score Dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

The preprocessing steps used for dataset 2 can be found [here](https://www.kaggle.com/code/clkmuhammed/credit-score-classification-part-1-data-cleaning/notebook) 

## Known issues

Currently the application partially works on MacOS systems. The root of failure is **autokeras** being a tricky tool to use with MacOS, especially M1 chips. We were not able to properly install and run autokeras dependent pages on a Mac system. However the app should work fine on Windows and Linux based systems.

## Credits

This course is completed as a requirement for the course Designing and Deploying AI/ML systems (course info [here](https://www.coursicle.com/cmu/courses/MEG/24679/))

