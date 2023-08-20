#!/usr/bin/env python
# coding: utf-8

# # Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url= "https://en.wikipedia.org/wiki/Main_Page"
r= requests.get(url)
soup=BeautifulSoup(r.text, "html.parser")
header= soup.find_all(['h1', "h2"])
#print(header)
list =[]
for i in header:
    list.append(i.text)

df=pd.DataFrame(list, index=range(1,11))
print(df)


# # Question 3 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# #a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# #b) Top 10 ODI Batsmen along with the records of their team andrating.
# #c) Top 10 ODI bowlers along with the records of their team andrating.
# 

# In[15]:


#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

table1=soup.find('table', class_='table')
#table1
header=[]
for i in table1.find_all('th'):
    header.append(i.text)
    header =[item.strip('\n') for item in header]
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
print((mydata, )[0:11])
     


# In[46]:


#Another solution for the same problem

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

team=[]
for i in soup.find_all('span', class_="u-hide-phablet"):
    team.append(i.text)
#print(team)

matches=[]
match1=soup.find("td", class_='rankings-block__banner--matches')
#print(match1.text)
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
    matches.append(i.text)

finalmatches = []
finalpoints=[]
count = 0
for i in matches:
    if count % 2 == 1:
        finalpoints.append(i)
        count += 1
    else:
        finalmatches.append(i)
        count+=1
#print(finalpoints)
#print(finalmatches)
finalmatches.insert(0,match1.text)

points=[]
point1=soup.find("td", class_='rankings-block__banner--points')
#print(point1.text)
finalpoints.insert(0,point1.text)

ratings=[]
rating1=soup.find("td", class_="rankings-block__banner--rating u-text-right")
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
ratings.insert(0, rating1.text)
ratings=[item.strip('\n') for item in ratings]
#print(ratings)

final_data=pd.DataFrame({'Team':team, "Matches":finalmatches, 'Points':finalpoints, "Ratings":ratings})
final_data[0:10]


# In[3]:


#b) Top 10 ODI Batsmen along with the records of their team andrating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting?at="
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

table1=soup.find('table', class_="table rankings-table")
#table1
header=[]
for i in table1.find_all('th'):
    header.append(i.text)
    header =[item.strip('\n') for item in header]
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
print(mydata)


# In[56]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting?at="
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

batsman=[]
batsman1=soup.find('div', class_="rankings-block__banner--name-large")
for i in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    batsman.append(i.text)
    
batsman.insert(0, batsman1.text) 
#print(batsman)

team=[]
team1=soup.find('div', class_="rankings-block__banner--nationality")
#print(team1.text)
for i in soup.find_all('span', class_="table-body__logo-text"):
    team.append(i.text)
    
#team.insert(0, team1.text) 
#print(team)
#rating

table1=soup.find('table', class_="table rankings-table")
#table1
header=[]
for i in table1.find_all('th'):
    header.append(i.text)
    header =[item.strip('\n') for item in header]
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
#print(mydata)


# In[4]:


#c) Top 10 ODI bowlers along with the records of their team and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

table1=soup.find('table', class_="table rankings-table")
#table1
header=[]
for i in table1.find_all('th'):
    header.append(i.text)
    header =[item.strip('\n') for item in header]
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
print(mydata)


# # Question 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# #a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# #b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# #c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[5]:


#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print (soup)

table1=soup.find('table', class_='table')
#table1

header=[]
for i in table1.find_all("th"):
    header.append(i.text)
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
    

for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row

print(mydata) 


# In[6]:


#b) Top 10 women’s ODI Batting players along with the records of their team and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')

table1=soup.find('table', class_='table rankings-table')
#table1

header=[]
for i in table1.find_all('tr'):
    for j in i.find_all('th'):
        header.append(j.text)
#print(header)

mydata=pd.DataFrame(columns=header)
#mydata

for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
print(mydata)


# In[7]:


#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

table1=soup.find('table', class_="table rankings-table")
#table1
header=[]
for i in table1.find_all('th'):
    header.append(i.text)
    header =[item.strip('\n') for item in header]
#print(header)
mydata=pd.DataFrame(columns=header)
#mydata
for j in table1.find_all('tr')[1:11]:
    row_data=j.find_all('td')
    row=[a.text for a in row_data]
    row=[item.strip('\n') for item in row]
    #print(row)
    l=len(mydata)
    mydata.loc[l]= row
print(mydata)


# # 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
# make data frame
# #i) Headline
# #ii) Time
# #iii) News Link

# In[85]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.cnbc.com/world/?region=world"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)

headings=[]
for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    headings.append(i.text)
#print(headings)

time=[]
for i in soup.find_all('time', class_="LatestNews-timestamp"):
    time.append(i.text)
#print(time)

links=[]
for i in soup.find('div', class_='LatestNews-isHomePage LatestNews-isIntlHomepage'):                 
    for link in i.find_all('a', class_="LatestNews-headline"):
        links.append(link.get('href'))
#print(links)

#print(len(headings), len(time), len(links))

df=pd.DataFrame({'Headings': headings, "Time":time, 'Links':links}, index=range(1,31))
df


# # Question6 Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data frame
# #i) Paper Title
# #ii) Authors
# #iii) Published Date
# #iv) Paper URL
# 

# In[104]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')

paper_title=[]
for i in soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
#print(paper_title)

authors=[]
for i in soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
#print(authors)


published_date=[]
for i in soup.find_all('span', class_="sc-1thf9ly-2 dvggWt"):
    published_date.append(i.text)
#print(published_date)

paper_url=[]
for i in soup.find_all('a', class_="sc-5smygv-0 fIXTHm"):
    paper_url.append(i.get('href'))
#print(paper_url)

print(len(paper_title), len(authors), len(published_date), len(paper_url))
most_downloaded_articles=pd.DataFrame({'Paper Title':paper_title, "Author":authors, "Published Date":published_date, "Paper Link":paper_url}, index=range(1,25))
print (most_downloaded_articles)


# In[105]:


#Question7) Write a python program to scrape mentioned details from dineout.co.inand make data frame
#i) Restaurant name
#ii) Cuisine
#iii) Location
#iv) Ratings
#v) Image URL


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.dineout.co.in/jaipur-restaurants"
r=requests.get(url)
soup=BeautifulSoup(r.content)

r_name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    r_name.append(i.text)
#print(r_name)

cost_and_cuisine=[]
for i in soup.find_all('div',class_="detail-info"):
    cost_and_cuisine.append(i.text.replace('₹',''))
#print(cost_and_cuisine)

location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
#print(location)

images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
#print(images)

#print(len(r_name), len(cost_and_cuisine), len(location), len(images))

restaurant_data=pd.DataFrame({"Restaurant Name":r_name, "Location": location, "Cost & Cuisine": cost_and_cuisine, "Links":images}, index=range(1,22))
print(restaurant_data)


# In[ ]:





# In[ ]:




