#!/usr/bin/env python
# coding: utf-8

# # Web Scraping and CSV Conversion Project
# 
# ## Overview
# This Python script performs web scraping on the Wikipedia page listing the largest companies in the United States by revenue. The data is extracted from the Fortune 500 list for the year 2023, based on the fiscal year 2022.
# 
# ## Source
# The data is sourced from the Wikipedia page: [List of largest companies in the United States by revenue](put_the_wikipedia_link_here)
# 
# ## Dependencies
# - Python 
# - BeautifulSoup for web scraping
# - Pandas for data manipulation and CSV conversion
# 
# 
# 
# - The final result will be saved as a CSV file named 'largest_companies_2023.csv'.
# 

# In[36]:


# Import necessary libraries
from bs4 import BeautifulSoup  # BeautifulSoup is used for web scraping
import requests  # Requests is used for making HTTP requests

# Explanation:
# - BeautifulSoup is a library for pulling data out of HTML and XML files.
# - 'requests' is a popular Python library for making HTTP requests.


# In[21]:


# Import the pandas library and alias it as 'pd'
import pandas as pd

# Explanation:
# - 'import pandas as pd' is a common convention to import the pandas library and alias it as 'pd' for easier reference.
# - Pandas is widely used for data manipulation and analysis, and the alias 'pd' is a common shorthand in the Python community.


# In[37]:


# Define the URL of the Wikipedia page containing the list of largest companies in the United States by revenue
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Make an HTTP request to the specified URL and get the webpage content
page = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content of the webpage
soup = BeautifulSoup(page.text, 'html')
# Explanation:
# - 'requests.get(url)' fetches the HTML content of the specified URL.
# - 'BeautifulSoup(page.text, 'html')' creates a BeautifulSoup object to parse the HTML content using the 'html'.


# In[38]:


# Print the entire HTML content of the webpage
print(soup)

# Explanation:
# - 'print(soup)' prints the entire HTML content of the webpage that has been parsed using BeautifulSoup.
# - This can be helpful for inspecting the structure of the HTML and identifying the elements you want to extract.
# - However, printing the entire HTML might be overwhelming for large pages, so it's often more practical to inspect specific sections.


# In[41]:


# Find the first 'table' element in the parsed HTML content
table = soup.find('table')

# Explanation:
# - 'soup.find('table')' searches for the first 'table' element in the parsed HTML content.
# - This assumes that the table containing the data you want is the first 'table' element on the page.
# - If there are multiple tables on the page, you might need to use a more specific selector or index to identify the correct table.
# - The variable 'table' now holds the BeautifulSoup object representing the found 'table' element.

table


# In[45]:


# Find all 'table' elements in the parsed HTML content and select the second one
table = soup.find_all('table')[1]

# Explanation:
# - 'soup.find_all('table')' finds all 'table' elements in the parsed HTML content and returns a list.
# - '[1]' selects the second 'table' element from the list. Note that indices are zero-based, so [1] refers to the second element.
# - This assumes that the table you are interested in is the second 'table' element on the page.
# - Adjust the index accordingly if the target table is at a different position.
# - The variable 'second_table' now holds the BeautifulSoup object representing the selected 'table' element.

table


# In[44]:


# Find the 'table' element with the class 'wikitable sortable' in the parsed HTML content
target_table = soup.find('table', class_='wikitable sortable')

# Explanation:
# - 'soup.find('table', class_='wikitable sortable')' searches for the first 'table' element with the specified class.
# - This is a more specific way to identify the target table, assuming it has the class 'wikitable sortable'.
# - If there are multiple tables with this class, you may need to adjust the code accordingly.
# - The variable 'target_table' now holds the BeautifulSoup object representing the found 'table' element.

target_table


# In[46]:


# Find all 'table' elements in the parsed HTML content and select the second one
table = soup.find_all('table')[1]

# Print the entire HTML content of the selected table
print(table)

# Explanation:
# - 'soup.find_all('table')' finds all 'table' elements in the parsed HTML content and returns a list.
# - '[1]' selects the second 'table' element from the list. Note that indices are zero-based, so [1] refers to the second element.
# - This assumes that you are interested in printing the entire HTML content of the second table on the page.
# - Adjust the index accordingly if you want to print a different table.
# - The 'print(table)' statement outputs the HTML content of the selected table.


# In[47]:


# Find all 'th' (table header) elements within the selected table
world_title = table.find_all('th')

# Explanation:
# - 'table.find_all('th')' finds all 'th' elements within the previously selected table.
# - This is typically used to extract the column headers (titles) of the table.
# - The variable 'world_title' now holds a list of BeautifulSoup objects representing the 'th' elements in the table.

world_title


# In[48]:


