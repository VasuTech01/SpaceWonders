import time
import requests
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_pgMN0u.json"
lottie_url_download = "https://assets3.lottiefiles.com/packages/lf20_1bdm0t0m.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)
df=pd.read_csv("funda/omicron.csv")
st.title("WELCOME TO MY RESUME")
st_lottie(lottie_download, key="hello")
if "n" not in st.session_state:

    st.session_state["n"]=3
a=st.button("INCrement",)
if a:
    st.session_state.n+=1

b=st.button("DECrement")
if b:
    st.session_state.n-=1
st.table(df.head(st.session_state.n))
st.write("**"+str(st.session_state.n)+"** :thumbsup:")





if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()