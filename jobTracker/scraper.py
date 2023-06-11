import requests
from bs4 import BeautifulSoup

# Define the list of URLs for the job sites you want to scrape
job_sites = [
    'https://indeed.com'
]


def scrape_indeed_jobs(query):
    url = f'https://www.indeed.com/jobs?q={query.replace(" ", "+")}'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')

    jobs = []
    for job_element in job_elements:
        title = job_element.find('h2', class_='title').text.strip()
        company = job_element.find('span', class_='company').text.strip()
        location = job_element.find('div', class_='recJobLoc')['data-rc-loc']
        date = job_element.find('span', class_='date').text.strip()
        link = 'https://www.indeed.com' + job_element.find('a')['href']
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'date': date,
            'link': link
        })

    return jobs