import pandas  as pd
import requests  



#Step 1 Data Collection


url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
req = requests.get(url)

data_list = pd.read_html(req.text)

target_df = data_list[5]


#Step 2 Data Cleaning

#Renaming column Names

target_df.columns = ['','Country','Total Cases','Total Deaths','Total Recoveries', 'Col5']

#Removing extra columns

target_df = target_df[['Country','Total Cases','Total Deaths','Total Recoveries']]


#Removing Empty rows
# As there were empty rows in the dataframe at the end 

last_index = target_df.index[-1]

target_df = target_df.drop([0,1,last_index, last_index - 1])

# Removing inconsistencies within the country name

target_df['Country'] = target_df['Country'].str.replace('\[.*\]','')

#Removing No data and replacing it with 0

for i in range(len(target_df.columns)):
    target_df.iloc[:,i] = target_df.iloc[:,i].str.replace('No data','0')


#Updating Total Cases, Total Deaths and Total Recoveries Column Type to integer    
    
for i in range(len(target_df.columns) - 1):
    target_df.iloc[:,i+1] = pd.to_numeric(target_df.iloc[:,i+1])
    

#Step 3 Data Export xls
    
target_df.to_excel(r'covid_19.xlsx')