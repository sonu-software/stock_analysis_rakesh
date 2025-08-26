import streamlit as st


import nselib
from nselib import capital_market

import pandas as pd

from datetime import datetime

import requests
from bs4 import BeautifulSoup

import feedparser



#stock_data_date=capital_market.bhav_copy_with_delivery(stock_date_query)
#stock_data_period=capital_market.price_volume_data(stock_name.upper(), period=period.upper())



def know_stock_on_date(stock_date_query,stock_name_query):
    try:
        #stock_data_date=capital_market.bhav_copy_with_delivery(stock_date_query)
        new=stock_data_date[["SYMBOL", "SERIES","OPEN_PRICE", "CLOSE_PRICE","HIGH_PRICE", "LOW_PRICE"]]
        new=new[new["SERIES"]=="EQ"]
        if stock_name_query=="nifty50":
            list_nifty50=capital_market.nifty50_equity_list()["Symbol"].tolist()
            final_data_on_date=new[new["SYMBOL"].isin(list_nifty50)]
            
        else:   
            final_data_on_date= new[new["SYMBOL"]==stock_name_query.upper()]

        return final_data_on_date

    except Exception as e:
        return e




def know_stock_on_period(stock_name_query, period):
    try:
        stock_data_period=capital_market.price_volume_data(stock_name_query.upper(), period=period.upper())

        new= stock_data_period[["Symbol","Series","OpenPrice","ClosePrice","HighPrice","LowPrice"]]
        new=new.rename(columns={"Symbol":"SYMBOL" ,"Series":"SERIES","OpenPrice":"OPEN_PRICE","ClosePrice":"CLOSE_PRICE","HighPrice":"HIGH_PRICE","LowPrice":"LOW_PRICE"})
        final_data_on_period=new[new["SERIES"]=="EQ"]
        return final_data_on_period
    
    except Exception as e:
        raise e
    


def know_stock_on_from_to_period(stock_name_query, from_date, to_date):
    try:
        stock_data_period=capital_market.price_volume_data(stock_name_query.upper(),from_date=from_date, to_date=to_date)

        new= stock_data_period[["Symbol","Series","OpenPrice","ClosePrice","HighPrice","LowPrice"]]
        new=new.rename(columns={"Symbol":"SYMBOL" ,"Series":"SERIES","OpenPrice":"OPEN_PRICE","ClosePrice":"CLOSE_PRICE","HighPrice":"HIGH_PRICE","LowPrice":"LOW_PRICE"})
        final_data_on_period=new[new["SERIES"]=="EQ"]
        return final_data_on_period
    
    except Exception as e:
        raise e







def get_real_time_data(query):
    try:
        url1= f"https://www.google.com/finance/quote/{query}:NSE"
        response= requests.get(url1)
        soup= BeautifulSoup(response.text,"html.parser")

        class1= "YMlKec fxKbKc"
        price=float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
        return price
    except Exception as e:
        raise e




    




        
def calculate_cpr(final_data):
    try:
        open_price= final_data["OPEN_PRICE"]
        close_price= final_data["CLOSE_PRICE"]
        high_price= final_data["HIGH_PRICE"]
        low_price= final_data["LOW_PRICE"]
        
        pivot= (high_price+ low_price + close_price)/3
        bc=(high_price+ low_price)/2
        tc=(2*pivot)-bc
        n_cpr = abs(tc-bc) / pivot
        
        return pivot, bc, tc, n_cpr

    except Exception as e:
        raise e
    
@st.cache_data
def knowledge_base(stock_date_query):
    try:
        stock_data_date=capital_market.bhav_copy_with_delivery(stock_date_query)
        return stock_data_date
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
    


def show_dashboard1():
    st.markdown(f"**DATE** {stock_date_query} ")
    pivot, bc, tc, n_cpr =calculate_cpr(data_frame)
    data_frame_calculate={"PIVOT":pivot,"BC":bc,"TC":tc,"NARROW CPR %":n_cpr}
    data_frame_calculate= pd.DataFrame(data_frame_calculate)
    st.dataframe(data_frame)
    st.dataframe(data_frame_calculate)
    price_df = data_frame[["OPEN_PRICE",  "LOW_PRICE","CLOSE_PRICE", "HIGH_PRICE"]]
    price_df_transposed = price_df.T
    price_df_transposed.columns = ['Value']

    # Display the bar chart
    st.bar_chart(price_df_transposed)

    st.subheader(f"CURRENT LIVE STOCK PRICE\n ✅**{stock_name_query}💰₹ {real_time_data}***")
    # Display News Current
    st.subheader(f"📰 Latest news about 📈{stock_name_query}")
    rss_url = f'https://news.google.com/rss/search?q={stock_name_query}&hl=en-US&gl=US&ceid=US:en'

    feed = feedparser.parse(rss_url)
    titles = [entry.title for entry in feed.entries]
    for i, title in enumerate(titles, start=1):
        st.write(f"{i} 🟢 {title}")



