import streamlit as st
from PIL import Image
from matplotlib import image
import os

#Title of the home page
st.header(":blue[Flipkart Laptop Price Prediction Data App :desktop_computer]")
#Using subheader
st.write('By: :red[Suraj Honkamble]')

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

#Using markdown cell type
st.markdown(":green[Connect with me on,]")

#Creating column layout
col1,col2,col3,col4=st.columns(4, gap='small')
with col1:
    st.write("[LinkedIn](https://www.linkedin.com/in/surajhonkamble/)")
with col2:
    st.write("[GitHub](https://github.com/surajh8596)")
with col3:
    st.write("[Instagram](https://www.instagram.com/surajking6958/)")
with col4:
    st.write("[Tableau](https://public.tableau.com/app/profile/suraj.honkamble)")