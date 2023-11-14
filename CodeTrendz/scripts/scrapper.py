from bs4 import BeautifulSoup
import requests


class Web_Scrapper:  # web scrapper design
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts

    def scrape_linkedIn(self):
        pass

    def scrape(self):
        response = requests.get(self.platform_to_scrape)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
