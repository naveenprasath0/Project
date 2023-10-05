#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_excel('D:/Mano/jupyter projects/fake review/review names.xlsx')
df


# In[3]:


a = df[['id']]
a


# In[4]:


b = df[['name']]
b


# In[7]:


inp = input("Enter Customer ID:")
lst1=[]
lst2=[]
lst3=[]
for i in df.index:
    if df.loc[i,'id'] == inp:
        a = df.loc[i,'id']
        b = df.loc[i,'name']
        c = df.loc[i,'description']
        lst1.append(a)
        lst2.append(b)
        lst3.append(c)
print(lst1, sep='\n')
print('')
print("Number of fake ID's ",len(lst1))
print('')

print(lst2,sep = '\n')
print('')
print('Number of fake names',len(lst1))
print('')

print(*lst3, sep = '\n')
print('')
print('Number of fake reviews',len(lst1))


# In[5]:


import matplotlib.pyplot as plt
# Scatter plot with day against tip
plt.scatter(df['rating'], df['likes_count'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Rating')
plt.ylabel('Likes Count')

plt.show()


# In[8]:


import seaborn as sns
sns.regplot(df['rating'], df['likes_count'])

