import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from bokeh.plotting import figure
import time
plt.style.use("ggplot")
data = {
    "num": [x for x in range(1, 11)],
    "square": [x**2 for x in range(1, 11)],
    "twice": [x*2 for x in range(1, 11)],
    "thrice": [x*3 for x in range(1, 11)]
}
# rd = st.sidebar.radio("Navigation", ["Home", "About Us"])
# if(rd == "Home"):
#     df = pd.DataFrame(data=data)
#     col = st.sidebar.multiselect("Select a column", df.columns, "num")
#     plt.plot(df['num'], df[col])
#     st.pyplot()
# if(rd == "About Us"):
#     progress = st.progress(0)
#     for i in range(100):
#         time.sleep(0.1)
#         progress.progress(i+1)

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal")

if selected=="Home":
    st.title(f"you are at {selected}")
    a,b,c=st.columns([1,1,1]);
    a.metric(label="PYTHON",value=50,delta=3.5)
    b.metric(label="JavaScript",value=50,delta=1.5)
    c.metric(label="C++",value=50,delta=2.5)
if selected=="Projects":
    st.title(f"you are at {selected}")
if selected=="Contact":
    st.title(f"you are at {selected}")
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)


# st.write("Hi :thumbsup: i'm **Vasu**")
# st.error("Error")
# st.success("Show Success")
# st.info("information")
# st.exception(RuntimeError("this is an error"))
# st.warning("this is a warning")
