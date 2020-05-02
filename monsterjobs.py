# Import required packages
import requests
from bs4 import BeautifulSoup

# Retrieve Job Title and Job Location to search for
job_type = input("What type of job do you want to search?").lower()
job_location = input("What location do you want to search?").lower()

# Clean up Responses
job_type_clean = job_type.replace(' ', '-')
job_location_clean = job_location.replace(',', '__2C')
job_location_clean = job_location_clean.replace(' ', '-')

# Set up Url
URL = 'https://www.monster.com/jobs/search/?q=' + job_type_clean + '&where=' + job_location_clean
page = requests.get(URL)

# Parse the content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the results section of the job search
results = soup.find(id='SearchResults')

# Grab each element out of the job search
job_elems = results.find_all('section', class_='card-content')

# Loop through jobs and print out the title, company, and location
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
