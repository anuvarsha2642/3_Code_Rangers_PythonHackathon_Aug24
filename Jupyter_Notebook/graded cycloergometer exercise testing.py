#!/usr/bin/env python
# coding: utf-8

# In[235]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


# In[236]:


df_kayaking=pd.read_excel('V02Max_Combined.xlsx','Kayaking')
df_kayaking


# In[237]:


df_athletes=pd.read_excel('V02Max_Combined.xlsx','Athletes')
df_athletes


# In[238]:


df_triathlon=pd.read_excel('V02Max_Combined.xlsx','Triathlon')
df_triathlon


# In[239]:


df_fencing=pd.read_excel('V02Max_Combined.xlsx','Fencing')
df_fencing


# Question 49 Retrieve the row with minimum IBI for fencing athletes using sorting technique.

# In[240]:


df_fencing['IBI'] = df_fencing['RR']/1000


# In[241]:


df_fencing


# In[242]:


df_fencing.sort_values(by='IBI',ascending=True).iloc[0] ###Retriewing the row with minimum IBI


# In[243]:


df_fencing.drop(columns=['IBI'], inplace=True)


# In[244]:


df_fencing


# Question 50 Create a violin chart using any 2 columns in the dataset

# In[42]:



plt.figure(figsize=(5,5))
ax=sns.violinplot(x ='Gender',y='age', data = df_athletes,split=True,inner='quartile')
plt.title('Gender vs Age')
plt.show()


# Question 51 List every athlete’s V02 ml/kg

# In[186]:


df_fulldata = pd.merge(df_kayaking, df_athletes, on='ID', how='outer')

# Merge the result with the third DataFrame
df_fulldata = pd.merge(df_fulldata, df_triathlon, on='ID', how='outer')

# Merge the result with the fourth DataFrame
df_fulldata = pd.merge(df_fulldata, df_fencing, on='ID', how='outer')


# In[187]:


df_fulldata


# In[188]:


df_fulldata['VO2'].max()


# In[189]:


df1=df_fulldata.groupby('ID')['VO2'].max()
df1


# In[ ]:


Question 52 Using all markers of fitness available to you, who is fittest athlete. Write 1-2 lines about the analysis that led to your insight.


# In[99]:


df_fulldata = pd.merge(df_kayaking, df_athletes, on='ID', how='right')

# Merge the result with the third DataFrame
df_fulldata = pd.merge(df_fulldata, df_triathlon, on='ID', how='right')

# Merge the result with the fourth DataFrame
df_fulldata = pd.merge(df_fulldata, df_fencing, on='ID', how='right')


# In[100]:


df_fulldata


# In[101]:


df_fulldata['VO2'].max()


# In[102]:


df_fulldata['power'].max()


# In[103]:


df_fulldata[['VO2','power']].max()


# In[104]:


fittestathlete = df_fulldata.groupby('ID').agg({
    'VO2': 'max',
    'power': 'max'
}).reset_index()


# In[108]:


fittestathlete


# Question 53 phonebook={"john":938477566,"Jack":938377264,"Jill":947662781}  ,find the phone number of Jill

# In[161]:


phonebook={"john":938477566,"Jack":938377264,"Jill":947662781} 


# In[162]:


print(phonebook)


# In[163]:


print(phonebook["Jill"])


# QUESTION 55 Using a for loop iterate through HR for all triathletes and display all details of the athlete with the highest heart rate

# In[191]:


df_triathlon['HR'] = 60/df_triathlon['RR']


# In[192]:


df_triathlon


# In[216]:


max_HR= df_triathlon['HR'].max()
max_HR


# In[217]:


# empty row
row_max_HR=[]


# In[218]:


for index,row in df_triathlon.iterrows():
    if row['HR'] == max_HR :
        row_max_HR.append(row)
        
row_max_HR = pd.DataFrame(row_max_HR)
row_max_HR


# Question 56 Display a histogram to show distribution of athletes by sport.

# In[40]:



plt.figure(figsize=(5,5))
ax=sns.histplot(x ='sport', data = df_athletes)
ax.bar_label(ax.containers[0])
plt.title('Athletes by Sport')
plt.show()


# Question 57 get the first letter of last name of students using for loops and RegEX

# In[ ]:





# In[ ]:





# In[ ]:





# Question 59 Who is the tallest athlete in the dataset. What is his sport and his Vo2 ml/kg?

# In[135]:


df_maxheight=df_athletes['Height'].max()
df_maxheight


# In[136]:


df_athletes_height = df_athletes[df_athletes['Height']== df_maxheight]


# In[140]:


df_athletes_height


# In[145]:


df_athletes_height['sport']


# Question 60 get the last letter of athletes last names using RegEX

# In[ ]:



    


# In[153]:





# In[ ]:


last_letter=[]


# In[159]:


text=df_athletes['Last Name']
text


# In[ ]:





# Question 61 Reverse an arrays order in Python. You can use any array with any values you like.

# In[132]:


array = ['A','R','R','A','Y']


# In[133]:


rev = array[::-1]


# In[134]:


rev


# Question 64 Count athletes based on Gender using count plot

# In[41]:



plt.figure(figsize=(5,5))
ax=sns.countplot(x ='Gender', data = df_athletes)
ax.bar_label(ax.containers[0])
plt.title('Count of athletes based on Gender')
plt.show()

