import streamlit as st

st.title('New text app')

txt = st.text_area('Введите текст: ')

st.write('Введенный текст:',txt)