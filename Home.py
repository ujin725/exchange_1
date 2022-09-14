
from urllib.request import HTTPDefaultErrorHandler
import streamlit as st
import pandas as pd
from PIL import Image
# import matplotlib.pyplot as plt
# import plotly.express as px

st.sidebar.title("Menu")
# st.set_page_config(layout="wide")


st.title(' Exchange Rate Anaysis  ')

st.markdown("""
Topic: 

Past Exchange rates Retrieving Data , Realtime fluctuation, extra : AI/MI ! 
""")

st.markdown("---------------") 

st.markdown("""
Page Composition :
""")

st.markdown("""

* 🐈Exchange : finshot 서비스 국가들의 통화환율 보여주기
* 🦆Data_Retrieve: 현시점, 과거 환율정보 불러와서 비교하기
* 기타 추가 예정 페이지 : 
    1) 환율변동에 따른 spread margin 



""")

st.markdown("---------------") 


st.markdown("""
Package Information :
""")


st.markdown("""
* Installed Packages: Python libraries,  streamlit, pandas, pillow, requests, json, etc.
* Data API source: [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)
  and relating company 
* Credit:  Finshot.com
* Version: Betta 0.9 
""")


st.markdown("---------------") 


st.markdown("""
Credited by Finshot Corp. Sep. '2022  
""")                             




