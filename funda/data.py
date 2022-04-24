import streamlit as st
import pandas as pd
import numpy as np
import time
a=np.array([1,2,3,4,5,6,7,8])
nd=a.reshape((2,4))
dic={
    "name":["vasu"],
"age":[21],
"city":["noida"]
}
data=pd.read_csv("D:\\visual Java\\Python\\omicron.csv")
st.dataframe(data,width=800,height=500)
st.table(a)
st.json(dic)
st.write(dic)
@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()
if st.checkbox("1"):
    st.write(ret_time(1))
if st.checkbox("2"):
    st.write(ret_time(2))