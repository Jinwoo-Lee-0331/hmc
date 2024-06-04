import streamlit as st

# HTML 파일을 읽어서 HTML 컴포넌트로 출력
with open('CV - Jinwoo Lee.html', 'r', encoding='utf-8') as file:
    html_code = file.read()
st.components.v1.html(html_code, height=8000, width=1000)