def show_dashboard2(data_frame):
    
    for col in ["OPEN_PRICE", "CLOSE_PRICE", "HIGH_PRICE", "LOW_PRICE"]:
        data_frame[col] = data_frame[col].replace({',': ''}, regex=True).astype(float)
    data_frame=pd.DataFrame({"SYMBOL":[data_frame["SYMBOL"].iloc[0]],
                   "SERIES":[data_frame["SERIES"].iloc[0]],
                   "OPEN_PRICE":[data_frame["OPEN_PRICE"].iloc[0]],
                   "CLOSE_PRICE":[data_frame["CLOSE_PRICE"].iloc[-1]],
                   "HIGH_PRICE":[data_frame["LOW_PRICE"].max()],
                   "LOW_PRICE":[data_frame["LOW_PRICE"].min()]
                  })
    st.markdown(f"📈**{stock_name_query}** 📆 {button_name} ")
    pivot,bc,tc, n_cpr=calculate_cpr(data_frame)
    

    data_frame_calculate={"PIVOT":pivot,"BC":bc,"TC":tc,"NARROW CPR %":n_cpr}
    data_frame_calculate= pd.DataFrame(data_frame_calculate)
    st.dataframe(data_frame)
    st.dataframe(data_frame_calculate)
    price_df = data_frame[["OPEN_PRICE",  "LOW_PRICE","CLOSE_PRICE", "HIGH_PRICE"]]
    price_df_transposed = price_df.T
    price_df_transposed.columns = ['Value']

    # Display the bar chart
    st.bar_chart(price_df_transposed)

    st.subheader(f"CURRENT LIVE STOCK PRICE\n ✅**{stock_name_query}💰₹ {real_time_data}***")

    # Display News Current
    st.subheader(f"📰 Latest news about 📈{stock_name_query}")
    rss_url = f'https://news.google.com/rss/search?q={stock_name_query}&hl=en-US&gl=US&ceid=US:en'

    feed = feedparser.parse(rss_url)
    titles = [entry.title for entry in feed.entries]
    for i, title in enumerate(titles, start=1):
        st.write(f"{i} 🟢 {title}")




    









    

st.set_page_config(layout="wide")

st.title(f":material/finance: STOCK ANALYSIS by ₹AKESH📈")
st.subheader(f"🅻🅸🆅🅴")
placeholder=st.empty()


with st.sidebar:

    stock_date_query= st.date_input("Choose stock date", value="today")
    stock_date_query = stock_date_query.strftime("%d-%m-%Y")

    stock_data_date= knowledge_base(stock_date_query)

    if stock_data_date is None:
        st.error("⚠️ No data found for this date. Please choose a working trade day.")
        st.stop()
    
    else:
    
        option= st.selectbox("Select Option", options=["ALL-EQ","NIFTY50","ALL"])
        if option=="ALL-EQ":
            stock_list= stock_data_date[stock_data_date["SERIES"]=="EQ"]["SYMBOL"].tolist()

        elif option=="NIFTY50":
            stock_list=capital_market.nifty50_equity_list()["Symbol"].tolist()
        
        elif option=="ALL":
            stock_list= stock_data_date["SYMBOL"].tolist()

        stock_name_query= st.selectbox("Choose Stock Name",stock_list)
        real_time_data= get_real_time_data(stock_name_query)
        now = datetime.now()
        formatted = now.strftime(f"%d/%b/%Y - %H:%M:%S")
        placeholder.markdown(f"📈{stock_name_query} 🟢{formatted} \n💰₹{real_time_data}")
        
    

if stock_data_date is None:
    st.error("⚠️ No data found for this date. Please choose a working trade day.")
    st.stop()

else:
    st.markdown("_____________________________________________________________________")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        button_1day = st.button("1 Day  ")

    with col2:
        button_1week = st.button("1 Week ")

    with col3:
        button_1month = st.button("1 Month")
    
    with col4:
        button_6month = st.button("6 Month")
    
    with col5:
        button_1year = st.button("1 Year ")

    with col6:
        from_date= st.date_input("FROM Date", value="today")
        from_date_query = from_date.strftime("%d-%m-%Y")
    
    with col7:
        to_date= st.date_input("TO Date", value="today")
        to_date_query = to_date.strftime("%d-%m-%Y")
        button_for_date= st.button(f"Search")

    
    
    
    
    



    data_frame=know_stock_on_date(stock_date_query,stock_name_query)
    if not button_1month and not button_1week and not button_6month and not button_1year and not button_for_date:
        show_dashboard1()


    if button_1day:
        button_name="1 DAY"
        show_dashboard1()
    
    elif button_1week:
        button_name="1 WEEK"
        data_frame1=know_stock_on_period(stock_name_query, "1W")
        show_dashboard2(data_frame1)

    elif button_1month:
        button_name="1 MONTH"
        data_frame1=know_stock_on_period(stock_name_query,"1M")
        show_dashboard2(data_frame1)
    
    elif button_6month:
        button_name="6 MONTH"
        data_frame1=know_stock_on_period(stock_name_query,"6M")
        show_dashboard2(data_frame1)

    elif button_1year:
        button_name="1 YEAR"
        data_frame1=know_stock_on_period(stock_name_query,"1Y")
        show_dashboard2(data_frame1)

    elif button_for_date:
        data_frame1=know_stock_on_from_to_period(stock_name_query, from_date_query, to_date_query)
        button_name=f"{from_date_query} ↔️ {to_date_query}"
        show_dashboard2(data_frame1)



        
        
    
