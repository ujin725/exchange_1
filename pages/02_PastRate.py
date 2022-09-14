
from operator import index
from sqlite3 import Date
import webbrowser
import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import requests
import json
from datetime import datetime, timedelta
from plotly import graph_objs as gom
from forex_python.converter import CurrencyRates


currency_list_1 = ['USD', 'KRW','EUR','AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY',  'ZAR']
purchase_day_list = ['2022-03-01','2022-05-01', '2022-07-01','2022-09-01']
# st.header(" :sunglasses: 송금액 계산기 ")
# st.text ('1) to be defined ')

now = datetime.now()
st.sidebar.title( " 현 시각 달러환율" )
st.sidebar.write( "Date/Time:", now )
CR = CurrencyRates()
result = CR.convert('USD', 'KRW', 1 )
FormattedValue = "{:.5f}".format(result) 
value = float(FormattedValue)
st.sidebar.write( " 1 $ = ", value)

# CR = st.session_state['CR']
st.sidebar.markdown("---------------") 
st.sidebar.title( "달러구매시점" )

purchase_day =st.sidebar.selectbox( " slect the one ", purchase_day_list )

st.header(':sunglasses: 일정기간 환율변동 추이 ')
new_sub_4 = '<p style="font-family:sans-serif; color:Green; font-size: 22px;"> 1)조건입력하기 </p>'
st.markdown(new_sub_4, unsafe_allow_html=True)
those_day = datetime.now() - timedelta(days=365)
start_day = st.date_input( "1. 시작일자 입력하기 ( or 달러 구매시점 )", those_day  )
start_day =str(start_day)

end_day = st.date_input( "2. 종료일자 입력하기"  )
end_day = str(end_day)

base_cur = st.selectbox(' 3. Select Base currency ',currency_list_1 )
target_currency = st.multiselect(' 4. Select Target currency to compare ',currency_list_1, ['PHP','JPY','USD','CNY'] )


@st.cache
def load_data():
  url = ''.join( [ 'https://api.apilayer.com/exchangerates_data/timeseries?start_date=',start_day,'&end_date=',end_day ])  #final 
  payload = {}
  headers= {
  "apikey": "kKiUQUbkMLY59Re2a6aaqsX5jASitrdW"
  }
  response = requests.request("GET", url, headers=headers, data = payload)
  status_code = response.status_code
  result = response.text
  print("result: ",result) #prw
  data = response.json()
  return data

qq = load_data()
df_1 = pd.DataFrame(qq)


df_1.to_excel('df_1_excel.xlsx')
df_2 = df_1[['base']]
index_list=df_2.index ###
df_2 = pd.DataFrame(index_list, columns=['Date'])
index_list=df_2.index   

df_3 = pd.json_normalize(df_1['rates'])
df_4 = df_3[target_currency]
df_10 = df_2.join(df_4)

new_sub_5 = '<p style="font-family:sans-serif; color:Green; font-size: 22px;">2) 통계데이터 결과조회 </p>'
st.markdown(new_sub_5, unsafe_allow_html=True)

st.write("**1) Exchange rate fluctuation** ",df_10)

##############################################################

st.write("**2) 달러(or EUR)기준 각국 통화환율 변동 그래프** ")

des_0= df_4[target_currency]
st.line_chart(des_0)
st.write("**3) 평균/표준편차/분산** ")
st.write(des_0.describe())

def plot_raw_data():
  fig = gom.Figure()
  fig.add_trace(gom.Scatter( x=df_10['Date'] ,y=df_10[target_currency[0]], name = 'rate change'  ))
  st.plotly_chart(fig)

st.write("**4) Detail Graph, PHP currency** ")
plot_raw_data()

