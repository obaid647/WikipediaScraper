"""
-------------------------------------------------------
Top Canada Companies
-------------------------------------------------------
Author:  Obaid Khan
Email:   obaid.khan1450@gmail.com
-------------------------------------------------------
"""
#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

def TopCA():

    #get website
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_Canada"
    page = requests.get(url)

    #extract html code
    soup = BeautifulSoup(page.text, features="lxml")

    #get table from code
    table = soup.find_all('table')[0]

    #get titles of table
    htmlTitles = table.find_all("th")
    columnTitles = [title.text.strip() for title in htmlTitles]

    #get data of the table
    tableData = table.find_all("tr")

    #initialize data frame
    df = pd.DataFrame(columns = columnTitles)

    #append each row in df
    for row in tableData[1:]:
        raw = row.find_all("td")
        companyData = [data.text.strip() for data in raw]
        
        #add to df
        length = len(df)
        df.loc[length] = companyData
    
    return df
