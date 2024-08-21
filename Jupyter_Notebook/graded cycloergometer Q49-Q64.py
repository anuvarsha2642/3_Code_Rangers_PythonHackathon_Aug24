#!/usr/bin/env python
# coding: utf-8

# In[352]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


# In[353]:


df_kayaking=pd.read_excel('V02Max_Combined.xlsx','Kayaking')
df_kayaking


# In[354]:


df_athletes=pd.read_excel('V02Max_Combined.xlsx','Athletes')
df_athletes


# In[355]:


df_triathlon=pd.read_excel('V02Max_Combined.xlsx','Triathlon')
df_triathlon


# In[279]:


df_fencing=pd.read_excel('V02Max_Combined.xlsx','Fencing')
df_fencing


# In[446]:


df_sports=pd.read_excel('V02Max_Sports.xlsx')
df_sports


# Question 49 Retrieve the row with minimum IBI for fencing athletes using sorting technique.

# In[281]:


df_fencing['IBI'] = df_fencing['RR']/1000


# In[282]:


df_fencing


# In[283]:


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


# Question51 List every athletes VO2

# In[362]:


df_Sum_VO2=df_sports.groupby('ID')['VO2'].sum().reset_index()

df_merge_VO2=pd.merge(df_athletes, df_Sum_VO2[['ID', 'VO2']], on='ID')
df_merge_VO2['VO2max']=df_merge_VO2['VO2']/df_merge_VO2['Weight']
df_merge_VO2


# In[364]:


df_merge_VO2[['ID','VO2max']]


# In[ ]:


Question 52 Using all markers of fitness available to you, who is fittest athlete. Write 1-2 lines about the analysis that led to your insight.


# In[331]:


df_sports['VO2'].max()


# In[332]:


df_sports['power'].max()


# In[334]:


df_sports['fit'] = df_sports['power'] + df_sports['VO2']


# In[335]:


df_maxfit=df_sports['fit'].max()
df_maxfit


# In[336]:


df_sports = df_sports[df_sports['fit']==df_maxfit]


# In[337]:


df_sports


# In[ ]:


# The athlete who is the fittest among other is selected based on having maximum VO2 and power combined.


# Question 53 phonebook={"john":938477566,"Jack":938377264,"Jill":947662781}  ,find the phone number of Jill

# In[161]:


phonebook={"john":938477566,"Jack":938377264,"Jill":947662781} 


# In[162]:


print(phonebook)


# In[163]:


print(phonebook["Jill"])


# In[ ]:


Question 54 Create a Pie chart for  Athletes and explode the wedge with Highest V02 kg/ml in and Label by Athlete ID


# In[382]:


plt.figure(figsize=(12, 12))

df_merge_VO2.plot.pie(y='VO2max', autopct='%1.1f%%', startangle=140, legend=False)
plt.ylabel('ID') 
plt.title('Athletes with highest VO2')


# QUESTION 55 Using a for loop iterate through HR for all triathletes and display all details of the athlete with the highest heart rate

# In[447]:


df_triathlon['HR'] = 60/(df_triathlon['RR']/1000)


# In[448]:


df_triathlon


# In[449]:


max_HR= df_triathlon['HR'].max()
max_HR


# In[450]:


# empty row
row_max_HR=[]


# In[451]:


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





# In[383]:





# In[ ]:





# In[ ]:


get_ipython().set_next_input('Question 58 What is the average % difference in heart rate between warm up and GET for all athletes');get_ipython().run_line_magic('pinfo', 'athletes')


# In[348]:


df_sports["stage"] = ""
df_sports.loc[df_sports["power"] == 0, "stage"] = "cooldown"
df_sports.loc[df_sports["time"] < 0, "stage"] = "warmup"
df_sports.loc[df_sports["power"] > 0, "stage"] = "GET"


# In[349]:


df_sports


# In[ ]:


df[percent] = (df['column_name'] / df['column_name'].sum()) * 100


# In[ ]:


percentage= (df_sports['stage']-df_sports['warmup'])/df_sports['warmup']*100


# In[ ]:


df[percentage].mean()


# In[ ]:





# Question 59 Who is the tallest athlete in the dataset. What is his sport and his Vo2 ml/kg?

# In[424]:


df_merge_VO2


# In[425]:


df_maxheight = df_merge_VO2['Height'].max()
df_maxheight


# In[430]:


df_athletes_height = df_merge_VO2[df_merge_VO2['Height']== df_maxheight]


# In[431]:


df_athletes_height


# In[433]:


df_athletes_height = pd.DataFrame(df_athletes_height)


# In[436]:


df_athletes_height[['sport','VO2max']]


# Question 60 get the last letter of athletes last names using RegEX

# In[309]:


text=df_athletes['Last Name']
text  


# In[312]:


pattern = re.compile(r'^(.).*\1$')
matches = pattern.finditer(text)
return [match.group(0) for match in matches]



    


# In[ ]:





# In[303]:


text=df_athletes['Last Name']
text


# In[300]:


text


# Question 61 Reverse an arrays order in Python. You can use any array with any values you like.

# In[132]:


array = ['A','R','R','A','Y']


# In[133]:


rev = array[::-1]


# In[134]:


rev


# In[ ]:


Question 63 On average how many minutes did each athlete in the sport of fencing spend in Zone 5?


# In[452]:


df_sports


# In[453]:


df_sports['HR'] = 60/(df_sports['RR']/1000)
df_sports


# In[454]:


df_sports["zone"]= df_sports["HR"].apply(lambda x: "Zone 1" if x <100
                                     else "Zone 2" if x<=120
                                     else "Zone 3" if x <= 135
                                     else "Zone 4" if x<=155
                                     else "Zone 5")


# In[455]:


df_sports


# In[459]:


df_zone =pd.merge(df_athletes, df_sports, on='ID', how='inner')
df_zone


# In[467]:


df_zone5 = df_zone[(df_zone['sport'] == 'fencing') & (df_zone['zone'] == 'Zone 5')]
print(df_zone5)


# In[466]:


df_zone5


# In[483]:


df_avgminute_athlete = df_zone5.groupby('ID').mean()


# In[484]:


df_avgminute_athlete


# In[485]:


df_avgminute_athlete['time_in_minutes'] = df_avgminute_athlete['time']/60


# In[486]:


df_avgminute_athlete['time_in_minutes']


# Question 64 Count athletes based on Gender using count plot

# In[41]:



plt.figure(figsize=(5,5))
ax=sns.countplot(x ='Gender', data = df_athletes)
ax.bar_label(ax.containers[0])
plt.title('Count of athletes based on Gender')
plt.show()

