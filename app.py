import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport


st.title("Data Profiling App")
st.subheader("This app will help you to do Data Exploration")

st.sidebar.header('User Input Features')


# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input Excel file", type="xlsx")
if uploaded_file is not None:
    st.markdown('---')
    input_df = pd.read_excel(uploaded_file, engine="openpyxl")

    profile = ProfileReport(input_df, title="New Data for profiling")

    st.subheader("Detailed Report of the Data Used")

    st.write(input_df)

    st.html(profile.html)

else:
    st.write("You did not upload the new file")
