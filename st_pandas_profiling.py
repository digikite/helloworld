import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()

st_profile_report(pr)



st.write(df)

link = "https://wikidocs.net/231592"

st.write(" wikidoc = " + link)

link = "https://wikidocs.net/231606"

st.write(" streamlit cache = " + link)


