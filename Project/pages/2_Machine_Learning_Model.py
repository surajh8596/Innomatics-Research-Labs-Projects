import streamlit as st
import pandas as pd
import os

#Adding Title to page
st.title("What is your Car :car: Price?")

#Loading the dataset
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH = os.path.join(dir_of_interest, "Data")
DATA_PATH1 = os.path.join(DATA_PATH, "CarPricesData.pkl")
df = pd.read_pickle(DATA_PATH1)

#Preproccing the data
X=df.drop('Price', axis=1).values
y=df['Price'].values

#Standardizing the features
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler_x=MinMaxScaler()
scaler_x_fit=scaler_x.fit(X)
X=scaler_x_fit.transform(X)

#Train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#I chose Gradient boosting model, because it is giving me low RMSE
from sklearn.ensemble import GradientBoostingRegressor
grb= GradientBoostingRegressor(n_estimators =100,random_state =0)
grb=grb.fit(x_train, y_train)

#Accepting the user input for features and storing it into dataframe
st.subheader("Enter the required values to check your Car Price")
age=st.number_input("Enter Age of your car:")
km=st.number_input("Enter the Kilometers Run:")
wt=st.number_input("Enter Weight of your car:")
hp=st.number_input("Enter Horse Power(HP) of your car:")
mc=st.number_input("Whether car has Metalic color? Enter 1 for Yes or 0 for No:")
cc=st.number_input("Enter CC of your car:")
d=st.number_input("Enter the number of doors of your car:")
dd=pd.DataFrame({'Age':[age], 'KM':[km], 'Weight':[wt], 'HP':[hp], 'MetColor':[mc], 'CC':[cc], 'Doors':[d]})

#Your Entered Values
st.subheader("Below are the Values that You have Entered,")
st.dataframe(data=dd)

#Scaling the values and Displying the Car Price
X=dd.values
X=scaler_x_fit.transform(X)
car_price=grb.predict(X)
car_price=car_price.round(2)

#Display car price
st.subheader("Price of your Car is,")
st.write(pd.DataFrame({
    'Car Price in $ ': [car_price]
}))
