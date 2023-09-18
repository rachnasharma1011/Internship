#!/usr/bin/env python
# coding: utf-8

# # 1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: A ) Rank B) Name C) Artist D) Upload date E) Views 

# In[1]:


import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver=webdriver.Chrome()


# In[3]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[4]:


driver.maximize_window()


# In[6]:


container=driver.find_element(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]')
container.text


# In[15]:


ranks=[]
rank=container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[1]')[0:30]
for i in rank:
    ranks.append(i.text)


# In[16]:


ranks


# In[17]:


rank=[i.text for i in container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[1]')][0:30]
rank


# In[19]:


name=[i.text.split('[')[0] for i in container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]')][0:30]
name


# In[20]:


artist=[i.text for i in container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')][0:30]
artist


# In[24]:


views=[i.text for i in container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')][0:30]
views


# In[23]:


pub_date=[i.text for i in container.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')][0:30]
pub_date


# In[25]:


print(len(rank), len(name), len(artist), len(views), len(pub_date))


# In[26]:


import pandas as pd


# In[30]:


Youtube_videos=pd.DataFrame({'Rank':rank, "Name":name, "Artist":artist, "Views":views, "Upload Date":pub_date}, index=range(1,31))
Youtube_videos


# # 2. Scrape the details team India’s international fixtures from bcci.tv.
# #Url = https://www.bcci.tv/.
# #You need to find following details:
# #A) Match title (I.e. 1 ODI)
# #B) Series
# #C) Place
# #D) Date
# #E) Time
# #Note: - From bcci.tv home page you have reach to the international fixture page through code. 

# In[59]:


driver=webdriver.Chrome()


# In[60]:


driver.get('https://www.bcci.tv/.')


# In[61]:


driver.maximize_window()


# In[62]:


select=driver.find_element(By.XPATH, '/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
select.click()


# In[63]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


# In[64]:


#Click on accept cookies and click on more button to load more details
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="cookie__accept btn btn-primary"]'))).click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@ng-click="viewMoreMatches()" and contains(.,"More Fixtures")]')))
while True:
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@ng-click="viewMoreMatches()" and contains(.,"More Fixtures")]'))).click()
        print('More button Clicked')
    except TimeoutException:
        break
    except ElementClickInterceptedException as ec:
        print('Error ',ec)


# In[82]:


series=[i.text for i in driver.find_elements(By.XPATH, '//h5[@class="match-tournament-name ng-binding"]')]
series


# In[66]:


len(series)


# In[68]:


match_title=[i.text.split('-')[0] for i in driver.find_elements(By.XPATH, '//div[@class="match-place ng-scope"]')]
match_title


# In[69]:


location=[i.text.split('-')[1] for i in driver.find_elements(By.XPATH, '//div[@class="match-place ng-scope"]')]
location


# In[70]:


len(match_title)


# In[71]:


len(location)


# In[74]:


date=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="match-dates ng-binding"]')]
date


# In[76]:


len(date)


# In[77]:


time=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="match-time no-margin ng-binding"]')]
time


# In[78]:


len(time)


# In[83]:


Match_details=pd.DataFrame({"Match Title": match_title, "Series":series, "Place":location, "Date":date, "Time":time}, index=range(1, 40))
Match_details


# # 3. Scrape the details of State-wise GDP of India from statisticstime.com.
# #Url = http://statisticstimes.com/
# #You have to find following details: A) Rank B) State C) GSDP(18-19)- at current prices D) GSDP(19-20)- at current prices E) Share(18-19) F) GDP($ billion)
# #Note: - From statisticstimes home page you have to reach to economy page through code. 

# In[93]:


driver=webdriver.Chrome()


# In[94]:


driver.get('http://statisticstimes.com/')


# In[95]:


driver.maximize_window()


# In[96]:


select_economy=driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/button')
select_economy.click()


# In[99]:


#Try later
#select_India=driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')

#i=0
#while i<len(select_India):
#    if(select_India[i].text=='India'):
#       select_India[i].click
#    i+=1


# In[101]:


select=driver.find_element(By.LINK_TEXT, "India")
select.click()


# In[102]:


indian_statesgdp=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
indian_statesgdp.click()


# In[104]:


table=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]')][0]
table


# In[149]:


rank1=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[1]')][0:33]
rank1


# In[114]:


state=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[2]')][0:33]
state


# In[115]:


gsdp_19_20=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[3]')][0:33]
gsdp_19_20


# In[116]:


gsdp_18_19=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[4]')][0:33]
gsdp_18_19


# In[117]:


share_18_19=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[5]')][0:33]
share_18_19


# In[118]:


