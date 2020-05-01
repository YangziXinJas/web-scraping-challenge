from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd
import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_scraping_data = dict()
    # scrape NASA Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(5)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_ = 'article_teaser_body').text
    mars_scraping_data ['news_title'] = news_title
    mars_scraping_data['news_p']= news_p


    #JPL Mars Space Images - Featured Image

    # scrape NASA Mars News
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
 
    image_url = soup.find('img', class_ = 'thumb')
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url['src']
    mars_scraping_data['featured_image_url'] = featured_image_url

    #Mars Weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.full_screen()
    browser.visit(weather_url)
    time.sleep(15)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tweet = soup.find_all("article")[0]
    tweet.text
    tweet.find_all('span')
    weather_string = ''
    for span in tweet.find_all('span'):
        if 'sol' in span.text:
            weather_string = span.text
    #weather_string

    mars_scraping_data['weather_string']= weather_string

    #Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    facts_df = pd.read_html(facts_url)[0]
    facts_df.columns = ['Property', 'Values']
    data = facts_df.to_html('table.html')
    mars_scraping_data['facts_data'] = data


#     #Mars Hemispheres
#     hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(hemisphere_url)
#     hemisphere_html = browser.html  
#     soup = BeautifulSoup(hemisphere_html, 'html.parser')
#     time.sleep(15)

#     results = soup.find_all('div', class_='item')
#     hemisphere = []
#     for result in results:
#         title = soup.find('h2', class_='title')
#         url_hemisphere = soup.find('a',class_= 'itemLink product-item')['href']
#         browser.visit(hemisphere_url + url_hemisphere)
#         html_hemisphere =browser.html
#         soup = BeautifulSoup(html_hemosphere, 'html.parser')
#     
#  
#         img_url = hemisphere_url + soup.find('img', class_ = 'wide-image')['src']
#         hemisphere.append({"title": title, )
#                            "img_url": img_url})


    
#         mars_scraping_data['hemisphere']= hemisphere



    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_scraping_data
