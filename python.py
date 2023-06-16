import pandas as pd  #for data manipulation
import numpy as np #for mathematical calculations
import seaborn as sns #for visualization
import pydeck as pdk #for map visualization
import streamlit as st #for BI
import matplotlib.pyplot as plt


## Read the dataset from the url link in DataGouv

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/4c176588-a444-4dc7-b6bf-60390ae7e5be", sep=";")


# check the NaN values in the dataset

df.isnull().sum()
df.info()

# Rename the columns to make it easier to manipulate 

df = df.rename(columns={
    'Extraction générée le 20 mars 2023': 'Date',
    'Unnamed: 1': 'Secteur d\'activité',
    'Unnamed: 2': 'Natures',
    'Unnamed: 3': 'Nombre de personnes impactées',
    'Unnamed: 4': 'Typologie de données impactées',
    'Unnamed: 5': 'Données sensibles',
    'Unnamed: 6': 'Origine de l\'incident',
    'Unnamed: 7': 'Causes de l\'incident',
    'Unnamed: 8': 'Informations complémentaires',
})


# Delete the first row  

df = df.drop(df.index[0])
df.head()   

# Delete the last column
#df = df.drop(df.columns[9], axis=1)
#df.head()



# convert the first column to date format YYYY-MM-DD

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Extract the year from the date column

df['Year'] = pd.DatetimeIndex(df['Date']).year


# Extract the month from the date column

df['Month'] = pd.DatetimeIndex(df['Date']).month

## convert the Month and year columns to string format

df['Month'] = df['Month'].astype(str)
df['Year'] = df['Year'].astype(str)
df.info()

## Histogram of the data breaches by year - 2018-2022 

# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df['Year'], bins=5, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Year - 2018-2022')
ax.set_xlabel('Year')
ax.set_ylabel('Frequency')

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()

# 2022 data breaches
df_2022 = df[df['Year'] == '2022']
## Replace the Month numbers with the month names
df_2022['Month'] = df_2022['Month'].replace(['1'], 'Jan')
df_2022['Month'] = df_2022['Month'].replace(['2'], 'Feb')
df_2022['Month'] = df_2022['Month'].replace(['3'], 'Mar')
df_2022['Month'] = df_2022['Month'].replace(['4'], 'Apr')
df_2022['Month'] = df_2022['Month'].replace(['5'], 'May')
df_2022['Month'] = df_2022['Month'].replace(['6'], 'June')
df_2022['Month'] = df_2022['Month'].replace(['7'], 'July')
df_2022['Month'] = df_2022['Month'].replace(['8'], 'Aug')
df_2022['Month'] = df_2022['Month'].replace(['9'], 'Sep')
df_2022['Month'] = df_2022['Month'].replace(['10'], 'Oct')
df_2022['Month'] = df_2022['Month'].replace(['11'], 'Nov')
df_2022['Month'] = df_2022['Month'].replace(['12'], 'Dec')


# 2021 data breaches
df_2021 = df[df['Year'] == '2021']
## Replace the Month numbers with the month names
df_2021['Month'] = df_2021['Month'].replace(['1'], 'Jan')
df_2021['Month'] = df_2021['Month'].replace(['2'], 'Feb')
df_2021['Month'] = df_2021['Month'].replace(['3'], 'Mar')
df_2021['Month'] = df_2021['Month'].replace(['4'], 'Apr')
df_2021['Month'] = df_2021['Month'].replace(['5'], 'May')
df_2021['Month'] = df_2021['Month'].replace(['6'], 'June')
df_2021['Month'] = df_2021['Month'].replace(['7'], 'July')
df_2021['Month'] = df_2021['Month'].replace(['8'], 'Aug')
df_2021['Month'] = df_2021['Month'].replace(['9'], 'Sep')
df_2021['Month'] = df_2021['Month'].replace(['10'], 'Oct')
df_2021['Month'] = df_2021['Month'].replace(['11'], 'Nov')
df_2021['Month'] = df_2021['Month'].replace(['12'], 'Dec')