gdp=[i.text for i in driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[6]')][0:33]
gdp


# In[147]:


#Another method
ranks=[]
table=driver.find_elements(By.XPATH, '//table[@class="display dataTable"]')
for i in table:
    r=i.find_elements(By.XPATH, '//td[@class="data1"]')[0:33]

for rank in r:
    ranks.append(rank.text)
ranks    


# In[150]:


Statewise_GDP=pd.DataFrame({"Rank":rank1, "State":state, "GSDP(18-19)- at current prices":gsdp_18_19, "GSDP(19-20)- at current prices":gsdp_19_20, "Share(18-19)":share_18_19, "GDP($ billion)":gdp}, index=range(1, 34))
Statewise_GDP


# # 4. Scrape the details of trending repositories on Github.com. Url = https://github.com/ You have to find the following details: A) Repository title B) Repository description C) Contributors count D) Language used Note: - From the home page you have to click on the trending option from Explore menu through code. 

# In[155]:


driver=webdriver.Chrome()


# In[156]:


driver.get('https://github.com/')


# In[157]:


driver.maximize_window()


# In[166]:


open_btn=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
open_btn.click()


# In[167]:


trending=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a")
trending.click()


# In[168]:


rep_title=[i.text for i in driver.find_elements(By.XPATH, '//a[@class="Link"]')]
rep_title


# In[171]:


len(rep_title)


# In[169]:


rep_des=[i.text for i in driver.find_elements(By.XPATH, '//p[@class="col-9 color-fg-muted my-1 pr-4"]')]
rep_des


# In[172]:


len(rep_des)


# In[177]:


con_count=[i.text for i in driver.find_elements(By.XPATH, '//a[@class="Link Link--muted d-inline-block mr-3"]')][1::2]
con_count


# In[179]:


stars=[i.text for i in driver.find_elements(By.XPATH, '//a[@class="Link Link--muted d-inline-block mr-3"]')][::2]
stars


# In[181]:


len(stars), len(con_count)


# In[216]:


language=[]
containers=driver.find_elements(By.XPATH, '//div[@class="f6 color-fg-muted mt-2"]')
for i in containers:
    try:
        lang=i.find_element(By.XPATH, './/span[@itemprop="programmingLanguage"]')
        language.append(lang.text)
    except:
        language.append('-')   


# In[217]:


language


# In[218]:


len(language)


# In[220]:


Github_details=pd.DataFrame({"Repository title":rep_title, "Repository description":rep_des, "Contributors count":con_count, "Stars":stars, "Language used":language}, index=range(1,26))
Github_details


# # 5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/ You have to find the following details: A) Song name B) Artist name C) Last week rank D) Peak rank E) Weeks on board Note: - From the home page you have to click on the charts option then hot 100-page link through code.

# In[3]:


driver=webdriver.Chrome()


# In[3]:


driver.get('https:/www.billboard.com/')


# In[4]:


driver.maximize_window()


# In[5]:


chart_select=driver.find_element(By.XPATH, '/html/body/div[3]/header/div/div[2]/div/div/div[2]/div[2]/div/div/nav/ul/li[1]/a')
chart_select.click()


# In[10]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException


# In[12]:


try :
    hot_100=driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]/a')
    hot_100.click()
except NoSuchElementException:
    hot_100=driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]')
    hot_100.click()
    


# In[14]:


pop_up=driver.find_element(By.XPATH, '/html/body/div[2]/div/span')
pop_up.click()


# In[32]:


song1=driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[2]/ul/li[4]/ul/li[1]/h3')
s1=[song1.text]
s1


# In[17]:


songs=[i.text for i in driver.find_elements(By.XPATH, '//h3[@class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"]')]
songs


# In[33]:


song_name=s1+songs
song_name


# In[29]:


len(song_name)


# In[34]:


artist1=driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[2]/ul/li[4]/ul/li[1]/span').text
artist1


# In[35]:


artists=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"]')]
artists


# In[37]:


artist_names=[artist1]+artists
artist_names


# In[38]:


len(artist_names)


# In[42]:


details=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet"]')]
details


# In[45]:


lastwk_rank1=details[0]
peak_rank1=details[1]
weeks_on_board1=details[2]
print(lastwk_rank1, peak_rank1, weeks_on_board1)


# In[46]:


ranks=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')][:594:6]
ranks


# In[48]:


lastwk_rank=[lastwk_rank1]+ranks
lastwk_rank


# In[49]:


len(lastwk_rank)


# In[50]:


peak_ranks=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')][1:594:6]
peak_ranks


# In[51]:


peak_rank=[peak_rank1]+peak_ranks
peak_rank


# In[52]:


len(peak_rank)


# In[53]:


weeks_on_board2=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')][2:594:6]
weeks_on_board2


# In[54]:


weeks_on_board=[weeks_on_board1]+weeks_on_board2
weeks_on_board


# In[55]:


len(weeks_on_board)


# In[56]:


import pandas as pd


# In[57]:


top_100_songs=pd.DataFrame({"Song Name":song_name, 'Artist Name':artist_names, "Last Week Rank":lastwk_rank, "Peak Rank":peak_rank, "Weeks On Board":weeks_on_board }, index=range(1, 101))
top_100_songs


# # 6. Url = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey. You have to find the following details:
# #Scrape the details of Highest selling novels.
# #compare A) Book name B) Author name C) Volumes sold D) Publisher E) Genre 

# In[9]:


driver=webdriver.Chrome()


# In[10]:


driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[11]:


driver.maximize_window()


# In[12]:


