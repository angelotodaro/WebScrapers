# Import required packages
import requests
from bs4 import BeautifulSoup

# Retrieve Job Title and Job Location to search for
job_type = input("What type of job do you want to search?").lower()
job_location = input("What location do you want to search?").lower()

# Clean up Responses
job_type_clean = job_type.replace(' ', '+')
job_location_clean = job_location.replace(',', '%2C')
job_location_clean = job_location_clean.replace(' ', '+')

# Set up Url
URL = 'https://www.indeed.com/jobs?q=' + job_type_clean + '&l=' + job_location_clean
page = requests.get(URL)


# Parse the content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the results section of the job search
results = soup.find(id='resultsCol')
print(results)

# Grab each element out of the job search
job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

# Loop through jobs and print out the title, company, and location
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find('div', class_='location accessible-contrast-color-location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
