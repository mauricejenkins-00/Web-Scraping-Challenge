#Webscraping Application
#Importing Dependencies

from flask import Flask, render_template, redirect
from pandas import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

#Application Name
mars_site = Flask(__name__)

#Defining procedures to scrape a number of websites

def scrape():
    executeable_path = {'executable_path': ChromeDriverManager().install}
    browser = Browser('chrome', **executeable_path, headless=False)
    url = ["https://redplanetscience.com/", "https://spaceimages-mars.com", "https://galaxyfacts-mars.com","https://marshemispheres.com/"]
    
    #Scraping News
    browser.visit(url[0])
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    mars_info = {}
    
    mars_info['latest_title'] = soup.find("div", class_ = "content_title").get_text()
    mars_info['latest_paragraph'] = soup.find("div", class_ = "article_teaser_body").get_text()
    
    browser.quit()
    return (mars_info)
