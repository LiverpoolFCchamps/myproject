import streamlit as st
st.titlie("Моето първо приложение")
name = st.text_input("Как се казваш?")
if name:
  st.write(f"Здравей,{name}!")