# Extract the text content of each 'th' element and remove leading/trailing whitespaces
world_table_title = [title.text.strip() for title in world_title]

# Print the extracted table titles
print(world_table_title)

# Explanation:
# - The list comprehension '[title.text.strip() for title in world_title]' extracts the text content of each 'th' element and removes leading/trailing whitespaces.
# - The variable 'world_table_title' now holds a list of cleaned and formatted table titles.
# - The 'print(world_table_title)' statement outputs the list of extracted table titles.


# In[49]:


# Create an empty DataFrame with columns specified by 'world_table_title'
df = pd.DataFrame(columns=world_table_title)

# Explanation:
# - 'pd.DataFrame(columns=world_table_title)' creates a new pandas DataFrame with columns specified by the 'world_table_title' list.
# - The variable 'df' now holds an empty DataFrame with the specified column names.

df


# In[50]:


# Find all 'tr' (table row) elements within the selected table
column_data = table.find_all('tr')

# Explanation:
# - 'table.find_all('tr')' finds all 'tr' elements within the previously selected table.
# - This is typically used to extract the rows of the table.
# - The variable 'column_data' now holds a list of BeautifulSoup objects representing the 'tr' elements in the table.

column_data


# In[51]:


# Iterate over each 'tr' element in the list, starting from the second element (skipping the header row)
for row in column_data[1:]:
    # Find all 'td' (table data) elements within the current row
    row_data = row.find_all('td')
    
    # Extract the text content of each 'td' element, remove leading/trailing whitespaces, and store in a list
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Get the current length of the DataFrame
    length = len(df)
    
    # Add a new row to the DataFrame with the extracted data
    df.loc[length] = individual_row_data

# Explanation:
# - The for loop iterates over each 'tr' element in the list, starting from the second element (skipping the header row).
# - Inside the loop, 'row.find_all('td')' finds all 'td' elements within the current row.
# - The list comprehension '[data.text.strip() for data in row_data]' extracts the text content of each 'td' element, removes leading/trailing whitespaces, and stores the data in 'individual_row_data'.
# - 'len(df)' gets the current length of the DataFrame 'df'.
# - 'df.loc[length] = individual_row_data' adds a new row to the DataFrame with the extracted data.
 


# In[30]:


# Display the first few rows of the DataFrame 'df'
df.head()

# Explanation:
# - 'df.head()' is a pandas function that displays the first few rows of the DataFrame.
# - It's useful for quickly inspecting the structure and content of the DataFrame.
# - By default, it shows the first 5 rows, but you can pass a different number inside the parentheses to display a different number of rows.


# In[52]:


# Save the DataFrame 'df' to a CSV file
df.to_csv(r'C:\Users\IPSITA\Downloads\largest_companies_2023.csv', index=False)

# Explanation:
# - 'df.to_csv()' is a pandas function that writes the contents of a DataFrame to a CSV file.
# - The first argument is the file path where the CSV file will be saved.
# - 'index=False' is used to exclude the DataFrame index from being written to the CSV file.
# - Adjust the file path as needed to specify the location and name of the CSV file you want to create.


# ## Conclusion
# 
# ### Project Overview
# This project aimed to scrape data from the Wikipedia page listing the largest companies in the United States by revenue as of 2023. The data was extracted from the Fortune 500 list for the fiscal year 2022 using web scraping techniques.
# 
# ### Workflow Summary
# 1. **Web Scraping:** Utilized the BeautifulSoup library to parse the HTML content of the Wikipedia page and extract relevant information.
# 2. **DataFrame Creation:** Employed pandas to create a DataFrame for organizing and manipulating the extracted data.
# 3. **CSV Conversion:** Saved the DataFrame to a CSV file for further analysis and sharing.
# 
# ### Challenges and Solutions
# - **HTML Structure:** The structure of the HTML page, including nested tables, presented challenges in data extraction. This was addressed by selecting the appropriate table and navigating through the HTML structure.
# - **Data Cleaning:** Some data required cleaning, such as removing unnecessary whitespaces. This was achieved using list comprehensions and pandas functionality.
# 
# ### Results
# The final output is a CSV file named 'largest_companies_2023.csv' containing information about the largest companies in the United States, including columns such as company name, revenue, and other relevant details.
# 
# ### Future Work
# - This project can be extended to include additional data points or to automate periodic updates.
# - Consider exploring more advanced web scraping techniques for handling dynamic content or JavaScript-rendered pages.
# 
# ## Acknowledgments
# Special thanks to the BeautifulSoup and pandas libraries for their role in simplifying the web scraping and data manipulation processes.
# 
# This project provides a foundation for further analysis and insights into the landscape of the largest companies in the United States by revenue.
# 

# 
