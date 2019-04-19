from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
import os
import requests
from selenium import webdriver


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_info = {}

     # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    # Design an XPATH selector to grab the "Mars in natural color in 2007" image on the right
    xpath = '//td//a[@class="image"]/img'

    # Use splinter to Click the "Mars in natural color in 2007" image 
    # to bring up the full resolution image
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # Find the src for the mrs image
    img_url = soup.find("img")["src"]
    img_url = "https://www.jpl.nasa.gov/"+img_url
    featured_image_url = img_url

    # relative_image_path = soup.find_all('img')[2]["src"]
    # img_url = url + relative_image_path
    # featured_image_url = img_url


    # Collect the latest News Title and Paragraph Text
    news_title=soup.find('div',class_='content_title').get_text()
    # print (news_title)

    # news_title=soup.find_all('div',{"class":"content_title"})
    # print (news_title)

    # Collect the latest News Paragraph Text
    news_p=soup.find('div',class_='article_teaser_body').get_text()

    # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text


    # Variables to store data in a dictionary
    mars_data = {
    "news_title" : news_title,
    "news_p" : news_p,
    # "mars_weather" : mars_weather
    }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_info

#######################################################


