import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for item in soup.select('.s-result-item'):
        title = item.select_one('.a-text-normal')
        price = item.select_one('.a-price-whole')
        rating = item.select_one('.a-icon-star-small .a-icon-alt')

        if title and price:
            products.append({
                'Title': title.text.strip(),
                'Price': price.text.strip() if price else 'N/A',
                'Rating': rating.text.strip() if rating else 'N/A'
            })

    return products


st.title('Amazon Product Scraper')

url = st.text_input('Enter Amazon search URL:')

if url:
    if st.button('Scrape Data'):
        with st.spinner('Scraping data...'):
            products = scrape_amazon(url)

        if products:
            df = pd.DataFrame(products)
            st.dataframe(df)
        else:
            st.error('No products found. Please check the URL and try again.')

st.markdown('---')
st.markdown(
    'Note: This application is for educational purposes only. Please respect Amazon\'s terms of service and robots.txt file.')
