import requests
from bs4 import BeautifulSoup

URL = 'https://www.merriam-webster.com/dictionary/dogs'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
job_elems = results.find_all('section', class_='sb-0')
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('span', class_='sb-0')
    company_elem = job_elem.find('span', class_='sb-0')
    location_elem = job_elem.find('span', class_='sb-0')
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()