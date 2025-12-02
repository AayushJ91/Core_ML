import streamlit as st

st.title("Hello")
st.subheader("doing Streamlit tutorial")
st.text("Welcome to the tutorial")
st.write("This is 'write' function")

selected=st.selectbox("This is a dropdown box to select the opitons: ", ["Opt1","Opt2","Opt3"]) # a dropdown list
st.write(f"Selected Option : {selected}")
st.success(f"this is st.success {selected}") #gives a green box

if st.button("learning 'button' and 'if'"):
    st.write("Kucch Hua")

check = st.checkbox("checkbox")
if check:
    st.write("inside 'if' : checked")

radio = st.radio("Pick your option: ", ['opt1','opt2'])
slider = st.slider("choose a number",0,5,2)
num_inp=st.number_input("number_input", min_value=1, max_value=100)
st.write(num_inp)
text_inp = st.text_input("text inp")
if text_inp:
    st.write(f"printing {text_inp}")

st.subheader("Columns")
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    vote1 = st.button("vote1")
    st.success("col1")
with col2:
    st.header("Column 2")
    vote2 = st.button("vote2")
    st.success("col2")


file = st.file_uploader("Enter the file", type=["csv","xlsx","pdf"])