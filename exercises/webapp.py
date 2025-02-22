import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("exercises/exer_data.txt")[1:]
print(df)
dates = df["date/time"]
temperature = df[' temperature']

figure = px.line(x=dates, y=temperature)

st.header("temperature graph")
# st.line_chart(df,x= "date/time",y=' temperature')
st.plotly_chart(figure)
