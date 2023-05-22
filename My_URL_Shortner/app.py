import streamlit as st
import pyshorteners

url=st.text_input("Enter URL to Short.")
button=st.button("SHort URL")
if button:
    s=pyshorteners.Shortener()
    short_url=s.tinyurl.short(url)
    st.success(short_url)