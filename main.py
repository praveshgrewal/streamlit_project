import streamlit as st
import pandas as pd
import numpy as np
# from nbformat import write
import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#title
st.title("Upload Your File")

st.sidebar.header("File")
#csv file
uplod_file=st.sidebar.file_uploader("Upload your file(only in csv)",type="csv")
if uplod_file is not None:
    st.markdown('---')
    df=pd.read_csv(uplod_file,engine="c")

    profile=ProfileReport(df,title="summary of the data")

    st.title("Detailed Report ")
    st.write(df)
    st_profile_report(profile)

else:
    st.markdown('---')
    st.write("You Have no any CSV File")
    #excel
uplod_file_excel=st.sidebar.file_uploader("Upload your file(only in Excel)",type="xlsx")
if uplod_file_excel is not None:
    st.markdown('---')
    df1=pd.read_excel(uplod_file_excel,engine="openpyxl")

    profile_excel=ProfileReport(df1,title="summary of the data")

    st.title("Detailed Report ")
    st.write(df1)
    st_profile_report(profile_excel)

else:
    st.markdown('---')
    st.write("You Have no any  EXCEL File")
