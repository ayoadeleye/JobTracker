import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

BASE_URL = f"www.indeed.com"
template = "https://www.indeed.com/jobs?q={}&l={}"
def get_url(position, location):
    url = template.format(position, location)
    return url


url = get_url()
def extractJob(html):
    pass

def extractJob(html):
    pass