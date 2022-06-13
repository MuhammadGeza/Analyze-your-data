import streamlit as st
from utils import *
import pandas as pd


def app():
    st.markdown("""
        <h1>
            Analyze your data
        </h1>""", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a file (only supports csv file extension or excel file)")

    try:
        if uploaded_file:
            name = uploaded_file.name
            df = pd.read_csv(uploaded_file) if name.split('.')[-1]=='csv' else pd.read_excel(uploaded_file)

            st.markdown("""<h2 class="text-center">First five data</h2>""", unsafe_allow_html=True)
            st.write(df.head())
        
            options = st.multiselect("Select the column you don't want to analyze (such as name, index number, etc). Skip it if it's not there", df.columns)
            
            categorical = st.multiselect("Select a column that has a categorical data type (column that is not selected will be considered as numeric). Skip it if it's not there", [col for col in df.columns if col not in options][::-1])

            checkbox = st.checkbox('Show analysis results')
            if checkbox:
                df.drop(columns=options, inplace=True)
                df_num = df.select_dtypes(['int', 'float']).dropna()

                st.markdown("""<h2>Dataset Statistics</h2>""", unsafe_allow_html=True)
                dataset_statistics(df)

                st.markdown("""<h2 style="margin-top: 1.5rem;">Variabels overview</h2>""", unsafe_allow_html=True)
                variabels_overview(df, categorical)

                st.markdown("""<h2 style="margin-top: 1.5rem;">Interaction</h2>""", unsafe_allow_html=True)
                interactions(df_num)

                st.markdown("""<h2 style="margin-top: 1.5rem;">Correlations</h2>""", unsafe_allow_html=True)
                correlations(df_num)
    except:
        st.warning('Uploaded file extension must be csv or excel file')