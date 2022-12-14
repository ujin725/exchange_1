
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

* ๐Exchange : finshot ์๋น์ค ๊ตญ๊ฐ๋ค์ ํตํํ์จ ๋ณด์ฌ์ฃผ๊ธฐ
* ๐ฆData_Retrieve: ํ์์ , ๊ณผ๊ฑฐ ํ์จ์ ๋ณด ๋ถ๋ฌ์์ ๋น๊ตํ๊ธฐ
* ๊ธฐํ ์ถ๊ฐ ์์  ํ์ด์ง : 
    1) ํ์จ๋ณ๋์ ๋ฐ๋ฅธ spread margin 



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




