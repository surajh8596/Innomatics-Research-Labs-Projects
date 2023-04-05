import streamlit as st
import pandas as pd
import pickle
import os
import plotly.express as px
import plotly.graph_objects as go

st.header(":blue[Relation Between Laptop Price and Features]")

#Adding backgroung image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i2mag.com/wp-content/uploads/2016/01/Marketing-1-1.jpg");
background-size: 100%;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

#resourses path
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)
data=df.copy()
data.drop("MRP", axis=1, inplace=True)


feature=st.selectbox(
    "Select Feature to See the Relation",
    (data.columns))

fig = px.box(df, x=feature, y='MRP', color=feature)
st.plotly_chart(fig, use_container_width=True)