# 2020 data breaches
df_2020 = df[df['Year'] == '2020']
## Replace the Month numbers with the month names
df_2020['Month'] = df_2020['Month'].replace(['1'], 'Jan')
df_2020['Month'] = df_2020['Month'].replace(['2'], 'Feb')
df_2020['Month'] = df_2020['Month'].replace(['3'], 'Mar')
df_2020['Month'] = df_2020['Month'].replace(['4'], 'Apr')
df_2020['Month'] = df_2020['Month'].replace(['5'], 'May')
df_2020['Month'] = df_2020['Month'].replace(['6'], 'June')
df_2020['Month'] = df_2020['Month'].replace(['7'], 'July')
df_2020['Month'] = df_2020['Month'].replace(['8'], 'Aug')
df_2020['Month'] = df_2020['Month'].replace(['9'], 'Sep')
df_2020['Month'] = df_2020['Month'].replace(['10'], 'Oct')
df_2020['Month'] = df_2020['Month'].replace(['11'], 'Nov')
df_2020['Month'] = df_2020['Month'].replace(['12'], 'Dec')


# 2019 data breaches
df_2019 = df[df['Year'] == '2019']
## Replace the Month numbers with the month names
df_2019['Month'] = df_2019['Month'].replace(['1'], 'Jan')
df_2019['Month'] = df_2019['Month'].replace(['2'], 'Feb')
df_2019['Month'] = df_2019['Month'].replace(['3'], 'Mar')
df_2019['Month'] = df_2019['Month'].replace(['4'], 'Apr')
df_2019['Month'] = df_2019['Month'].replace(['5'], 'May')
df_2019['Month'] = df_2019['Month'].replace(['6'], 'June')
df_2019['Month'] = df_2019['Month'].replace(['7'], 'July')
df_2019['Month'] = df_2019['Month'].replace(['8'], 'Aug')
df_2019['Month'] = df_2019['Month'].replace(['9'], 'Sep')
df_2019['Month'] = df_2019['Month'].replace(['10'], 'Oct')
df_2019['Month'] = df_2019['Month'].replace(['11'], 'Nov')
df_2019['Month'] = df_2019['Month'].replace(['12'], 'Dec')


# 2018 data breaches
df_2018 = df[df['Year'] == '2018']
## Replace the Month numbers with the month names
df_2018['Month'] = df_2018['Month'].replace(['1'], 'Jan')
df_2018['Month'] = df_2018['Month'].replace(['2'], 'Feb')
df_2018['Month'] = df_2018['Month'].replace(['3'], 'Mar')
df_2018['Month'] = df_2018['Month'].replace(['4'], 'Apr')
df_2018['Month'] = df_2018['Month'].replace(['5'], 'May')
df_2018['Month'] = df_2018['Month'].replace(['6'], 'June')
df_2018['Month'] = df_2018['Month'].replace(['7'], 'July')
df_2018['Month'] = df_2018['Month'].replace(['8'], 'Aug')
df_2018['Month'] = df_2018['Month'].replace(['9'], 'Sep')
df_2018['Month'] = df_2018['Month'].replace(['10'], 'Oct')
df_2018['Month'] = df_2018['Month'].replace(['11'], 'Nov')
df_2018['Month'] = df_2018['Month'].replace(['12'], 'Dec')


# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df_2022['Month'], bins=12, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Month - 2022')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency')
ax.invert_xaxis()

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()

# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df_2021['Month'], bins=12, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Month - 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency')
ax.invert_xaxis()

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()

# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df_2020['Month'], bins=12, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Month - 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency')
ax.invert_xaxis()

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()

# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df_2019['Month'], bins=12, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Month - 2019')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency')
ax.invert_xaxis()

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()

# Set figure size
sns.set(rc={'figure.figsize':(10,6)})

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df_2018['Month'], bins=12, kde=False, ax=ax)

# Set title and labels
ax.set_title('Data Breaches Distribution - By Month - 2018')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency')
ax.invert_xaxis()

# Add data labels inside each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center')

plt.show()


