import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh #auto refresh data for streamlit 
#pip install streamlit-autorefresh

st.set_page_config(page_title = 'Sales dashboard',
                   page_icon = ":bar_chart:",
                   layout = "wide"
)

# update every 30 seconds
st_autorefresh(interval= 0.5 * 60 * 1000, key="dataframerefresh")

def get_data():
    # Perform some request to get a dataframe
    data = pd.read_excel(
                    io= 'supermarkt_sales.xlsx',
                    engine= 'openpyxl',
                    sheet_name= 'Sales',
                    skiprows= 3,
                    usecols= 'B:R',
                    nrows= 1000
    )
    return data

df = get_data()
st.dataframe(df)