name=[i.text for i in driver.find_elements(By.XPATH, '//td[@class="left"]')][1::5]
name


# In[13]:


len(name)


# In[14]:


author_name=[i.text for i in driver.find_elements(By.XPATH, '//td[@class="left"]')][2::5]
author_name


# In[15]:


len(author_name)


# In[16]:


vol_sold=[i.text for i in driver.find_elements(By.XPATH, '//td[@class="left"]')][3::5]
vol_sold


# In[17]:


len(vol_sold)


# In[18]:


publisher=[i.text for i in driver.find_elements(By.XPATH, '//td[@class="left"]')][4::5]
publisher


# In[19]:


len(publisher)


# In[20]:


genre=[i.text for i in driver.find_elements(By.XPATH, '//td[@class="last left"]')]
genre


# In[21]:


len(genre)


# In[22]:


import pandas as pd


# In[24]:


best_selling_books=pd.DataFrame({"Book Name":name, "Author Name":author_name, "Volumes Sold":vol_sold, "Publisher":publisher, 'Genre':genre}, index=range(1,101))
best_selling_books


# # 7 Scrape the details most watched tv series of all time from imdb.com. Url = https://www.imdb.com/list/ls095964455/ You have to find the following details: A) Name B) Year span C) Genre D) Run time E) Ratings F) Votes 

# In[87]:


driver=webdriver.Chrome()


# In[88]:


driver.get('https://www.imdb.com/list/ls095964455/')


# In[89]:


driver.maximize_window()


# In[112]:


names=[i.text.split('.')[1].split('(')[0].strip(' ') for i in driver.find_elements(By.XPATH, '//h3[@class="lister-item-header"]')]
names


# In[99]:


len(name)


# In[101]:


year_span=[i.text.split('(')[1].strip(') ') for i in driver.find_elements(By.XPATH, '//h3[@class="lister-item-header"]')]
year_span


# In[102]:


len(year_span)


# In[103]:


genre=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="genre"]')]
genre


# In[104]:


len(genre)


# In[105]:


run_time=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="runtime"]')]
run_time


# In[106]:


len(run_time)


# In[110]:


rating=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="ipl-rating-star__rating"]')][::23]
votes=[i.text for i in driver.find_elements(By.XPATH, '//span[@name="nv"]')]
print(rating, votes)


# In[111]:


print(len(votes), len(rating))


# In[114]:


Details=pd.DataFrame({"Name":names, "Year Span":year_span, "Genre":genre, "Run Time":run_time, "Ratings":rating, "Votes":votes}, index=range(1, 101))
Details


# # 8. Details of Datasets from UCI machine learning repositories.
# Url = https://archive.ics.uci.edu/
# You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute G) Year
# Note: - from the home page you have to go to the Show All Dataset page through code. 
# 

# In[116]:


driver=webdriver.Chrome()


# In[117]:


driver.get('https://archive.ics.uci.edu/ ')


# In[118]:


driver.maximize_window()


# In[119]:


select_dataset=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
select_dataset.click()


# In[120]:


cookie=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[2]/button')
cookie.click()


# In[121]:


expand=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/div/label[2]/div[2]/span[2]')
expand.click()


# In[157]:


dataset_name=[i.text for i in driver.find_elements(By.XPATH, '//a[@class="link-hover link text-xl font-semibold"]')]
dataset_name


# In[176]:


task=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="truncate"]')][::8]

for i in range(len(task)):
    if task[i]=='':
        task[i]="-"
        
task


# In[171]:


data_type=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="truncate"]')][1::8]

for i in range(len(data_type)):
    if data_type[i]=='':
        data_type[i]="-"
data_type


# In[175]:


no_of_instances=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="truncate"]')][2::8]

for i in range(len(no_of_instances)):
    if no_of_instances[i]=='':
        no_of_instances[i]="-"
        
no_of_instances


# In[126]:


no_of_features=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="truncate"]')][3::8]
no_of_features


# In[129]:


attribute_type=[i.text for i in driver.find_elements(By.XPATH, '//tbody[@class="border"]/tr/td[2]')]
attribute_type


# In[130]:


subject_area=[i.text for i in driver.find_elements(By.XPATH, '//tbody[@class="border"]/tr/td[1]')]
subject_area


# In[135]:


import re


# In[155]:


date=[i.text for i in driver.find_elements(By.XPATH, '//tbody[@class="border"]/tr/td[3]')]
date


# In[154]:


year=[]
yr=driver.find_elements(By.XPATH, '//tbody[@class="border"]/tr/td[3]')
for i in yr:
    if len(i.text.split('/'))==3:
        year.append(i.text.split('/')[2])
    else:
        year.append('N/A')

year


# In[160]:


print(len(dataset_name), len(year), len(subject_area), len(attribute_type), len(no_of_features), len(no_of_instances), len(data_type), len(task))


# In[177]:


Details=pd.DataFrame({"Dataset name":dataset_name, "Data Type":data_type, "Task":task, "Attribute Type":attribute_type, "No of Instances":no_of_instances, "No of Attribute":no_of_features , "Year":year }, index=range(1, 11))
Details


# In[ ]:




