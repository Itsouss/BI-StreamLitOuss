import pandas as pd  #for data manipulation
import numpy as np #for mathematical calculations
import seaborn as sns #for visualization
import pydeck as pdk #for map visualization
import streamlit as st #for BI
import matplotlib.pyplot as plt
## Read the dataset from the url link in DataGouv

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/4c176588-a444-4dc7-b6bf-60390ae7e5be", sep=";")

