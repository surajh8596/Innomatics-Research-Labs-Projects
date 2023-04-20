import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Header
st.header("🍺🍸Search Nearest Pubs🍺🍸")

#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://theoxfordmagazine.com/wp-content/uploads/angels-cocktail-bar-oxford-02.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
background-blur;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_clean.csv")
df = pd.read_csv(DATA_PATH1)

#Take input -latitude and longitude
col1,col2=st.columns(2)
with col1:
    lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)
with col2:
    lon=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)

#Entered location
search_location=np.array((lat,lon))
#Original/available Location
original_location=np.array([df['latitude'],df['longitude']]).T
#Finding Euclidean distance
dist=np.sum((original_location-search_location)**2, axis=1)
#Adding Distance column to dataframe
df['Distance']=dist

#Asking user that how many nearest Pub they want to see
nearest=st.slider(label="How Many Nearest Pub You Want to See",
                   min_value=1, max_value=50, value=5)
data=df.sort_values(by='Distance', ascending=True)[:nearest]

#List of Bar Names
st.subheader(f"{nearest} Nearest Pubs:")

#Show Nearest Pubs on Map
st.map(data=data, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(data[['name','address','local_authority']])