import streamlit as st
import pandas as pd

st.title("Registration Form")
st.balloons()
first,last=st.columns(2)
first.text_input("First Name")
last.text_input("last Name")
email,mob=st.columns([3,1])
email.text_input("EMAIL")
mob.text_input("Mob No")
user,pw,pw2=st.columns(3)
user.text_input("User")
pw.text_input("Password",type="password")
pw2.text_input("Confirm",type="password")
ch,sub=st.columns([1,3])
ch.checkbox("I Agree")
sub.button("Submit")
