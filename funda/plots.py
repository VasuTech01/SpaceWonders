import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data=pd.DataFrame(np.random.randn(100,3),columns=['a','b','c'])
chart=alt.Chart(data).mark_circle().encode(
    x='a',y='b',tooltip=['a','b']
)
st.altair_chart(chart)
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
plt.scatter(data['a'],data['b'])
st.pyplot()
st.graphviz_chart("""
digraph{
   watch->like
   like->share
   share->watch 
}
""")
st.map()
st.image("vasu.jpg")
st.audio("D:\\visual Java\\Python\\audio3.wav")
st.video("D:\\visual Java\\Python\\vdo1.mp4")
