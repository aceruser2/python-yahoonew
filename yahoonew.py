
# coding: utf-8

# In[1]:

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
from bs4 import BeautifulSoup

#driver=webdriver.PhantomJS(executable_path="")
driver=webdriver.Chrome(executable_path="")
driver.get("https://tw.news.yahoo.com/technology/archive/")
time.sleep(3)
bs1=BeautifulSoup(driver.page_source,"html.parser")
news=""
for new in bs1.find("ul",{"class":"yom-list-wide thumbnail"}):
    title=new.find("div",{"class":"txt"}).find("a").text
    href=new.find("div",{"class":"txt"}).find("a").attrs['href']
    url="https://tw.news.yahoo.com"+href
    driver.get(url)
    time.sleep(15)
    bs2=BeautifulSoup(driver.page_source,"html.parser")
    content=bs2.find("div",{"class":"yom-mod yom-art-content "}).find("div",{"class":"bd"}).get_text()
    #print(content)
    
    news+=title+"\n"+"\n"+content+"\n"+"\n"

    

#print(news)
f=open("yahoonews.txt","w")    
f.write(news)
f.close()

    
    
driver.close()











