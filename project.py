#!/usr/bin/env python
# coding: utf-8

# # Project Title: Air Q Assessment TN
# 
# Dataset Link: https://tn.data.gov.in/resource/location-wise-daily-ambient-air-quality-tamil-nadu-year-2014
# 
# ## Phase 1: Project Definition and Design Thinking
# 
# ### Project Definition: 
#     
#     The project aims to analyze and visualize air quality data from monitoring stations in Tamil Nadu. The objective is to gain insights into air pollution trends, identify areas with high pollution levels, and develop a predictive model to estimate RSPM/PM10 levels based on SO2 and NO2 levels. This project involves defining objectives, designing the analysis approach, selecting visualization techniques, and creating a predictive model using Python and relevant libraries.
# 
# ### Design Thinking:
# 
#         Project Objectives: Define objectives such as analyzing air quality trends, identifying pollution hotspots, and building a predictive model for RSPM/PM10 levels.
#         Analysis Approach: Plan the steps to load, preprocess, analyze, and visualize the air quality data.
#         Visualization Selection: Determine visualization techniques (e.g., line charts, heatmaps) to effectively represent air quality trends and pollution levels.
# 
# ## Phase 2: Innovation
# 
# 
# ## Phase 3: Development Part 1
# 
# In this phase we'll begin the analysis by loading and preprocessing the air quality dataset with the help of python module named as 'pandas'.
# 
# **Install pandas module**
# > pip install pandas
# 
# Now, import the module
# > pip import pandad as pd
# 
# Load dataset
# >rawdata_df = pd.read_csv(r"C:\Users\vicky\Desktop\Project\dataset.csv")
# ![Alt text](image.png)
# 
# Output:
# ![Alt text](image-1.png)
# View Columns Data of row 1
# 
# ![Alt text](image-2.png)
# 
# 
# 
# 
# 
# 
# 

# In[5]:


import pandas as pd


# In[10]:


rawdata_df = pd.read_csv(r"C:\Users\vicky\Desktop\Project\dataset.csv")


# # Data Set
# 

# In[11]:


rawdata_df


# In[12]:


rawdata_df.columns


# In[13]:


selected_columns=(['Stn Code', 'Sampling Date', 'State', 'City/Town/Village/Area',
       'Location of Monitoring Station', 'Agency', 'Type of Location', 'SO2',
       'NO2', 'RSPM/PM10', 'PM 2.5'])


# # Data Preparation and Cleaning

# In[17]:


analysis_df = rawdata_df[selected_columns].copy()


# In[18]:


analysis_df


# Let's view some basic information about the data frame.

# In[19]:


analysis_df.shape


# In[20]:


analysis_df.info()


# Most columns have the data type object, either because they contain values of different types, or they contain empty values, which are represented using NaN. It appears that every column contains some empty values, since the Non-Null count for every column is lower than the total number of rows (29531). We'll need to deal with empty values and manually adjust the data type for each column on a case-by-case basis.
# 
# Only two of the columns were detected as contain empty values and we will drop the rows. 
# 
# let's convert 'Date' columns into datetime64[ns] data type since its data type is objet.

# analysis_df.describe()

# In[23]:


analysis_df.describe()


# In[26]:


analysis_df.dropna(subset=['SO2'], inplace=True)
analysis_df.dropna(subset=['NO2'], inplace=True)


# In[27]:


analysis_df


# In[29]:


analysis_df['Location of Monitoring Station']


# Let's view again basic information about the data frame.

# In[30]:


analysis_df.shape


# In[31]:


analysis_df.info()


# In[32]:


analysis_df.describe()


# After Data Cleaning like removing empty rows and changing data type.
# 
# 

# #  Exploratory Analysis and Visualization
# 
# It's important to Visualize the data to understand the data clearly.For that we will matplotlib / seaborn library.
# 
# Let's begin by importing matplotlib.pyplot and seaborn.

# In[33]:


pip install seaborn


# In[34]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[40]:


Location_of_Monitoring_Station = analysis_df['Location of Monitoring Station'].value_counts()
Location_of_Monitoring_Station


# In[57]:


plt.figure(figsize=(10,6))
plt.title('Location_of_Monitoring_Station')
plt.pie(Location_of_Monitoring_Station, labels=Location_of_Monitoring_Station.index, autopct='%1.0f%%', startangle=400);


# In[60]:


sns.countplot(y=analysis_df.SO2)
plt.xticks(rotation=75);
plt.title('SO2')
plt.ylabel(None);


# In[65]:


sns.countplot(y=analysis_df.NO2)
plt.xticks(rotation=70);
plt.title('NO2')
plt.ylabel(None);


# In[ ]:




