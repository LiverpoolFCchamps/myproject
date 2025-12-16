import streamlit as st
st.titlie("My first app")
name = st.text_input("What is your name?")
if name:
  st.write(f"Hello,{name}!")
