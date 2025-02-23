import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import requests

#Establish a connection and cursor
connection = sqlite3.connect("exercises/exercise_data.db")


# Queries to read all data
cursor = connection.cursor()
cursor.execute("SELECT * FROM events")
rows= cursor.fetchall()

dates = [row[0] for row in rows]
temperature = [row[1] for row in rows]
print(temperature)

# df = pd.read_csv("exercises/exer_data.txt")[1:]
# print(df)
# dates = df["date/time"]
# temperature = df[' temperature']
#
figure = px.line(x=dates, y=temperature)

st.header("temperature graph")
#st.line_chart(df,x= "date/time",y=' temperature')
st.plotly_chart(figure)
