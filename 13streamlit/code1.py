import streamlit as st
import pandas as pd

st.title("I am Tafheem Ahemad")

name=st.text_input("Enter your name")

st.write(f"Your name is {name}")

# Slider
age=st.slider("Enter your age",0,100,25)
st.write(f"Your age is {age}")

# Drop down
options=["English","Bengali","Odia","Hindi"]
language_choose=st.selectbox("Enter your language",options=options)
st.write(f"your language is {language_choose}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
st.write(df)
df.to_csv('sales.csv')

file=st.file_uploader("Select the file","csv")

if file is not None:
	df=pd.read_csv("sales.csv")
	st.write(df)