#!/usr/bin/env python
# coding: utf-8

# ![LL%20&%20SU.jpg](attachment:LL%20&%20SU.jpg)

# # Assignment \#5 Part 1: Matplotlib
# Data set used: an open source dataset containing car specifications.
# 
# For part 1 of Assignment 5, you are only allowed to use Matplotlib, no seaborn or built in pandas plotting.
# 
# ## Ensure all graphs are titled and labelled.
# **You will receive an impression mark for the overall presentation of your graphs, therefore you are advised to use different colormaps, markers, grids, linestyles, etc**

# In[10]:


#imports and data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('src/mpg.csv')
df['origin'] = df['origin'].str.upper()
df = df.dropna()
df


# # Data Types
# 
# Before plotting your data, it is important to understand its composition. 
# 
# Answer below for each of the indicated features, if it is categorical or numerical. 
# 
# Furthermore, if a feature is numerical, further add if it is discrete or continuous?
# 
# As for categorical features, are they nominal or ordinal?
# 
# 

# ## *Answer below*
# ### MPG
# Numerical. Continuous.
# 
# ### Cylinders
# Numerical. Discrete. 
# 
# ### Discplacement
# Numerical. Continuous.
# 
# ### Horsepower
# Numerical. Continuous.
# 
# ### Weight
# Numerical. Discrete. 
# 
# ### Accelartion
# Numerical. Continuous. 
# 
# ### Model Year
# Numerical. Discrete. 
# 
# ### Origin
# Categorical.

# ## Plotting distributions
# Next we will analyze the distribution of each feature, through a histogram
# 
# Finish the code below to plot histograms for each of the following features: *MPG, Cylinders, Displacement, Horsepower, Weight, Acceleration, Model Year, Origin*
# 
# For continuous features, use the default binsize of matplotlib.

# In[2]:


fig, axs = plt.subplots(4,2,figsize=(10,20))

axs[0, 0].hist(df['mpg'], bins= 20)
axs[0, 0].set_title('MPG ')
axs[0, 1].hist(df['cylinders']) 
axs[0, 1].set_title('Cylinders')
axs[1, 0].hist(df['acceleration'])
axs[1, 0].set_title('Acceleration')
axs[1,1].hist(df['origin'], bins = 3)
axs[1,1].set_title('Origin')
axs[2,0].hist(df['displacement'])
axs[2,0].set_title('Displacement')
axs[2,1].hist(df['horsepower'])
axs[2,1].set_title('Horsepower')
axs[3,0].hist(df['weight'])
axs[3,0].set_title('Weight')
axs[3,1].hist(df['model_year'], bins = 15)
axs[3,1].set_title('Model Year')

for ax in axs.flat:
    ax.set(xlabel='Variable of Interest', ylabel='Frequency')


# ## From the histograms above, choose the feature which most closely resembles a normal distribution:
# The acceleration variable most closely resembles a normal distribution. This is because of its relatively bell-shaped curve of its distribution.  
# 

# # Emphasising correlation
# 
# ## Complete the code below to plot a scatterplot for MPG vs Weight.
# 
# Furthermore, indicate using colours the different origins of each point.

# In[3]:


fig, ax = plt.subplots(figsize=(7,6))

colors = {'USA':'tab:blue', 'JAPAN':'tab:red', 'EUROPE':'tab:green'}

ax.scatter(df["mpg"], df["weight"])
ax.set_xlabel("mpg")
ax.set_ylabel('weight')

plt.show()


# ### Does MPG and Weight have positive, negative or no correlation
# MPG and Weight have a negative correlation. This can be seen on the scatterplot by the downward trend in the data. 
# 

# ## Complete the code below to plot a scatterplot of MPG vs Acceleration
# Furthermore, indicate using colours the different origins of each point.

# In[4]:


fig, ax = plt.subplots(figsize=(7,6))

colors = {'USA':'tab:blue', 'JAPAN':'tab:red', 'EUROPE':'tab:green'}
grouped = df.groupby("acceleration")["mpg"].size()
for index, df in grouped:
    ax.scatter(df["weight"], df["mpg"], color = colors[index], labels = index)
# insert code here
#ax.scatter(df["mpg"], df["acceleration"], color = colors)
#ax.set_xlabel("mpg")
#ax.set_ylabel('acceleration')

plt.show()


# ### Does MPG and Weight have positive, negative or no correlation
# The cloud-like distribution of the data indicates that there is no correlation.
# 

