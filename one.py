import streamlit as st
import pandas as pd
import numpy as np

st.title("hello GPT")
name = st.text_input("ask your questions")
st.write("This is your first streamlit app")
st.text("let's get started")
name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"hello, {name}")
    #how to upload any file
    upload_file = st.file_uploader("upload a csv", type='csv')
    if upload_file:
         df = pd.read_csv(upload_file)
         st.dataframe(df)



st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("[link](https://streamlit.io/)")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=10)
st.slider("choose a range", 0, 100)
st.selectbox("select a fruit", ["apple", "banana", "mango"])
st.multiselect("select language", ["java", "python", "c", "c++"])
st.radio("pick one", ["Option A", "Option A"])
st.checkbox("I agree terms & condition")


with st.form("login form"):
  username = st.text_input("Enter username")
  password = st.text_input("Enter password", type="password")
  submitted = st.form_submit_button("Login")

  if( submitted):
    st.success(f"Welcome, {username}")

df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")
st.image("image.jpg", caption="This is a sample image", use_container_width=True)