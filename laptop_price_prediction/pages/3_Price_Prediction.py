import streamlit as st
import pandas as pd
import pickle
import os
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#Page Heading
st.header(":blue[Laptop Price Prediction]:desktop_computer:")

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
data.drop('Processor Type', axis=1, inplace=True)

#Accepting the required features from user
col1, col2= st.columns(2)
with col1:
    brand = st.selectbox(
        ':green[Select Laptop Brand]',
        (df.Brand.unique()))
    st.write('Your Selected Brand:', brand)

with col2:
    operating_system=st.selectbox(
        ':green[Select Operating System]',
        (df['Operating System'].unique()))
    st.write('Your Selected Operating System:', operating_system)

col1, col2= st.columns(2)
with col1:
    ram_type=st.selectbox(
        ':green[Select RAM Type]',
        (df['RAM Type'].unique()))
    st.write('Your Selected RAM Type:', ram_type)

with col2:
    ram_size=st.selectbox(
        ':green[Select RAM Size]',
        (df['RAM Size'].unique()))
    st.write('Your Selected RAM Size:', ram_size)

col1, col2= st.columns(2)
with col1:
    disc_type=st.selectbox(
        ':green[Select DISC Type]',
        (df['Disc Type'].unique()))
    st.write('Your Selected DISC Type:', disc_type)

with col2:
    disc_size=st.selectbox(
        ':green[Select DISC Size]',
        (df['Disc Size'].unique()))
    st.write('Your Selected DISC Size:', disc_size)  

#Create dataframe using all these values
sample=pd.DataFrame({"Brand":[brand],"Operating System":[operating_system],
                   "RAM Type":[ram_type], "RAM Size":[ram_size],
                   "Disc Type":[disc_type], "Disc Size":[disc_size]})

#Convert these values to suitable integer form
#Function to change brand to number
def replace_brand(brand):
    if brand=='Lenovo':
        return 1
    elif brand=='ASUS':
        return 2
    elif brand=='HP':
        return 3
    elif brand=='DELL':
        return 4
    elif brand=='RedmiBook':
        return 5
    elif brand=='realme':
        return 6
    elif brand=='acer':
        return 7
    elif brand=='MSI':
        return 8
    elif brand=='APPLE':
        return 9
    elif brand=='Infinix':
        return 10
    elif brand=='SAMSUNG':
        return 11
    elif brand=='Ultimus':
        return 12
    elif brand=='Vaio':
        return 13
    elif brand=='GIGABYTE':
        return 14
    elif brand=='Nokia':
        return 15
    elif brand=='ALIENWARE':
        return 16  
data['Brand']=data['Brand'].apply(replace_brand)

#Function to change os to number
def replace_os(os):
    if os=='Windows 11':
        return 1
    elif os=='Windows 10':
        return 2
    elif os=='Mac':
        return 3
    elif os=='Chrome':
        return 4
    elif os=='DOS':
        return 5
data['Operating System']=data['Operating System'].apply(replace_os)

#Function to change ram type to number
def replace_ram_type(ram_type):
    if ram_type=='DDR4':
        return 1
    elif ram_type=='DDR5':
        return 2
    elif ram_type=='LPDDR4':
        return 3
    elif ram_type=='Unified':
        return 4
    elif ram_type=='LPDDR4X':
        return 5
    elif ram_type=='LPDDR5':
        return 6
    elif ram_type=='LPDDR3':
        return 7   
data['RAM Type']=data['RAM Type'].apply(replace_ram_type)

#Function to change ram size to number
def replace_ram_size(ram_size):
    if ram_size=='8GB':
        return 1
    elif ram_size=='16GB':
        return 2
    elif ram_size=='4GB':
        return 3
    elif ram_size=='32GB':
        return 4
data['RAM Size']=data['RAM Size'].apply(replace_ram_size)

#Function to disc type to number
def replace_disc_type(disc_type):
    if disc_type=='SSD':
        return 1
    elif disc_type=='HDD':
        return 2
    elif disc_type=='EMMC':
        return 3
data['Disc Type']=data['Disc Type'].apply(replace_disc_type)

#Function to change disc size to number
def replace_disc_size(disc_size):
    if disc_size=='256GB':
        return 1
    elif disc_size=='512GB':
        return 2
    elif disc_size=='1TB':
        return 3
    elif disc_size=='128GB':
        return 4
    elif disc_size=='64GB':
        return 5
    elif disc_size=='32GB':
        return 6
    elif disc_size=='2TB':
        return 7
data['Disc Size']=data['Disc Size'].apply(replace_disc_size)

#Split data into X and y
X=data.drop('MRP', axis=1).values
y=data['MRP'].values

#Standarizing the features
std=StandardScaler()
std_fit=std.fit(X)
X=std_fit.transform(X)

#Train the model
xgb=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=42)
xgb.fit(X,y)

#Convert User input to suitable integer form
sample['Brand']=sample['Brand'].apply(replace_brand)
sample['Operating System']=sample['Operating System'].apply(replace_os)   
sample['RAM Type']=sample['RAM Type'].apply(replace_ram_type)
sample['RAM Size']=sample['RAM Size'].apply(replace_ram_size)
sample['Disc Type']=sample['Disc Type'].apply(replace_disc_type)
sample['Disc Size']=sample['Disc Size'].apply(replace_disc_size)

#Standardize the features
sample=sample.values
sample=std_fit.transform(sample)

#Prediction
if st.button('Predict'):
    price=xgb.predict(sample)
    price=price[0].round(2)    
    st.subheader(":blue[Laptop Price For Your Selected Feature :] :green[{}]".format("₹"+str(price)))
else:
    pass