# # Visualising categoricals features
# 
# ## Plot a pie chart of model years
# Clearly indicate each segements' numerical percentage.

# In[ ]:


fig, ax = plt.subplots(figsize=(7,6))

# insert code here
df.model_year.value_counts().plot(kind='pie')
plt.show()


# ## Plot a pie chart of origin
# Clearly indicate each segements' numerical percentage.

# In[ ]:


fig, ax = plt.subplots(figsize=(7,6))

# insert code here
df.origin.value_counts().plot(kind='pie')
plt.show()


# ## Why is using pie charts bad when analysing categorical features?
# Hint: This drawback is especially predominant in the first pie chart.
# 
# It is not clear to easily identify the different proportions of interest, as it is as easy to read as another type, like a barchart. It would make analysing the data by eye significantly easier to interpret. 
# 

# ## It is better to rather use barplots when visualising categorical features. 
# Therefore once again plot the model year and origin on two seperate graphs.
# But instead using barplots this time.

# In[5]:


fig, ax = plt.subplots(figsize=(7,6))

# Plot a bar-chart of gold medals as a function of country
#ax.bar(df['model_year'].index, df['model_year'].count)


new = df.groupby("model_year")["mpg"].size()

ax.bar(new.index,new)

plt.xlabel("Model Year")
plt.ylabel("Frequency")
plt.show()


# In[6]:


fig, ax = plt.subplots(figsize=(7,6))

# insert code here

new = df.groupby("origin")["mpg"].size()

ax.bar(new.index,new)

plt.xlabel("Origin")
plt.ylabel("Frequency")

plt.show()


# # Working with time series
# Next we will be working with a new dataset: 
# 
# The daily temperature for an arbitrary location was recorded from 1981 to 1991.
# 
# Once again answer the following questions plotting only with matplotlib.
# 
# Hint: For some of the following questions it is necessary to restructure the dataframe first using pd.groupby(). Seperating each year into a new dataframe column.
# 

# In[11]:


# Load in data
ts = pd.read_csv('src/temps.csv', index_col=0, parse_dates=True, header=0, squeeze=True)
ts.head()
ts = ts.to_frame()


# ## Plot the daily temperature for each recorded measurement.

# In[12]:


fig, ax = plt.subplots(figsize=(12,5))

# insert code here
ax.plot(ts, color="green")


# ## Comparing different years
# Complete the code below to plot the temperature of each year on a different subplot.

# In[16]:


fig, ax = plt.subplots(10,1,figsize=(10,20))
ax[0].plot(ts['1981'], color="purple")
ax[1].plot(ts['1982'], color = "blue")
ax[2].plot(ts['1983'], color = "green")
ax[3].plot(ts['1984'], color = "cyan")
ax[4].plot(ts['1985'], color = "orange")
ax[5].plot(ts['1986'], color = "pink")
ax[6].plot(ts['1987'], color = "red")
ax[7].plot(ts['1988'], color = "blue")
ax[8].plot(ts['1989'], color = "green")
ax[9].plot(ts['1990'], color = "pink")
ax[10].plot(ts['1991'], color = "purple")
#fig.suptitle('Daily Temperature Recorded for each respective year')
#plt.tight_layout()
#fig.subplots_adjust(top=0.95)
#plt.show()


# ## Comparing distributions of time intervals
# To properly visualise and compare the distributions of yearly or monthly data, we employ the use of boxplots.
# 
# ### Write code below to plot a boxplot for the temperatures of each respective year.

# In[ ]:


fig, ax = plt.subplots(figsize=(10,5))

df.reset_index(inplace=True)

# Prepare data
df['Date'] = [d.year for d in df.Date]
years = df['year'].unique()

# Draw Plot
fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
sns.boxplot(x='year', y='value', data=df, ax=axes[0])
sns.boxplot(x='month', y='value', data=df.loc[~df.year.isin([1991, 2008]), :])

# Set Title
axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18); 
axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)
plt.show()


# insert code here
#grouped.plot(kind='box')
# Add x-axis tick labels:
#plt.tight_layout()
#lt.show()

# Add a y-axis label


# ### If answered correctly, we can see that 1982 had the largest spread in recorded temperature. 
# We therefore seek to further analyse this specific year. Finish the code below to plot boxplots for each month in 1982.
# 

# In[ ]:


fig, ax = plt.subplots(figsize=(10,5))
x_labels = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# insert code here

plt.show()

