import numpy as np
import pandas as pd
import re
import gender_guesser.detector as gender
import matplotlib.pyplot as plt

df=pd.read_csv('ccmovies.csv')
df.head()

#Clean up the dataset
df = df.drop(df[df.TITLE.str.contains('(?i)box set')].index)  
df['YEAR'] = df['YEAR'].astype(str)  
df.dropna(subset=['FILMMAKER'], inplace=True) 

#Look at most represented filmmakers
top_filmmakers=df.FILMMAKER.value_counts()  
top_filmmakers.head()  

#Plot filmmakers most represented in Collection
top_filmmakers = df.FILMMAKER.value_counts().reset_index().rename(columns={'index': 'FILMMAKER_NAME'})   
filmmaker_number = (top_filmmakers['FILMMAKER_NAME'][0], top_filmmakers['FILMMAKER_NAME'][1], top_filmmakers['FILMMAKER_NAME'][2], top_filmmakers['FILMMAKER_NAME'][3], top_filmmakers['FILMMAKER_NAME'][4], top_filmmakers['FILMMAKER_NAME'][5], top_filmmakers['FILMMAKER_NAME'][6], top_filmmakers['FILMMAKER_NAME'][7], top_filmmakers['FILMMAKER_NAME'][8], top_filmmakers['FILMMAKER_NAME'][9])
y_pos = np.arange(len(filmmaker_number))
number_of_films = [top_filmmakers['FILMMAKER'][0], top_filmmakers['FILMMAKER'][1], top_filmmakers['FILMMAKER'][2], top_filmmakers['FILMMAKER'][3], top_filmmakers['FILMMAKER'][4], top_filmmakers['FILMMAKER'][5], top_filmmakers['FILMMAKER'][6], top_filmmakers['FILMMAKER'][7], top_filmmakers['FILMMAKER'][8], top_filmmakers['FILMMAKER'][9]]
 
plt.barh(y_pos, number_of_films, align='center')
plt.yticks(y_pos, filmmaker_number)
plt.xlabel('Number of films in Criterion Collection')
plt.ylabel('Filmmaker')
plt.title('Filmmakers most represented in Criterion Collection')
 
plt.show()

#Look at most represented countries
top_countries=df.COUNTRY.value_counts()  
top_countries.head()  

#Plot most represented countries
top_countries = df.COUNTRY.value_counts().reset_index().rename(columns={'index': 'COUNTRY_NAME'})    
countryname = (top_countries['COUNTRY_NAME'][0], top_countries['COUNTRY_NAME'][1], top_countries['COUNTRY_NAME'][2], top_countries['COUNTRY_NAME'][3], top_countries['COUNTRY_NAME'][4], top_countries['COUNTRY_NAME'][5], top_countries['COUNTRY_NAME'][6], top_countries['COUNTRY_NAME'][7], top_countries['COUNTRY_NAME'][8], top_countries['COUNTRY_NAME'][9])
y_pos = np.arange(len(filmmaker_number))
number_of_films_percountry = [top_countries['COUNTRY'][0], top_countries['COUNTRY'][1], top_countries['COUNTRY'][2], top_countries['COUNTRY'][3], top_countries['COUNTRY'][4], top_countries['COUNTRY'][5], top_countries['COUNTRY'][6], top_countries['COUNTRY'][7], top_countries['COUNTRY'][8], top_countries['COUNTRY'][9]]
 
plt.barh(y_pos, number_of_films, align='center')
plt.yticks(y_pos, countryname)
plt.xlabel('Number of films in Criterion Collection')
plt.ylabel('Country')
plt.title('Countries most represented in Criterion Collection')
 
plt.show()

#Look at how many films are in the Collection from each decade
#remove all eclipse series (case insensitive) because they are compilations from different years
df = df.drop(df[df.TITLE.str.contains('(?i)eclipse series')].index)  

