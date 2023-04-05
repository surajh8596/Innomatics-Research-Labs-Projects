import streamlit as st

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

st.header(":blue[Summay of Relationship Between Laptop Features And Laptop Price And How The Laptop Pricing Works In The Market]")

st.write("1. Price for laptop brand `ALIENWARE` is ranges approximetely from 2 Lakh to 3.5 Lakh, these are costiest laptops.\n",
         "2. Average price for `ALIENWARE, APPLE, ASUS`,`MSI` laptops brand is high.\n",
         "3. Average price is high for `Mac Operating System` laptops.\n",
         "4. `Apple M1 Max`processor laptops has high average laptop price as compared to any other processor.\n",
         "5. `LPDDR3` RAM type laptops has highest average price.\n",
         "6. `SSD` Disc type laptops has highest aaverage price.\n",
         "7. Higher the RAM size higher the Price of laptop.\n",
         "8. Higher the Disc size highrt the Price of laptop.\n",
         "9. `64GB` RAM size laptops have high average price.\n",
         "10. `2TB` Disc size laptops have high average price.\n")