Amazon Product Scraper Overview

Amazon Product Scraper is a simple web application built with Streamlit for scraping product information from Amazon search results. The application allows users to input an Amazon search URL, and it extracts product titles, prices, and ratings, displaying them in a tabular format.

Features
Scrapes Product Data: Extracts product titles, prices, and ratings from Amazon search result pages.
  
User Interface: Built with Streamlit, providing a clean and interactive UI for users to input URLs and view results.
  
Educational Use: Designed for learning purposes to demonstrate web scraping techniques.

Requirements
Python 3.x
Streamlit
Requests
BeautifulSoup4
Pandas
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install streamlit requests beautifulsoup4 pandas
Usage
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your browser and navigate to the URL provided by Streamlit.

Enter an Amazon search URL in the input box.

Click the "Scrape Data" button to fetch and display the product information.

Code Explanation
scrape_amazon(url): This function takes an Amazon search URL, sends a request to it, and parses the HTML to extract product titles, prices, and ratings.

Headers: Sets a user-agent and accept-language to mimic a real browser request.

BeautifulSoup: Parses HTML content to locate and extract product information.
  
Streamlit UI:

st.title: Displays the application title.
st.text_input: Takes the Amazon search URL input from the user.
st.button: Initiates the scraping process when clicked.
st.spinner: Shows a loading spinner during the scraping process.
st.dataframe: Displays the scraped data in a tabular format.
st.error: Displays an error message if no products are found.
  
Notes
This application is intended for educational purposes only.
  
Respect Amazon's terms of service and robots.txt file when scraping their site.
License

Acknowledgements
Streamlit for providing a simple and powerful tool for building web applications.
BeautifulSoup for web scraping and parsing HTML.
Requests for sending HTTP requests.
Feel free to contribute or report issues. Happy scraping!
