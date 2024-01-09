import streamlit as st

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

st.write("호스트 이름:", hostname)
st.write("IP 주소:", ip_address)
