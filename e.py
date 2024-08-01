import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_ebay(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for item in soup.select('.s-item'):
        title = item.select_one('.s-item__title')
        price = item.select_one('.s-item__price')

        if title and price:
            products.append({
                'Title': title.text.strip(),
                'Price': price.text.strip()
            })

    return products


st.title('eBay Product Scraper')

url = st.text_input('Enter eBay search URL:')

if url:
    if st.button('Scrape Data'):
        with st.spinner('Scraping data...'):
            products = scrape_ebay(url)

        if products:
            df = pd.DataFrame(products)
            st.dataframe(df)

            # CSV Download
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='ebay_products.csv',
                mime='text/csv',
            )
        else:
            st.error('No products found. Please check the URL and try again.')

st.markdown('---')
st.markdown(
    'Note: This application is for educational purposes only. Please respect eBay\'s terms of service and robots.txt file.')
