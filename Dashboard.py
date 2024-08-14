import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
st.config.set_option("deprecation.showPyplotGlobalUse", False)
st.set_page_config(
    page_title="Bike Sharing Dataset",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Bike Sharing Dataset Analysis"
    }
)
# Title of the Dashboard
# Proyek Analisis Data: Bike-Sharing Dataset
st.write("Nama: APRILIA ANGGRAINI")
st.write("Email: apriliaanggraini164@gmail.com")
st.title('Bike Sharing Dataset')
st.subheader("Gathering Data")
st.code("hourly_data = pd.read_csv('hour.csv')")
st.code("daily_data = pd.read_csv('day.csv')")
hourly_data = pd.read_csv("./hour.csv")
daily_data = pd.read_csv("./day.csv")

# hourly_data = pd.read_csv("D:\CODING\DICODING\PY-DATA\Dicoding-Dashboard_Bike_Sharing_Dataset_Analysis\hour.csv")
# daily_data = pd.read_csv("D:\CODING\DICODING\PY-DATA\Dicoding-Dashboard_Bike_Sharing_Dataset_Analysis\day.csv")

# Display the raw data
st.header('Raw Data')
st.subheader('Hourly Data')
st.write(hourly_data.head())
st.subheader('Daily Data')
st.write(daily_data.head())

# Display the characteristics of the data
st.title('Characteristics of the Data')

# Information about Hourly Data
st.header('Hourly Data Characteristics')
st.write('Number of Rows:', hourly_data.shape[0])
st.write('Number of Columns:', hourly_data.shape[1])
col1, col2 = st.columns(2)
with col1:
    st.subheader('Data Types of Columns')
    st.write(hourly_data.dtypes)
with col2:
    st.subheader('Summary of Columns')
    st.write(hourly_data.describe())

# Information about Daily Data
st.header('Daily Data Characteristics')
st.write('Number of Rows:', daily_data.shape[0])
st.write('Number of Columns:', daily_data.shape[1])
col1, col2 = st.columns(2)
with col1:  
    st.subheader('Data Types of Columns')
    st.write(daily_data.dtypes)
with col2:
    st.subheader('Summary of Columns')
    st.write(daily_data.describe())

st.subheader('Checking Outliers')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Hourly Data')
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=daily_data[['temp', 'atemp', 'hum', 'windspeed']])
    plt.title('Boxplot untuk Data Cuaca')
    plt.xlabel('Variabel Cuaca')
    plt.ylabel('Nilai')
    st.pyplot()
with col2:
    st.subheader('Daily Data')
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=daily_data[['temp', 'atemp', 'hum', 'windspeed']])
    plt.title('Boxplot untuk Data Cuaca')
    plt.xlabel('Variabel Cuaca')
    plt.ylabel('Nilai')
    st.pyplot()

#SMART QUESTION
st.header('Menentukan Pertanyaan Bisnis')
st.write('- Apakah variabel cuaca berpengaruh terhadap tingkat jumlah penyewaan sepeda?')
st.write('- Bagaimana hubungan musim terhadap jumlah penyewaan sepeda dari tahun 2011 sampai 2012')
# Data Exploration
# Data Cleaning
st.header('Data Cleaning')
st.subheader('Mengubah Tipe Data')
st.code("hourly_data['dteday'] = pd.to_datetime(hourly_data['dteday']).dt.strftime('%Y-%m-%d')")
st.code("daily_data['dteday'] = pd.to_datetime(daily_data['dteday']).dt.strftime('%Y-%m-%d')")
# Convert 'dteday' column to datetime format and then convert to string (without time)
hourly_data['dteday'] = pd.to_datetime(hourly_data['dteday']).dt.strftime('%Y-%m-%d')
daily_data['dteday'] = pd.to_datetime(daily_data['dteday']).dt.strftime('%Y-%m-%d')

st.subheader('Menghilangkan beberapa kolom')
st.code("hourly_data = hourly_data.drop(['instant', 'atemp'], axis=1)")
st.code("daily_data = daily_data.drop(['instant', 'atemp'], axis=1)")
# Drop unnecessary columns
hourly_data = hourly_data.drop(['instant', 'atemp'], axis=1)
daily_data = daily_data.drop(['instant', 'atemp'], axis=1)

# Calculate IQR
Q1 = hourly_data['hum'].quantile(0.25)
Q3 = hourly_data['hum'].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
hourly_data = hourly_data[(hourly_data['hum'] >= lower_bound) & (hourly_data['hum'] <= upper_bound)]
daily_data = daily_data[(daily_data['hum'] >= lower_bound) & (daily_data['hum'] <= upper_bound)]
col1, col2 = st.columns(2)
with col1:
    st.subheader('Hourly Data')
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=daily_data[['temp', 'hum', 'windspeed']])
    plt.title('Boxplot untuk Data Cuaca')
    plt.xlabel('Variabel Cuaca')
    plt.ylabel('Nilai')
    st.pyplot()
with col2:
    st.subheader('Daily Data')
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=daily_data[['temp', 'hum', 'windspeed']])
    plt.title('Boxplot untuk Data Cuaca')
    plt.xlabel('Variabel Cuaca')
    plt.ylabel('Nilai')
    st.pyplot()

