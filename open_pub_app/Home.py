import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("🍻Pubs In United Kingdom To Have Some Drink And Chillout🍻")
st.write('By: :red[Suraj Honkamble]')


st.subheader(":green[Connect with me on,]")

col1,col2,col3,col4=st.columns(4, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/surajhonkamble/)")
with col2:
    st.subheader("[GitHub](https://github.com/surajh8596)")
with col3:
    st.subheader("[Instagram](https://www.instagram.com/surajking6958/)")
with col4:
    st.subheader("[Tableau](https://public.tableau.com/app/profile/suraj.honkamble)")


#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://cascadecollision.com/wp-content/uploads/safe-and-fun-new-years.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)