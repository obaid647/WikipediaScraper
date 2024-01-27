"""
-------------------------------------------------------
Wikipedia Scraper
-------------------------------------------------------
Author:  Obaid Khan
Email:   obaid.khan1450@gmail.com
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
#imports
from bs4 import BeautifulSoup
import requests

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
rowData = []

#append each row in list
for row in tableData[1:]:
    raw = row.find_all("td")
    companyData = [data.text.strip() for data in raw]
    rowData.append(companyData)

#print titles
print(columnTitles[0] + " | ", end="")
print(columnTitles[1][:10] + " Rank | ", end="")
print(columnTitles[2] + "                        | ", end="")
print(columnTitles[3] + "         | ", end="")
print(columnTitles[4] + " | ", end="")
print(columnTitles[5] + " | ", end="")
print(columnTitles[6] + " | ", end="")
print(columnTitles[7] + " | ", end="")
print("")
print("-----------------------------------------------------------------------------------------------------------------------------"
      + "-----------------------")

#iterate rows and print
for i in range(len(rowData)):
    print("{:4} | ".format(rowData[i][0]), end="")
    print("{:15} | ".format(rowData[i][1]), end="")
    print("{:27} | ".format(rowData[i][2]), end="")
    print("{:16} | ".format(rowData[i][3]), end="")
    print("{:21} | ".format(rowData[i][4]), end="")
    print("{:21} | ".format(rowData[i][5]), end="")
    print("{:9} | ".format(rowData[i][6]), end="")
    print("{:12} | ".format(rowData[i][7]), end="")
    print("")
