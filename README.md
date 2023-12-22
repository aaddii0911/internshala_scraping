### Objective:

Develop a script to automate the extraction of job listing information from **Internshala**. This script aims to gather details such as job title, company name, location, and other relevant information from the Internshala website.

### Prerequisites:

1. **Python Setup:** Ensure Python is installed on your computer.
2. **Libraries:** Install necessary Python libraries: **`selenium`**, **`beautifulsoup4`**, and **`pandas`**. Optionally, install **`gspread`** for Google Sheets integration.
3. **Web Driver:** Download a web driver (like ChromeDriver or GeckoDriver) compatible with your browser.
4. **Google Account:** (Optional) For saving data to Google Sheets, ensure you have a Google account and a Google Sheets document.
5. **Google Sheets API:** (Optional) Enable the Google Sheets API in your Google Cloud Console and download the credentials file.

### Step-by-Step Instructions:

1. **Environment Setup:**
    - Import necessary Python libraries (**`selenium`**, **`beautifulsoup4`**, **`pandas`**, and optionally **`gspread`**).
    - Configure Selenium WebDriver with the path to your downloaded driver executable.
2. **WebDriver Initialization:**
    - Initialize the WebDriver to open a browser window and navigate to the Internshala website.
3. **Handling Pop-ups:**
    - Create a function to close any pop-ups or advertisements that appear on the Internshala site.
4. **Accessing Job Listings:**
    - Direct the WebDriver to the specific Internshala job listings page (e.g., fresher jobs, internship opportunities).
5. **Scraping Job Listings:**
    - Use BeautifulSoup to parse the HTML content obtained via Selenium.
    - Develop a function to extract relevant details from each job listing, such as the company name, job title, location, etc.
6. **Pagination and Data Collection:**
    - Implement logic to navigate through multiple pages of job listings if necessary, capturing data from each page.
7. **Data Aggregation:**
    - Store all extracted job details in a structured format, like a list or dictionary.
8. **Creating a DataFrame:**
    - Convert the aggregated data into a Pandas DataFrame for easier manipulation and readability.
9. **Exporting to Google Sheets (Optional):**
    - If integrating with Google Sheets, use **`gspread`** and Google Sheets API credentials for authentication.
    - Upload the DataFrame data to Google Sheets for storage and analysis. This step is optional.

**(Optional) Additional Resources to setup Gspread and Google Service Account:**

https://youtu.be/rPV9sJQCqr0

https://youtu.be/PyaRgFJBnH4

**URL**
url = 'https://internshala.com/fresher-jobs/analytics-jobs/'

