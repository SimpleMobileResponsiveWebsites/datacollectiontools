eBay Product Scraper

This is a simple web application built using Streamlit that allows users to scrape product data from eBay search result pages. It extracts product titles and prices and presents the data in a downloadable CSV format.

Features
eBay Scraping: Extracts product titles and prices from eBay search result pages.
Streamlit Interface: User-friendly web interface for inputting URLs and displaying results.
CSV Download: Allows users to download the scraped data in CSV format.

Prerequisites
Ensure you have the following Python packages installed:

streamlit
requests
beautifulsoup4
pandas
You can install these packages using pip:

bash
Copy code
pip install streamlit requests beautifulsoup4 pandas
Usage
Run the Streamlit App:

Save the code into a file named app.py and run the following command in your terminal:

bash
Copy code
streamlit run app.py
Enter eBay Search URL:

Open your web browser and go to the local server address (usually http://localhost:8501). Enter the eBay search URL in the input field.

Scrape Data:

Click the "Scrape Data" button to start the scraping process.

View and Download Data:

The scraped product data will be displayed in a table format. You can download this data as a CSV file by clicking the "Download data as CSV" button.

Notes
This application is intended for educational purposes only.
Please ensure compliance with eBay’s terms of service and robots.txt file when using this scraper.

Example
Here's an example of how to use the application:

Go to eBay and search for a product, e.g., "laptop".
Copy the URL from the search results page.
Paste the URL into the Streamlit app and click "Scrape Data".
View the results and download them if needed.

Troubleshooting
No Products Found: Ensure the URL is correct and points to a valid eBay search results page.
Data Not Displaying: Verify that the selectors used in the scrape_ebay function match the current eBay page structure.
Feel free to contribute or suggest improvements to this project. Happy scraping!
