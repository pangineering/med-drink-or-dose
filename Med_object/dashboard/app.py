import streamlit as st
from streamlit_webrtc import webrtc_streamer


st.title('My title')


webrtc_streamer(key="sample")