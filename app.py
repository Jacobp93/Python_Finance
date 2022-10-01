import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time
import pandas as pd
import plotly_express as px 
import datetime
import yfinance as yf



#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(layout="wide")
#---------------------------------#
# Title


st.title('JP_App')
st.markdown("""
This app compares cumulitive returns from a choosen start date against the selected financial assets, along with other analysis 
""")



#---------------------------------#
# About
expander_bar =  st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time , datetime
* **Data source:**  Csv file upload   
""")


st.write("please upload file to the application")

tickers = ('^FTSE', '^FTMC', '^GSPC', '^DJI', 'GC=F', 'CL=F', 'SI=F', 'GBPUSD=X', 'GBPEUR=X', 'TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD',
           'XDC-USD', 'CUDOS-USD', 'OMI-USD', 'LINK-USD', 'QNT-USD')

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value=pd.to_datetime(
    '2021-01-01'))
end = st.date_input('End', value=pd.to_datetime('today'))



# Machine learning data 


#pd.read_csv('Score_Project.csv')


#---------------------------------#
# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3 = st.columns((2,1))


#---------------------------------#
# Sidebar + Main panel
col1.header('Input Options')


## Sidebar - Setup 
Select_Industry = col1.selectbox('Select Industry', ('Show all' , 'Fire', 'Security', 'Electrical'))
#st.sidebar.date_input(label = "input date")



#upload tool
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file", type=['csv' , 'xlsx'])


global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len(dropdown) > 0:
    # df = yf.download(dropdown, start, end)['Adj Close']
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.line_chart(df)


# add a select widget to the side bar 
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots' , 'Lineplots' , 'Histogram' , 'Boxplot' , 'Funnel']
)


global numeric_columns
try:
    st.write(df)       
    numeric_columns = (df.select_dtypes(['float' , 'int' , 'object' ]).columns)  
except Exception as e:
    print(e)
    



if chart_select == 'Scatterplots' :
    st.sidebar.subheader("Scatterplot settings")
    try: 
        x_values = st.sidebar.selectbox('X axis' , options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis' , options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'Lineplots' :
    st.sidebar.subheader("Lineplots settings")
    try: 
        x_values = st.sidebar.selectbox('X axis' , options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis' , options=numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values)
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


        
        
if chart_select == 'Histogram' :
    st.sidebar.subheader("Histogram settings")
    try: 
        x_values = st.sidebar.selectbox('X axis' , options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis' , options=numeric_columns)
        plot = px.histogram(data_frame=df, x=x_values, y=y_values)
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)



if chart_select == 'Boxplot' :
    st.sidebar.subheader("Boxplot settings")
    try: 
        x_values = st.sidebar.selectbox('X axis' , options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis' , options=numeric_columns)
        plot = px.box(data_frame=df, x=x_values, y=y_values)
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)



if chart_select == 'Funnel' :
    st.sidebar.subheader("Funnel settings")
    try: 
        x_values = st.sidebar.selectbox('X axis' , options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis' , options=numeric_columns)
        plot = px.funnel(data_frame=df, x=x_values, y=y_values)
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'Averages' :
    st.sidebar.subheader("Average settings")
    try: 
        df.mean()
        #display chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
#Upload tool configuration 
st.set_option('deprecation.showfileUploaderEncoding' , False)



#t.sidebar.subheader("Visualization App")


err = print("Settings need revising")



class _Fire_:


    if Select_Industry == "Fire" :
        try: st.metric(label="Fire", value="23 - 40" , delta_color="off") and st.metric(label=" Model Data - Fire ", value=20, delta=-3) and st.metric(label="Active Diamond Companies within vertical", value=123, delta_color="off")
        except exception as err:
            print(err)



class _Security_:


    if Select_Industry == "Security" :
        try: st.metric(label="Security", value="40 - 60", delta_color="off") and st.metric(label=" Model Data - Security ", value=43, delta=3) and st.metric(label="Active Diamond Companies within vertical", value=123, delta_color="off")
        except exception as err:
            print(err)



#test_data = 80


class _Electrical_:


    if Select_Industry == "Electrical" :
        try: st.metric(label="Electrical", value="30 - 40" , delta_color="off") and st.metric(label=" Model Data - Electrical ", value=40, delta=-0 , delta_color='off') and st.metric(label="Active Diamond Companies within vertical", value=123, delta_color="off")
        except exception as err:
            print(err)



#test = st.sidebar.write("test")



#if Select_Industry == "Show all" :
