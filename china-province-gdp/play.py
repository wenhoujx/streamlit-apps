import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


def load_data():
    df = pd.read_csv("./china-province-gdp/data/Chinas-GDP-in-Province-En.csv")
    return df


source = load_data()

source = source.set_index("year")
source.index = source.index.astype(str)

provinces = st.multiselect(
    "select provinces or special economic zones", source.columns.tolist(), 
    ['Beijing', 'Shanghai', 'Jiangsu']

)
st.subheader("GDP of provinces in billions")
st.line_chart(source[provinces])