# Check for missing values
st.subheader('Missing Values Check & Data Type Check')
st.code("hourly_data.isnull().sum()")
st.code("daily_data.isnull().sum()")
col1, col2 = st.columns(2)
with col1:
    st.write("Checking Missing Values")
with col2:
    st.write('Checking Data Types')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write('Hourly Data:', hourly_data.isnull().sum())
with col2:
    st.write('Daily Data:', daily_data.isnull().sum())
with col3:
    st.write('Hourly Data:',hourly_data.dtypes)
with col4:
    st.write('Daily Data:',daily_data.dtypes)
st.subheader('Cleaned Data')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Hourly Data')
    st.write(hourly_data)
with col2:
    st.subheader('Daily Data')
    st.write(daily_data)
# Data Visualization
st.header('Data Visualization')

st.subheader('Apakah variabel cuaca berpengaruh terhadap tingkat jumlah penyewaan sepeda?')

col1, col2 = st.columns(2)
with col1:
# Plotting the scatter plot
    st.subheader('Hourly Data')
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=hourly_data, x='hum', y='temp', size='cnt', hue='weathersit', palette='viridis', sizes=(20, 200))
    plt.title('Pengaruh Variabel Cuaca terhadap Jumlah Penyewaan Sepeda')
    plt.xlabel('Humidity')
    plt.ylabel('Temperature')
    plt.legend(title='Weather Situation')
    plt.show()
    st.pyplot()
with col2:
    st.subheader('Daily Data')
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=daily_data, x='hum', y='temp', size='cnt', hue='weathersit', palette='viridis', sizes=(20, 200))
    plt.title('Pengaruh Variabel Cuaca terhadap Jumlah Penyewaan Sepeda')
    plt.xlabel('Humidity')
    plt.ylabel('Temperature')
    plt.legend(title='Weather Situation')
    plt.show()
    st.pyplot()
    
st.subheader('Bagaimana hubungan musim terhadap jumlah penyewaan sepeda dari tahun 2011 sampai 2012')
# Plotting the bar plot

col1, col2 = st.columns(2)
with col1:
    st.subheader('Hourly Data')
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(data=hourly_data, x='season', y='cnt', hue='yr', palette=['red', 'yellow'])
    plt.title('Perubahan Jumlah Penyewaan Sepeda dari Tahun 2011 sampai 2012 pada setiap musimnya')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, ['2011', '2012'], title='Tahun')
    labels = daily_data.groupby(['season', 'yr'])['cnt'].sum()
    print(labels)
    plt.tight_layout()
    plt.show()
    st.pyplot()
with col2:
    st.subheader('Daily Data')
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(data=daily_data, x='season', y='cnt', hue='yr', palette=['red', 'yellow'])
    plt.title('Perubahan Jumlah Penyewaan Sepeda dari Tahun 2011 sampai 2012 pada setiap musimnya')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, ['2011', '2012'], title='Tahun')
    labels = daily_data.groupby(['season', 'yr'])['cnt'].sum()
    print(labels)
    plt.tight_layout()
    plt.show()
    st.pyplot()

st.header('Conclusion')
st.subheader("Pertanyaan 1")
st.write('- Apakah variabel cuaca berpengaruh terhadap tingkat jumlah penyewaan sepeda?')
st.write("Pengaruh Cuaca terhadap Penyewaan Sepeda: Faktor-faktor cuaca seperti suhu, kelembaban, dan kondisi cuaca secara signifikan memengaruhi tingkat penyewaan sepeda. Cuaca yang cerah dan hangat cenderung meningkatkan jumlah penyewaan, sementara cuaca buruk atau suhu rendah menyebabkan penurunan. Oleh karena itu, disarankan agar perusahaan penyewaan sepeda dapat menyesuaikan strateginya dengan prakiraan cuaca, seperti melakukan penyesuaian pemasaran, menawarkan promosi khusus, atau memberikan layanan tambahan. Dengan demikian, perusahaan dapat lebih adaptif terhadap kondisi cuaca dan meningkatkan kinerja bisnisnya.")
st.subheader("Pertanyaan 2")
st.write('- Bagaimana hubungan musim terhadap jumlah penyewaan sepeda dari tahun 2011 sampai 2012')
st.write("Tren Penyewaan Sepeda dari Tahun ke Tahun dan Tren Musiman: Meskipun terdapat peningkatan lebih dari 10% dalam penyewaan sepeda dari tahun 2011 ke 2012, terdapat juga tren musiman yang menunjukkan penurunan signifikan selama musim semi, mungkin karena cuaca yang lebih hangat. Oleh karena itu, dianjurkan agar perusahaan menyewaan sepeda mempertimbangkan strategi khusus seperti kampanye atau promosi paket untuk meningkatkan minat dalam penyewaan sepeda selama musim-musim dengan kunjungan yang lebih rendah. Dengan mengadopsi pendekatan ini, perusahaan dapat mengoptimalkan pendapatan dan layanan sepanjang tahun.")