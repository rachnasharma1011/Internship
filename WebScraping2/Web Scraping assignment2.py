#!/usr/bin/env python
# coding: utf-8

# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# #This task will be done in following steps: #1. First get the webpage https://www.shine.com/ #2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field. #3. Then click the searchbutton. #4. Then scrape the data for the first 10 jobs results you get. #5. Finally create a dataframe of the scraped data.

# In[2]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

driver=webdriver.Chrome()
driver.get("https://www.shine.com/job-search/data-analyst-jobs-in-bangalore?q=Data%20Analyst&loc=Bangalore")

job_title=[]
location=[]
company_name=[]
exp_reqd=[]

job_title=[i.text for i in driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')]
#job_title

location=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')]
#location

company_name=[i.text for i in driver.find_elements(By.CLASS_NAME, 'jobCard_jobCard_cName__mYnow')]
company_names=[x.upper() for x in company_name]

exp_reqd=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')]
#exp_reqd

Job_Details=pd.DataFrame({"Job Title": job_title, "Location":location, "Company Name":company_names, "Experience Required":exp_reqd})[0:10]
Job_Details


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.This task will be done in following steps:
# #1. First get the webpage https://www.shine.com/ #2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field. #3. Then click the search button. #4. Then scrape the data for the first 10 jobs results you get. #5. Finally create a dataframe of the scraped data.

# In[3]:


import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings

driver=webdriver.Chrome()
driver.get('https://www.shine.com/job-search/data-scientist-jobs-in-bangalore?q=Data%20Scientist&loc=Bangalore')

title=[i.text for i in driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')]
#title

location=[i.text for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')]
#location

company=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')]
#company

experience=[i.text.split(' Yr')[0] for i in driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')]
#experience

Job_Details=pd.DataFrame({"Job Title": title, "Location":location, "Company Name":company, 'Experience Required': experience}, index=range(1,21))[0:10]
Job_Details


# In[ ]:




