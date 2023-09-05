#!/usr/bin/env python
# coding: utf-8

# # Q1 Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars. Extracting data from page 1

# In[1]:


import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver=webdriver.Chrome()
driver.get('https://www.amazon.in')


# In[3]:


input=input('Enter product name: ')


# In[4]:


search_input=driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search_input.send_keys(input)


# In[5]:


search_btn=driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_btn.click()


# # Q2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[6]:


all_brands=[]
start=0
end=3
for page in range(start, end):
    brand_name1=driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in brand_name1:
        all_brands.append(i.text.split(" ")[0])
    


# In[7]:


next_btn=driver.find_elements(By.CLASS_NAME, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')


# In[8]:


len(all_brands)


# In[9]:


all_brands


# In[10]:


all_pdt_names=[]
start=0
end=3
for page in range(start, end):
    product_name1=driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in product_name1:
        all_pdt_names.append(i.text)
    


# In[11]:


next_btn=driver.find_elements(By.CLASS_NAME, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')


# In[12]:


len(all_pdt_names)


# In[13]:


all_pdt_names


# In[14]:


all_pdt_prices=[]
start=0
end=3
for page in range(start, end):
    price1=driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
    for i in price1:
        all_pdt_prices.append(i.text)


# In[15]:


next_btn=driver.find_elements(By.CLASS_NAME, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')


# In[16]:


len(all_pdt_prices)


# In[17]:


all_pdt_prices


# In[18]:


all_pdt_del=[]
start=0
end=3
for page in range(start, end):
    del1=driver.find_elements(By.XPATH, '//span[@class="a-color-base a-text-bold"]')
    for i in del1:
        all_pdt_del.append(i.text)


# In[19]:


next_btn=driver.find_elements(By.CLASS_NAME, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')


# In[20]:


len(all_pdt_del)


# In[21]:


all_pdt_del


# In[22]:


all_pdt_url=[]
start=0
end=3
for page in range(start, end):
    url1=driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url1:
        all_pdt_url.append(i.get_attribute('href'))


# In[23]:


next_btn=driver.find_elements(By.CLASS_NAME, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')


# In[24]:


len(all_pdt_url)


# In[25]:


all_pdt_url


# In[26]:


from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


# In[27]:


pdt_availability=[]
for i in all_pdt_url:
    driver.get(i)
    try:
        availability=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[4]/div/div[1]/span')
        pdt_availability.append(availability.text)
    except NoSuchElementException:
        pdt_availability.append('No details')


# In[28]:


len(pdt_availability)


# In[29]:


pdt_availability


# In[30]:


import pandas as pd


# In[31]:


print(len(all_brands), len(all_pdt_names), len(all_pdt_prices), len(all_pdt_del), len(pdt_availability), len(all_pdt_url))


# In[32]:


Final_details=pd.DataFrame({"Brand Name":all_brands, "Name of the Product":all_pdt_names, "Price":all_pdt_prices, "Expected Delivery":all_pdt_del, "Availability":pdt_availability, "Product URL":all_pdt_url})
Final_details


# # Q3 Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,“Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[3]:


import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')


# In[4]:


driver=webdriver.Chrome()
driver.get('https://www.flipkart.com')


# In[5]:


login_pop=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
login_pop.click()


# In[6]:


input= driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
input.send_keys('redmi smartphone')


# In[7]:


from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


# In[8]:


try:
    search_btn=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button/svg')
    search_btn.click()
except NoSuchElementException:
    search_btn=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
    search_btn.click()


# In[10]:


smartphone_name=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')]


# In[11]:


len(smartphone_name)


# In[12]:


smartphone_name


# In[13]:


brand_name=[i.text.split(" ")[0] for i in driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')]


# In[14]:


brand_name


# In[15]:


for i in smartphone_name:
    price=[a.text for a in driver.find_elements(By.XPATH, '//div[@class="_30jeq3 _1_WHN1"]')]


# In[16]:


len(price)


# In[17]:


price


# In[19]:


import requests
from bs4 import BeautifulSoup


# In[54]:


soup=BeautifulSoup(driver.page_source, 'html.parser')


# In[55]:


for i in smartphone_name:
    info=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')]


# In[56]:


print(info)


# In[57]:


info1=driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')
RAM=[i.text.split('|')[0].split(" ")[0] for i in driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')]
print(RAM)


# In[25]:


len(RAM)


# In[24]:


import re


# In[27]:


info1=driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')
for i in info1:
    ROM=[i.text.split('GB')[1].split('|')[1] for i in driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')]
print(len(ROM))


# In[28]:


print(ROM)


# In[29]:


info1=driver.find_elements(By.XPATH, '//div[@class="fMghEO"]')
for i in info1:
    url=[i.get_attribute('href') for i in driver.find_elements(By.XPATH, '//a[@class="_1fQZEK"]')]
    print(url)


# In[31]:


color_name=[i.text.split('(')[1].split(',')[0] for i in driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')]
color_name


# In[33]:


len(color_name)


# In[84]:


soup=BeautifulSoup(driver.page_source, 'html.parser')


# In[85]:


info1=soup.find_all('div', class_="fMghEO")
RAM=[i.text.split('|')[0].split(" ")[0] for i in soup.find_all('div', class_="fMghEO")]
print(RAM)


# In[86]:


info1=soup.find_all('div', class_="fMghEO")
for i in info1:
    ROM=[i.text.split('GB')[1].split('|')[1] for i in soup.find_all('div', class_="fMghEO")]
print(len(ROM))


# In[87]:


print(ROM)


# In[88]:


info1=soup.find_all('div', class_="fMghEO")
for i in info1:
    url=[i.get_attribute('href') for i in driver.find_elements(By.XPATH, '//a[@class="_1fQZEK"]')]
    print(url)


# In[89]:


info=soup.find_all('div', class_='fMghEO')
print(info)


# In[102]:


for i in info:
    information=i.find_all('li', class_='rgWa7D')
    battery=information[3].text.split('mAh')[0]
    print(battery)


# In[91]:


for i in info:
    information=i.find_all('li', class_='rgWa7D')
    camera=information[2].text.split('|')
    try:
        prim_cam=camera[0]
        sec_cam=camera[1]
    except:
        sec_cam=0
    print(prim_cam, sec_cam)


# In[92]:


for i in info:
    information=i.find_all('li', class_='rgWa7D')
    space=information[0].text
    RAM1=space.split('|')[0].strip(' RAM')
    ROM1=space.split('|')[1].strip(' ROM')
    print(RAM1, ROM1)


# In[93]:


for i in info:
    information=i.find_all('li', class_='rgWa7D')
    display_size=information[1].text.split(' (')[0]
    print(display_size)


# In[98]:


import pandas as pd


# In[105]:


Phone_details=pd.DataFrame({"Brand":brand_name, "Smartphone Name":smartphone_name, "Color":color_name, "RAM":RAM1, 'ROM':ROM1, 'Primary Camera':prim_cam, "Secondary Camera":sec_cam, 'Display Size':display_size, 'Battery Capacity':battery, "Price":price, 'Product URL':url})


# In[106]:


Phone_details


# In[107]:


Phone_details.to_csv(r'C:\Users\asus 1\Desktop\Flipkart_Phone_Details.csv')


# # 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[108]:


import selenium
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup


# In[109]:


driver=webdriver.Chrome()


# In[110]:


driver.get('https://www.google.com/maps')


# In[111]:


search_icon=driver.find_element(By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input")
search_icon.send_keys('jabalpur')

search_btn=driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button')
search_btn.click()


# In[112]:


url=driver.current_url
print(url)


# In[113]:


det=url.split('@')[1]
det


# In[114]:


lat=det.split(",")[0]
long=det.split(',')[1]
print(lat, long)


# # Q6. Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[8]:


import selenium
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup


# In[9]:


driver=webdriver.Chrome()


# In[10]:


driver.get('https://www.digit.in/')


# In[11]:


driver.maximize_window()


# In[13]:


option=driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[2]/span')
option.click()


# In[14]:


best_laptop_option=driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[2]/div[2]/div/div[1]/span[4]')
best_laptop_option.click()


# In[15]:


bestgaming_laptop_option=driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[2]/div[2]/div/div[5]/div/div[2]/a/div')
bestgaming_laptop_option.click()


# In[16]:


laptop_name=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="datahreflink"]')][:7]
laptop_name


# In[17]:


brand_name=[i.text.split(" ")[0] for i in driver.find_elements(By.XPATH, '//span[@class="datahreflink"]')][:7]
brand_name


# In[18]:


soup=BeautifulSoup(driver.page_source, 'html.parser')


# In[19]:


specifications=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="product-detail"]')]
specifications


# In[20]:


for i in specifications:
    info=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="value"]')]
info   


# In[21]:


os=info[:28:4]
os


# In[22]:


display=info[1:28:4]
display


# In[23]:


processor=info[2:28:4]
processor


# In[24]:


memory=info[3:28:4]
memory


# In[26]:


#Another method using bs4
for i in soup.find_all('div', class_='product-detail'):
    info=i.find_all('div', class_="value")
    display1=info[1].text
    print(display1)


# In[27]:


details=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Spcs-details"]/table/tbody/tr/td')]
details


# In[28]:


details.index("Graphics Processor")


# In[29]:


graphic_processor=details[14:147:21]
graphic_processor


# In[30]:


body=details[17:147:21]
body


# In[31]:


price=details[20:148:21]
price


# In[32]:


image=[i.get_attribute('src') for i in driver.find_elements(By.XPATH, '//img[@class="lzy_img"]')][4:38:5]
image


# In[33]:


pdt_url=[i.get_attribute('data-href') for i in driver.find_elements(By.CLASS_NAME, "datahreflink")][:7]
pdt_url


# In[34]:


Best_Gaming_Laptops=pd.DataFrame({"Product Name":laptop_name, "Brand":brand_name, "Operating System":os, "Display Size":display, "Processor":processor, "Memory":memory, 'Graphic Processor':graphic_processor, "Body Details":body, "Price":price, "Product URL":pdt_url, "Image":image})
Best_Gaming_Laptops


# # Q7 Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”

# In[1]:


import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[150]:


driver=webdriver.Chrome()


# In[151]:


driver.get("https://www.forbes.com")
time.sleep(5)


# In[152]:


option=driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div[1]/div[1]/div/div')
option.click()


# In[156]:


select_billionare=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div[1]/div[1]/div[2]/ul/li[2]/div[1]')
select_billionare.click()


# In[158]:


select_wrld_bln=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div[1]/div[1]/div[2]/ul/li[2]/div[2]/div[3]/ul/li[1]/a')
select_wrld_bln.click()


# In[159]:


rank=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')]
print(rank)


# In[160]:


net_worth=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Table_netWorth___L4R5 Table_dataCell__2QCve"]')]
net_worth


# In[161]:


country=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')][4:1400:7]
country


# In[162]:


name=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')][1:1400:7]
name


# In[166]:


industry=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Table_dataCell__2QCve"]')][3:800:4]
print(industry)


# In[167]:


age=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Table_dataCell__2QCve"]')][1:800:4]
source=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="Table_dataCell__2QCve"]')][2:800:4]
print(age, source)


# In[168]:


print(len(age), len(source), len(industry))


# In[169]:


Billionare_list=pd.DataFrame({"Rank":rank, "Name":name, "Net Worth":net_worth, "Age": age, "COUNTRY / TERRITORY":country, "Source":source, "Industry":industry})
Billionare_list


# # Q8 Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video. 

# In[2]:


driver=webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=92sDjg8OGhg')


# In[37]:


for _ in range(50):
    driver.execute_script('window.scrollBy(0,500)')
    
comments=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="style-scope ytd-expander"]')][0:500]
print(comments)

for i in range(len(comments)):
    if i > 500:
        breakBy.XPATH


# In[38]:


len(comments)


# In[39]:


upvotes=[]
likes=driver.find_elements(By.XPATH, '//span[@id="vote-count-middle"]')[0:500]
for i in likes:
    if i.text is not None :
        upvotes.append(i.text)
    else:
        upvotes.append("None")

upvotes


# In[40]:


len(upvotes)


# In[41]:


for i in range(len(upvotes)):
    if upvotes[i]=='':
        upvotes[i]= '-'
print(upvotes) 


# In[42]:


posting_time=[i.text for i in driver.find_elements(By.XPATH, '//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')][0:500]
posting_time


# In[43]:


len(posting_time)


# In[44]:


import pandas as pd


# In[45]:


youtube_details=pd.DataFrame({'Comments':comments, "Upvote Comments":upvotes, 'Posting Time':posting_time})
youtube_details


# # Q9.Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description.

# In[36]:


import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[45]:


driver=webdriver.Chrome()


# In[46]:


driver.maximize_window()


# In[47]:


driver.get('https://www.hostelworld.com/')


# In[48]:


input=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/input')
input.send_keys('London')


# In[49]:


select=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]/button/div[2]/div[1]')
select.click()


# In[51]:


search_btn=driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/button[2]")
search_btn.click()
time.sleep(5)


# In[53]:


hostel_name=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="property-name"]')][2:]
hostel_name


# In[54]:


len(hostel_name)


# In[55]:


distance=[i.text.strip('- ').split(' from')[0] for i in driver.find_elements(By.XPATH, '//span[@class="distance-description"]')]
distance


# In[56]:


len(distance)


# In[57]:


rating=[i.text for i in driver.find_elements(By.XPATH, '//span[@class="number"]')][2:]
rating


# In[58]:


len(rating)


# In[59]:


total_reviews=[i.text.strip('(').strip(")") for i in driver.find_elements(By.XPATH, '//span[@class="left-margin"]')]
total_reviews


# In[60]:


len(total_reviews)


# In[61]:


a=[]
containers=driver.find_elements(By.XPATH, '//div[@class="property-info-container"]')
for container in containers:
    try:
        overall_review=container.find_element(By.XPATH, './/span[@class="keyword"]').text
        a.append(overall_review)
    except:
        a.append('-')
o_review=a[2:]
o_review


# In[62]:


len(o_review)


# In[63]:


price=[]
price1=driver.find_elements(By.XPATH, './/strong[@class="current"]')
for i in price1:
    price.append(i.text)

price.insert(3,"-")
price.insert(6,"-")
price.insert(14,"-")
price.insert(16,"-")
price.insert(18,"-")
price.insert(20,"-")
price.insert(22,"-")
price.insert(24,"-")
price.insert(26,"-")
price.insert(28,"-")
price.insert(32,"-")
price.insert(34,"-")
price.insert(36,"-")
price.insert(38,"-")
price.insert(41,"-")
price.insert(42,"-")
price.insert(44,"-")
price.insert(50,"-")
price.insert(54,"-")
price.insert(56,"-")
price.insert(59,"-")


# In[64]:


price


# In[65]:


len(price)


# In[66]:


pvt=[]
dom=[]
for j in range(0,len(price)):
        if (j % 2 == 0):
            pvt.append(price[j])
        else:
            dom.append(price[j])
            
    
print("Dorm prices ",dom)
print("private prices",pvt)


# In[67]:


print(len(pvt), len(dom))


# In[ ]:





# In[52]:


pp=[]
containers=driver.find_elements(By.XPATH, '//div[@class="property-info-container"]')
for container in containers:
    
    try:
        price1=[i.text for i in container.find_elements(By.XPATH, './/strong[@class="current"]')]
        pp.append(price1)
    except:
        pp.append('-')
price_pp=pp[2:]
price_pp


# In[53]:


for pr in price_pp[0:23]:
    if len(pr)==1:
        pr.insert(0, '-')
price_pp


# In[54]:


for pr in price_pp[24:30]:
    if len(pr)==1:
        pr.insert(0, '-')
price_pp


# In[55]:


for pr in price_pp[23:24]:
    if len(pr)==1:
        pr.insert(1, '-')
price_pp


# In[56]:


for i in price_pp:
    pvt_price=i[0]
    dorm_price=i[1]
    print(pvt_price, dorm_price)


# In[68]:


url=[i.get_attribute('href') for i in driver.find_elements(By.XPATH, '//a[@rel="noreferrer noopener"]')][2:]
url


# In[69]:


print(len(url))


# In[70]:


for i in url:
    driver.get(i)
    all_facilities=[i.text for i in driver.find_elements(By.XPATH, '//ul[@class="facilities"]')]
    print(all_facilities)
    print('\n')


# In[76]:


free_facilities=[]
for i in url:
    driver.get(i)
    facilities=[i.text for i in driver.find_elements(By.XPATH, '//ul[@class="facilities"]')][0]
    free_facilities.append(facilities) 


# In[77]:


free_facilities


# In[78]:


len(free_facilities)


# In[79]:


property_des=[]
for i in url:
    driver.get(i)
    property=[i.text for i in driver.find_elements(By.XPATH, '//div[@class="content collapse-content"]')][:1]
    property_des.append(property)


# In[80]:


property_des


# In[81]:


len(property_des)


# In[82]:


print(len(hostel_name), len(distance), len(rating), len(total_reviews), len(o_review), len(pvt), len(dom), len(free_facilities), len(property_des))


# In[83]:


Hostel_details=pd.DataFrame({"Hostel Name":hostel_name, "Distance from City Centre":distance,"Ratings":rating, "Total Reviews": total_reviews, "Overall Reviews":o_review , "Private Price":pvt, "Dorms Price":dom, "Facilities":free_facilities, "Property Description":property_des})
Hostel_details


# In[84]:


Hostel_details.to_csv(r'C:\Users\asus 1\Desktop\Fliprobo\hostel_details.csv')


# In[ ]:




