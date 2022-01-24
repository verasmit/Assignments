#!/usr/bin/env python
# coding: utf-8

# ![LL%20&%20SU.jpg](attachment:LL%20&%20SU.jpg)

# # Assignment \#4: Importing and Cleaning Data
# The following questions are based on the data from 'sensors.csv' and 'readings.csv'
# 
# 'sensors.csv' contains the coordinates for weather sensors used to record the temperature for a given time.
# 
# 'reading.csv' stores the temperature reading together with the time for a given sensor.
# 
# The data, however, requires cleaning before it can be analysed. Execute the following cells to examine the raw data.

# In[2]:


# imports
import pandas as pd
from IPython.display import display
from IPython.display import Image
from IPython.display import HTML

sensors = pd.read_csv('src/sensors.csv', index_col='SensorID')
readings = pd.read_csv('src/readings.csv', index_col='ReadingID')

sensors


# As you can see the dataframe 'sensors' currenlty stores both the latitude and longitude for a sensor within the same column. 
# 
# Start off by writing code to seperate this into two columns namely, "Latitude" and "Longitude"

# In[3]:


import pandas as pd
from IPython.display import display
from IPython.display import Image
from IPython.display import HTML

sensors = pd.read_csv('src/sensors.csv', index_col='SensorID')
readings = pd.read_csv('src/readings.csv', index_col='ReadingID')

sensors[['Lat','Long']] = sensors.StationLocation.str.split(expand=True)
sensors = sensors.drop(columns=['StationLocation'])

sensors = sensors.replace(to_replace='\(|\,|\)|', value="", regex=True)

print(sensors)


# In[4]:


display(Image(filename='src/ex1.png'))


# Next we can move on to the temperature readings. Below we see that the readings require some cleaning. 
# 
# Firstly, the date time format must be cleaned to be used for queries. To do so we must convert the dtype to datetime64\[ns\]. 
# (hint: pandas has a built in function to perform this)
# 
# Secondly, the temperature must be converted from Fahrenheit to Celsius.

# In[5]:


readings.head()


# In[6]:


# insert code here to clean the DateTime column to be of type datetime64[ns]

readings['DateTime'] = pd.to_datetime(readings['DateTime'])
print(readings)


# In[7]:


# insert code here to convert Fahrenheit to Celsius

readings['AirTemperature'] = (readings['AirTemperature'] - 32)*(5/9)
print(readings)


# In[8]:


# print the final table
display(Image(filename='src/ex2.png'))


# # Selecting the appropriate data
# Now that the data has been cleaned. We can analyse only that which is necessary.
# 
# For the rest of this assignment we are only interested in the measurements that took place on 2019-09-17 between 14:00 and 15:00.
# 
# Write code below to drop all entries outside of the indicated time.

# In[11]:


# insert code to drop all entries outside the specified time

readings[(readings['DateTime'] > '2014-09-17 14:00:00') & (readings['DateTime'] < '2019-09-17 15:00:00')]


# # Missing values
# Now that we have the portion of data we want to work with,
# we can check if there are any missing values within the remaining data.
# 
# Display all entries which have missing values below.

# In[12]:


# insert code to display all null records containing null values

null_records = readings[readings.isnull().any(axis=1)]
print(null_records)


# # Discuss the following
# 
# There are several strategies one can follow to combat missing values. 
# 
# Discuss in this cell, why simply imputing the mean of all recorded temperatures would not be a fitting solution in this case.
# 
# #Answer: replacing NA values with the mean since the standard errors of statistical estimates will be lower than what they may otherwise have been. Furthermore, a smaller variance in the data would mean that we are introducing bias to the results

# # Drop Null Values
# We have decided to drop the entries containg null values, instead of imputing them.

# In[13]:


# write the code below te drop all null values and print out the resulting dataframe
readings.dropna()
print(readings)


# # Perform the panda equivalent operations of SQL queries
# Next you will be given a SQL query which you are tasked with executing, by using the equivalent pandas functions.
# Ensure that you are working with only the data that took place on 2019-09-17 between 14:00 and 15:00.
# 
# Write code below to perform the SQL query using the pandas library:
# 
# ## Query 1:
# 
# SELECT StationName, AVG(RoadSurfaceTemperature), AVG(AirTemperature)
# 
# FROM readings
# 
# GROUP BY StationName

# In[29]:


# write the equivalent SQL operation using pandas functions and display the resulting dataframe
grouped = readings.groupby(['StationName'])
print(grouped)


# ## Query 2:
# SELECT StationName, COUNT(*) as No_Readings
# 
# FROM readings
# 
# GROUP BY StationName

# In[24]:


# write the equivalent SQL operation using pandas functions and display the resulting dataframe
display(readings['StationName'].isna())


# ## Query 3:
# 
# SELECT StationName,  AVG(RoadSurfaceTemperature), AVG(AirTemperature) Latitude, Longitude
# 
# FROM readings
# 
# GROUP BY StationName
# 
# JOIN sensors 
# 
# ON readings.StationName = sensors.StationName
# 

# In[25]:


# write the equivalent SQL operation using pandas functions and display the resulting dataframe
display(Image(filename='src/ex3.png'))


# # Discuss the following
# Now say we wanted to add an additional column to describe the status of a reading for a given sensor:
# 
# A sensor's reading can be assigned one of the following tags: {Fluctuating, Consistent}.
# 
# ## Why would the following strategy be faulty?
# 
# Add one additional column to the dataframe, assigning either {1, or 2} to each record to represent {Fluctuating, Consistent} for the given reading.
#  
# Answer: assigning either Fluctuating or Consistent may be a problem since the data may tend to be overfitted and therefore not a true reflection of the data. Also, the setting of the tags are categorical variables and may not be compatible with some machine learning models unless they are changed to integers or numeric variables. 
# 
# 

# # One-hot encoding
# The correct procedure to follow, is to one-hot encode the status of a sensor.
# 
# Write code in the cell below to add the status of a reading according to the following restraints:
# 
# If 'RoadSurfaceTemperature' and 'AirTemperature' differs with a value greater than 1°C, then assign it the tag of 'Fluctuating', otherwise 'Consistent' through one hot encoding.
# 
# Once again only use the measurements that took place on 2019-09-17 between 14:00 and 15:00 after excluding null values. 
# 
# Display the first 30 entries of the dataframe afterwards

# 

# In[ ]:


# insert code here
if readings['RoadSurfaceTemperature'] - readings['AirTemperature'] >= 1:
    
    


# # Text preprocessing
# Finally we will be looking at an example of text preprocessing for natural language processing. Before text can be parsed to a model it must first be normalised. This mean that all punctuation must be removed, all characters must be lowercase and any whitespacing removed. 
# 
# Below there are three functions that must be completed. Each funtions takes in the words in the corpus one by one and formats as required.
# 
# ## Function to_lowercase(word): 
# In the first function any uppercase letters must be converted into lowercase.
# 
# ## Function remove_punctuation(word): 
# The second function removes any punctuation from the word. There are many ways to achieve this. Refrain from using any imported libraries. If the entirety of the word is punctuation, simply return an empty string.
# 
# ## Function remove_newline(word): 
# The final functions checks for any newline characters ('\n') in a given word and removes it. If the word is only made up of a newline character, simply return an empty string.
# 
# 

# In[33]:


# Functions
def to_lowercase(word):
    # insert code here
    word.lower()
    return word

def remove_punctuation(word):
    # insert code here
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in word:
        if ele in punc:
            word = word.replace(ele, "")
            return(word)

def remove_newline(word):
    

# Read file
corpus = open('src/corpus.txt', 'r', encoding="utf8")
words = []

# Tokenize words
for line in corpus:
    for word in line.split(' '):
        
        #preprocess words
        word = to_lowercase(word)
        word = remove_punctuation(word)
        word = remove_newline(word)
        
        if word != '':
            words.append(word)

# Display words
print(words)
corpus.close()


# # Counting the frequencies of words
# After the text has been preprocessed, the next step would be counting the frequencies of n-grams. In this case we are only looking at unigrams (i.e. the frequencies of the words themselves).
# 
# Write code below to count the frequencies and store them in a dictionary. 
# 
# 
# The key of the dictionary being the word itself with the corresponding value the frequency.
# 
# Thereafter display the word with the highest frequencies count.

# In[ ]:


frequencies = {}

# insert code here

print(frequencies)


# In[ ]:


# display the word with the highest frequency

