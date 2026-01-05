from bs4 import BeautifulSoup
import requests

#Create request to targeted site

a1_job_board_serbia= "https://rs.mozzart.org/karijera/otvorene-radne-pozicije"
a1_jobs = requests.get(a1_job_board_serbia)
a1_jobs_content = a1_jobs.text


soup = BeautifulSoup(a1_jobs_content, 'html.parser')

print(soup.find('div', {"class": "job-sector"}))
