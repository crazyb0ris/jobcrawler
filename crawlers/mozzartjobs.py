from bs4 import BeautifulSoup
import requests

class MozzartCrawler:

    BASE_URL = "https://rs.mozzart.org"
    URL = BASE_URL + "/karijera/otvorene-radne-pozicije"

    def find_jobs(self):

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Nađi sektor "IT"
        it_sector = soup.find_all('div', class_="job-sector")

        # U okviru njega nađi sve job wrapper-e
        for sector in it_sector:
            job_wrappers = sector.find_all('div', class_="job-wrapper")

            for job in job_wrappers:
                # Pozicija (naziv posla)
                title = job.find('p').get_text(strip=True)

                # Link
                relative_link = job.find('a')['href']
                full_link = self.BASE_URL + relative_link

                print("Pozicija:", title)
                print("Link:", full_link)
                print("----------------------")
                print("Test commit")
