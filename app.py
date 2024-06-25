import streamlit as st
import pandas as pd
import plotly.express as px

def page_settings(): 
    st.set_page_config(layout="wide",page_title="Data Practice App",page_icon="database.png")

page_settings()

st.write("# 📊 Descriptive Data Analysis App")
@st.cache_data
def load_data(n):
    School_data = pd.read_csv('Data/School.csv',index_col=0)
    Economy_data = pd.read_csv('Data/economy.csv',index_col=0)
    Covid_data = pd.read_csv('Data/Sample Covid.csv',index_col=0)
    if(n == 1):
        return School_data
    elif(n == 2):
        return Economy_data
    elif(n == 3):
        return Covid_data
    
Sdata = load_data(1)
Edata = load_data(2)
Cdata = load_data(3)

def msg():
    st.toast("Data Imported Successfully.",icon='✅')

# Toggles
climate = st.toggle("**Show Climate Conditions (Metrics)**",False)
SchooL = st.toggle("**Show School Data**",False)
Economy = st.toggle("**Show Economy Data**",False)
Covid = st.toggle("**Show Covid Data**",False)

@st.cache_data
def climate_Data():
    st.header("Climatic Conditions with Toggle")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 km/h", "-8%")
    col3.metric("Humidity", "86%", "4%")
    col4.metric("Air Quality", "Fair","Fair")

@st.cache_data
def school_Data():
    st.header("School Data")
    col1, Avg_maths, Avg_Attendance = st.columns(3)
    col1.dataframe(Sdata)
    Avg_maths.metric("Average Mathematics Marks",Sdata["Mathematics Marks"].median(),"-4")
    Avg_maths.line_chart(Sdata)
    Avg_Attendance.metric("Average Attendance",Sdata["Attendance"].median(),"10")
    Avg_Attendance.line_chart(Sdata)
    descriptive, df, chart= st.columns(3)
    descriptive.subheader("**Description about Numerical Data**")
    descriptive.dataframe(Sdata[["Mathematics Marks","Attendance"]].describe())
    df.subheader("Correlation Matrix")
    df.dataframe(Sdata[["Mathematics Marks","Attendance"]].corr())
    df.subheader("Topper Marks")
    df.dataframe(Sdata["Mathematics Marks"].mode())
    chart.subheader("Descriptive Chart")
    chart.bar_chart(Sdata[["Mathematics Marks","Attendance"]].corr())

@st.cache_data
def economy_Data():
    st.header("Indian Economy Data")
    df,correlation,chart = st.columns(3)
    df.dataframe(Edata)
    correlation.subheader("Correlation Matrix")
    correlation.dataframe(Edata.corr())
    chart.subheader("Descriptive Chart")
    chart.area_chart(Edata.corr())

@st.cache_data
def Covid_Data():
    st.header("Covid Data")
    df,pie,chart = st.columns(3)
    df.dataframe(Cdata)
    fig = px.pie(Cdata, values='Odds ratio', names='COVID-19', title='Effects of Covid-19 on Human Organs')
    pie.subheader("Pie Chart")
    pie.plotly_chart(fig)
    chart.subheader("Descriptive Chart")
    chart.bar_chart(Cdata,x_label='Diseases',y_label='Odds Ratio')


if climate:
    msg()
    climate_Data()

if SchooL:
    msg()    
    school_Data()

if Economy:
    msg()
    economy_Data()

if Covid:
    msg()
    Covid_Data()