# AAA Gas Prices Scraper
This project is a Python script that extracts the AAA National Average gas price from https://gasprices.aaa.com/. The script uses the requests library to fetch the HTML content of the website and the BeautifulSoup library to parse and extract the required data.

# Features
* Fetches the AAA National Average gas price
* Parses and extracts data using BeautifulSoup
* Custom User-Agent header to bypass request restrictions

# Requirements
* Python 3.x
* requests
* beautifulsoup4
* 're'

# Installation
1. Make sure you have Python 3 installed on your system. If not, download and 2. install the latest version from https://www.python.org/downloads/.
2. Install the required libraries:
    CODE 
    { 
    - bash
    pip install requests
    pip install beautifulsoup4
    }

# Usage
1. Save the provided script as a .py file, e.g., gas_prices_scraper.py.
2. Open a terminal or command prompt, navigate to the directory where the script is saved, and run the following command:

The script will print the extracted gas price on the terminal or command prompt.

    CODE
     { 
    - bash
    python gas_prices_scraper.py
    }

# Disclaimer
Please note that web scraping can be against the terms of service of some websites. Always check a website's policies before scraping its content. This script is for educational purposes only, and the author is not responsible for its misuse.

According to 'robot.txt' webscrapping is not disallowed for the main page 'https://gasprices.aaa.com/'

"
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://gasprices.aaa.com/wp-sitemap.xml

"