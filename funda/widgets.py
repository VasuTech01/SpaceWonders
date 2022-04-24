from cv2 import CV_16S
import streamlit as st
import cv2 as cv
st.title("WiDgEtS")
if(st.button("Subscribe")):
    st.write("you **liked** this video :thumbsup:")
name=st.text_input("NAME")
st.write("**"+name+"**")

address=st.text_area("Enter your address")
st.write(address)
date=st.date_input("Enter a Date")
time=st.time_input("Enter time")
st.write("{} \n {}".format(date,time))
if(st.checkbox("You Accept the T&C",value=False)):
    st.write(":smile:")
st.radio("Colors",["r",'g',"b"],index=0)
a=st.selectbox("Colours",["vasu","varun","Krishna"],index=0)
st.write(a)
v3=st.multiselect("Colours",["r","g","b"])
st.write(v3)
st.slider("AGE",min_value=18,max_value=35,step=2)
st.number_input("Number",max_value=15.0,step=2.5)
img=st.file_uploader("Upload")
img=cv.GaussianBlur(img)
st.image(img)