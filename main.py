import streamlit as st

# HTML 파일을 읽어서 HTML 컴포넌트로 출력
with open('./ff5c7f90-5134-4e0e-8312-cf625ac8b5db_Export-439b2a57-7b62-4fa7-8691-a5bd63a9a87c/CV - Jinwoo Lee 12269f3b13ea4c489998b5d534218645.html', 'r', encoding='utf-8') as file:
    html_code = file.read()
st.components.v1.html(html_code, height=20000, width=1000)
