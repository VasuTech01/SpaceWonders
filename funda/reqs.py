import requests as rs
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date as dt
# print(dt.date(2012,3,2))
st.set_page_config("SPX",":punch:")
url="https://api.nasa.gov/planetary/apod?api_key=kqLb0gOxi41stQHepqLUhUZ4FTT8SVh4J8zhp69Y"
marsUrl="https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=1000&api_key=kqLb0gOxi41stQHepqLUhUZ4FTT8SVh4J8zhp69Y"
api_key="kqLb0gOxi41stQHepqLUhUZ4FTT8SVh4J8zhp69Y"
emj_dct={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
today=dt.today()
today_date=today.strftime("%Y-%m-%d")
if "apod" not in st.session_state:
    st.session_state["apod"]=1
if "picd" not in st.session_state:
    st.session_state["picd"]=1
@st.cache(suppress_st_warning=True)
def getData(url:str,date):
    r=rs.get(url+f"&date={date}")
    res=r.json()
    return res
def getApodData(url:str,st_date,ed_date):
    r=rs.get(url+f"&start_date={st_date}&end_date={ed_date}")
    res=r.json()
    return res
@st.cache(suppress_st_warning=True)
def getMarsImage(sol,rover:str):
    r=rs.get("https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol=1000&api_key="+api_key+"&sol="+str(sol))
    res=r.json()
    return res



def BuildGrid(g):
    print(g)
    st.image(g["hdurl"])
    st.header("**"+g["title"]+"** :bulb:")
    st.text(g["date"])
    st.write(" :green_book: "+g["explanation"])
    st.write(" :punch: ")

def sec_space(url:str):
    st.subheader("""WeLcOmE :pray: Here You Can Explaore The huge Database of Images Of Space Taken EveryDay By NASA :rocket:""")
    it=st.date_input("Enter Date")
    bt=st.button("Lets Go")
    if(bt):
        res=getData(url,it)
        st.session_state["apod"]=res

        BuildGrid(res)
        #st.write(":green_book:\n "+res["explanation"])
##Apod Section fro app
def sec_apod(url:str):
    st.subheader("""Get The Images of Space In Range Of Dates""")
    st.write(":calendar: Dates Must lie be Between Current Year and 2000")
    st.markdown(":white_check_mark: Maximun Day Limit is :one::five: days")
    a,b=st.columns([1,1])
    bg=a.date_input("Start Date")
    ed=b.date_input("End Date")
    bt=st.button("Lets Fetch")
    if(bt):
        res=getApodData(url,bg,ed)
        print(res)
        j=0
        p=0
        prog=st.progress(0)
        for g in res:
            j+=1
            st.image(g["hdurl"])
            st.header("**"+g["title"]+"** :bulb:")
            st.text(g["date"])
            st.write(" :green_book: "+g["explanation"])
            st.write(":flashlight: :moon: \n")
            p=int((j/len(res))*100)
            prog.progress(p)
def getImgNo(n):
    s=""
    for i in str(n):
        s+=":"+emj_dct[int(i)]+":"
    print(s)
    return s

def spec_mars():

    st.subheader("**Get Images Sent by Mars rover According to SOL** :satellite_antenna:")

    sol=st.number_input("Enter SOL",min_value=110,max_value=3000)
    rover=st.multiselect("Select Rover",options=["Spirit",'Opportunity',"Curiosity"])
    bt=st.button("Get Images")
    if bt:
        print(rover)
        res=getMarsImage(sol,rover[0].lower())
        print(res)
        imgs=res["photos"]
        for i in range(len(imgs)):
            s=getImgNo(i+1)
           
            st.write(s+" :pushpin:    :calendar: **"+imgs[i]["earth_date"]+"**")
            st.image(imgs[i]["img_src"],width=720)
            





    




    

        

    


    
 
st.title("SpAcE  :milky_way:  WoNdErS")
st.info("**_Get AmaZing ImaGes Of oUr Solar System_** ")
    

selected=option_menu(
    menu_title=None,
    options=["Home","Space","Mars"],
    icons=["brightness-high",'calendar-x',"radioactive"],
    menu_icon='cast',
    orientation="horizontal"
)

if selected=="Home":
    sec_space(url)
   
if selected=="Space":
    sec_apod(url)
if selected=="Mars":
    spec_mars()


# res=getData("https://api.nasa.gov/planetary/apod?api_key=kqLb0gOxi41stQHepqLUhUZ4FTT8SVh4J8zhp69Y",dt.date(2012,2,2))

# print(res)
# st.subheader(res["title"]+":bulb:")
# st.write("DATE  "+str(res["date"]) )
# st.image(res["hdurl"])
# st.write("__"+res["explanation"]+"__")












