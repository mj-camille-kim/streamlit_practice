import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

st.write("Good morning World !!!")

df = pd.read_csv("./data/my_data.csv", parse_dates=["date"])
df = df.set_index("date")
st.line_chart(df)