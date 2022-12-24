#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import folium
import requests

df = pd.read_csv(r'C:\Users\ozarr\crime.csv', encoding='ISO-8859-1')
df.head()

print(df[pd.notnull(df["Location"])]["Location"].count())
print(df.shape[0])
# no null entries for lat/long


# The dataset I am using contains crime data from the city of Bostonm, provided by the BPD (Boston Police Department). It includes the date and time of the crime, the classification of the crime, and the location (lat,long) of the crime. It also includes the neighborhood of which the crime happened in.

# In[26]:


#coordinates set to Boston
map_osm = folium.Map(location=[42.3601, -71.0589], zoom_start=13)
map_osm


# In[27]:


#Using the offense description column to choose which types of crimes I want to plot on the graph
print(df.dtypes)
list = df['OFFENSE_DESCRIPTION'].value_counts()
#display(list.to_string())

df = df[df['Lat'].notna()]
df = df[df['Long'].notna()]


# In[28]:


for index, crime in df.iterrows():
    if crime["OFFENSE_DESCRIPTION"] == 'PROSTITUTION - COMMON NIGHTWALKER':
        folium.Marker(location=[crime["Lat"], crime["Long"]],
                    icon=folium.Icon(color='red')).add_to(map_osm)
        
    if crime["OFFENSE_DESCRIPTION"] == 'ABDUCTION - INTICING':
        folium.Marker(location=[crime["Lat"], crime["Long"]],
                    icon=folium.Icon(color='blue')).add_to(map_osm)
map_osm 


# In this map, I tried to see if the locations of abductions from inticement were linked to the location of prostitution on the street, and if they clustered in a general area or were tied to a specific neighborhood. From my analysis, I can conclude that there is no trend between the location of the 2 types of crimes. However, I can see that most of the 2 types of crimes I looked at happen outside of downtown Boston, and more in rural areas. For reference, I marked the prostitution crimes as red and the abduction crimes and blue.
