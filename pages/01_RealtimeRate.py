from ast import FormattedValue
from unittest import result
import streamlit as st
import pandas as pd
import requests, os
from datetime import datetime
from forex_python.converter import CurrencyRates

now = datetime.now()
st.sidebar.title( " 현 시각 달러환율" )
st.sidebar.write( "Date/Time:", now )
CR = CurrencyRates()
result = CR.convert('USD', 'KRW', 1 )
FormattedValue = "{:.5f}".format(result) 
value = float(FormattedValue)
st.sidebar.write( " 1 $ = ", value)

st.header('🍉 Realtime Exchange Rates')
new_sub_1 = '<p style="font-family:sans-serif; color:Green; font-size: 22px;">1) Fixer API 사용</p>'
st.markdown(new_sub_1, unsafe_allow_html=True)

currency_list_1 = ['USD','KRW','AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY',  'ZAR']
currency_list_2 = ['EUR', 'USD','AUD', 'KRW', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'KRW', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR',  'INR', 'ISK', 'JPY', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'TBD', 'TRY',  'ZAR'] #'ILS', 'RUB',

base_cur = st.selectbox('- Select base currency for conversion', currency_list_1)
target_currency = st.multiselect(' - Select target currency to convert ',currency_list_2, default=['JPY','PHP','TBD'])
title = [ 'Base_Currency', 'Target_Currency', 'Price', 'Conversion_Date' ]  # bracket's meaning of importtance ?? 

@st.cache
def load_data():
    df = pd.DataFrame( columns = title )
    print(target_currency)
    for i,name in enumerate(target_currency):
        print("currencies:",name)
        url = ''.join(['https://api.apilayer.com/exchangerates_data/convert?to=',name,'&from=', base_cur,'&amount=','1'])
        payload = {}
        headers= {   "apikey": "kKiUQUbkMLY59Re2a6aaqsX5jASitrdW"  }  # 최신
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.text
        data = response.json()
        cc = [ (  data['query']['from'],  data['query']['to'],  data['info']['rate'] , data['date']    ) ]
        print ( "cc:", cc)   
        dfnew = pd.DataFrame( cc, columns = title ) 
        df = df.append(  pd.DataFrame( dfnew, columns = title)  )
    return df 
qq=load_data()
st.text ('-Completion of Currency conversion like below !!  ')
st.write ( qq )

#======2nd step ====================================

st.markdown("---------------")
st.markdown("")

new_sub_2 = '<p style="font-family:sans-serif; color:Green; font-size: 22px;">2) Python API 사용 </p>'
st.markdown(new_sub_2, unsafe_allow_html=True)

# error in presence of @st.cache 
title_2 = ['Currencies', 'Rates']
dg = pd.DataFrame( columns = title_2 )  # reserve

def currency_all():
    
    col1, col2, col3 = st.columns(3)
    CR = CurrencyRates()
    for i,j in enumerate(currency_list_2):
        Result = CR.convert(base_cur, j, 1)
        colname = str(base_cur + '/' + j)
        FormattedValue = "{:.5f}".format(Result) 
        value = float(FormattedValue)

        if i < 11:       
            with col1:
                st.write(colname, value )

        elif (i > 10) and (i<21) : 
            with col2:
                st.write(colname, value)

        elif(i > 20):
            with col3:
                st.write(colname, value)

        # dgnew = pd.DataFrame(value, columns=title_2, axis=1 )
        # dg = dg.append ( pd.DataFrame(dgnew, columns = colname ) )
        # # dg = pd.DataFrame(dgnew, columns = colname ) 
    # return dg

# rr =currency_all()

# rr.to_excel('Currency_Rate form Forex API')
currency_all()
# st.write ( " ( Caution: 'ILS', 'RUB' currency rate is not available )")
opt = st.radio( label = '- Select option for retriving the data', options = ['Go','Stop(Current Data Save)'] )
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)