df1900s = df.loc[(df.YEAR.str.contains('190[0-9]'))]  
total_1900s = len(df1900s.index) 
df1910s = df.loc[(df.YEAR.str.contains('191[0-9]'))]
total_1910s = len(df1910s.index) 
df1920s = df.loc[(df.YEAR.str.contains('192[0-9]'))] 
total_1920s = len(df1920s.index) 
df1930s = df.loc[(df.YEAR.str.contains('193[0-9]'))] 
total_1930s = len(df1930s.index)
df1940s = df.loc[(df.YEAR.str.contains('194[0-9]'))]
total_1940s = len(df1940s.index)
df1950s = df.loc[(df.YEAR.str.contains('195[0-9]'))] 
total_1950s = len(df1950s.index) 
df1960s = df.loc[(df.YEAR.str.contains('196[0-9]'))]
total_1960s = len(df1960s.index) 
df1970s = df.loc[(df.YEAR.str.contains('197[0-9]'))] 
total_1970s = len(df1970s.index) 
df1980s = df.loc[(df.YEAR.str.contains('198[0-9]'))]
total_1980s = len(df1980s.index) 
df1990s = df.loc[(df.YEAR.str.contains('199[0-9]'))]
total_1990s = len(df1990s.index) 
df2000s = df.loc[(df.YEAR.str.contains('200[0-9]'))] 
total_2000s = len(df2000s.index) 
df2010s = df.loc[(df.YEAR.str.contains('201[0-9]'))] 
total_2010s = len(df2010s.index) 


#Plot films per decade
decades = ('1900s', '1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s')
y_pos = np.arange(len(decades))
number_of_films = [total_1900s, total_1920s, total_1930s, total_1940s, total_1950s, total_1960s, total_1970s, total_1980s, total_1990s, total_2000s, total_2010s]
 
plt.barh(y_pos, number_of_films, align='center')
plt.barh(y_pos, number_of_films, align='center', alpha=0.5)
plt.yticks(y_pos, decades)
plt.xlabel('Number of films in Criterion Collection')
plt.ylabel('Decade')
plt.title('Films Per Decade')
 
plt.show()

#Look at gender representation in the Collection
d = gender.Detector()

df2 = df['FILMMAKER'].str.split(' ', 1, expand=True)    

#creates a list to store gender values
filmmakergender = [] 

#assigns each first name a gender and adds it to the filmmakergender list
for index, row in df2.iterrows(): 
	filmmakergender.append(d.get_gender((row[0])))    
#adds the filmmaker gender list to the original dataframe as a column titled FILMMAKERGENDER
df['FILMMAKERGENDER'] = filmmakergender     
	
#counts the values for male, female, etc.
gender_breakdown=df.FILMMAKERGENDER.value_counts() 
gender_breakdown 

#Plot gender representation in Collection
gender_breakdown = df.FILMMAKERGENDER.value_counts().reset_index().rename(columns={'index': 'gender'}) 

#remove all rows that aren't 'male' or 'female' (this could be done more simply....)
gender_breakdown = gender_breakdown.drop(gender_breakdown[gender_breakdown.gender.str.contains('mostly_male')].index) 
gender_breakdown = gender_breakdown.drop(gender_breakdown[gender_breakdown.gender.str.contains('mostly_female')].index) 
gender_breakdown = gender_breakdown.drop(gender_breakdown[gender_breakdown.gender.str.contains('unknown')].index) 
gender_breakdown = gender_breakdown.drop(gender_breakdown[gender_breakdown.gender.str.contains('andy')].index) 

gender = (gender_breakdown['gender'][0], gender_breakdown['gender'][3])
y_pos = np.arange(len(gender))
gender_representation = [gender_breakdown['FILMMAKERGENDER'][0], gender_breakdown['FILMMAKERGENDER'][3]]
 
plt.barh(y_pos, gender_representation, align='center')
plt.yticks(y_pos, gender)
plt.xlabel('Number of Films in Criterion Collection')
plt.ylabel('Gender')
plt.title('Gender Representaton in Criterion Collection')
plt.show()
	





 


