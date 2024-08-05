from bs4 import BeautifulSoup as bs
import requests as req
from sources import get_amazon, get_flipkart, get_ebay, get_shopclues
import streamlit as st


def get_item_details(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    html_text = req.get(url, headers)
    soup = bs(html_text.text, 'lxml')
    # print(soup.prettify().text)
    if 'amazon' in url:
        get_amazon(soup)
    
    elif 'flipkart' in url:
        get_flipkart(soup)
    
    elif 'ebay' in url:
        get_ebay(soup)

    elif 'shopclues' in url:
        get_shopclues(soup)
# get_item_details(link)

def perform_comparison(url_1, url_2):
    get_item_details(url_1)
    get_item_details(url_2)
st.title(":blue[E-Commerce Scraper]")
link = st.text_input("Enter Product URL:")
if st.button("Get Details"):
    get_item_details(link)
compare = st.text_input("Enter Site To Compare With(Optional)")
if st.button(":orange[Compare]"):
    perform_comparison(link, compare)