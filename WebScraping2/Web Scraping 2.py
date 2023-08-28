#!/usr/bin/env python
# coding: utf-8

# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# #This task will be done in following steps:
# #1. First get the webpage https://www.shine.com/
# #2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# #3. Then click the searchbutton.
# #4. Then scrape the data for the first 10 jobs results you get.
# #5. Finally create a dataframe of the scraped data.

# In[15]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

driver=webdriver.Chrome()

driver.get("https://www.shine.com/")

search_btn=driver.find_element(By.XPATH, "/html/body/div[1]/header[1]/div[3]/div/div/div[1]/div/span/i")
search_btn.click()


# In[34]:


#Solution using BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.shine.com/job-search/data-analyst-jobs-in-bangalore?q=Data%20Analyst&loc=Bangalore'
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

job_title= [i.text for i in soup.find_all('h2', itemprop="name")]

job_location=[i.text for i in soup.find_all('div', class_="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2")]

company_name=[i.text for i in soup.find_all('div', class_="jobCard_jobCard_cName__mYnow")]


exp_reqd=[j.text.split(' Yr')[0] for j in soup.find_all('div', class_="jobCard_jobCard_lists__fdnsc")]
#print(len(exp_reqd))

#print(len(job_title), len(job_location), len(company_name), len(exp_reqd))
Job_details=pd.DataFrame({'Job Title': job_title, "Loaction":job_location, "Company Name":company_name, 'Experience Required':exp_reqd}, index=range(1,21))[0:10]
Job_details


# In[16]:


job_title=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
job_title.send_keys('Data Analyst')


# In[18]:


location=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')

search=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[59]:


job_title=[]
location=[]
company_name=[]
exp_reqd=[]

job_title=[i.text for i in driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')]
#job_title

location=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')]
#location

company_name=[i.text for i in driver.find_elements(By.CLASS_NAME, 'jobCard_jobCard_cName__mYnow')]
#company_names=[x.upper() for x in company_name]

exp_reqd=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')]
#exp_reqd

Job_Details=pd.DataFrame({"Job Title": job_title, "Location":location, "Company Name":company_names, "Experience Required":exp_reqd})[0:10]
Job_Details


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.This task will be done in following steps:
# #1. First get the webpage https://www.shine.com/
# #2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# #3. Then click the search button.
# #4. Then scrape the data for the first 10 jobs results you get.
# #5. Finally create a dataframe of the scraped data.
# 

# In[33]:


import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings

driver=webdriver.Chrome()
driver.get('https://www.shine.com/')


# In[34]:


search_btn=driver.find_element(By.CLASS_NAME, "iconH-zoom-white")
search_btn.click()


# In[36]:


job_title=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
job_title.send_keys('Data Scientist')


# In[37]:


location=driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys("Bangalore")

search=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[43]:


title=[i.text for i in driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')]
title

location=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')]
location

company=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')]
company

experience=[i.text.split(' Yr')[0] for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')]
experience

Job_Details=pd.DataFrame({"Job Title": title, "Location":location, "Company Name":company, 'Experience Required': experience}, index=range(1,21))[0:10]
Job_Details


# In[ ]:




