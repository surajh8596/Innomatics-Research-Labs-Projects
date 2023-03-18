import streamlit as st
import plotly.express as px
import pandas as pd
import os

#Adding Title to page
st.title("Exploratory Data Analysis :bar_chart:")

#Loading the dataset
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH = os.path.join(dir_of_interest, "Data")
DATA_PATH1 = os.path.join(DATA_PATH, "CarPricesData.pkl")
df = pd.read_pickle(DATA_PATH1)

#Showing dataset on page
st.header("Cars Dataset:")
st.dataframe(data=df, use_container_width=True)

#Plotting Categorical columns
st.header("Categorical Plots")
col1,col2,col3,col4=st.columns(4, gap='small')
with col1:
    fig = px.histogram(df, x='HP')
    st.plotly_chart(fig, use_container_width=True)
with col2:
    fig = px.histogram(df, x='MetColor')
    st.plotly_chart(fig, use_container_width=True)
with col3:
    fig = px.histogram(df, x='CC')
    st.plotly_chart(fig, use_container_width=True)
with col4:
    fig = px.histogram(df, x='Doors')
    st.plotly_chart(fig, use_container_width=True)


#Ploting Numerical Columns
st.header("Numerical Plots")
col1,col2,col3=st.columns(3, gap='small')
with col1:
    fig = px.histogram(df, x='Age',)
    st.plotly_chart(fig, use_container_width=True)
with col2:
    fig = px.histogram(df, x='KM')
    st.plotly_chart(fig, use_container_width=True)
with col3:
    fig = px.histogram(df, x='Weight')
    st.plotly_chart(fig, use_container_width=True)

#Plot the Target Variable
st.header("Target Variable")
fig = px.histogram(df, x='Price',)
st.plotly_chart(fig, use_container_width=True)

st.markdown("Most of the Cars Price is between 7k  and 12k")
