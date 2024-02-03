
# Web Scraping Project: Largest Companies in the United States (2023)

## Project Overview
This project involves web scraping data from the Wikipedia page listing the largest companies in the United States by revenue as of 2023. The goal is to extract valuable information from the Fortune 500 list for the fiscal year 2022 and organize it for further analysis.

## Steps Taken
1. **Web Scraping:** Utilized the BeautifulSoup library in Python to parse the HTML content of the Wikipedia page.
2. **DataFrame Creation:** Employed pandas to create a DataFrame for organizing and manipulating the extracted data.
3. **CSV Conversion:** Saved the DataFrame to a CSV file for easy sharing and future analysis.

## Project Details
- **Language Used:** Python
- **Libraries Used:** BeautifulSoup, requests, pandas
- **Wikipedia URL:** [List of largest companies in the United States by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)

## Project Structure
- `script.ipynb`: Python script containing the web scraping and data processing code.
- `largest_companies_2023.csv`: CSV file containing the extracted data.


## Conclusion
The final output is a CSV file named 'largest_companies_2023.csv' containing information about the largest companies in the United States. The script navigates the HTML structure of the Wikipedia page, extracts relevant data, and organizes it into a structured format for analysis.

## Future Work
- Consider expanding the project to include more data points or automate periodic updates.
- Explore advanced web scraping techniques for handling dynamic content or JavaScript-rendered pages.

## Acknowledgments
Special thanks to the BeautifulSoup and pandas libraries for their contributions to simplifying the web scraping and data manipulation processes.

This project provides a foundation for further analysis and insights into the landscape of the largest companies in the United States by revenue.
