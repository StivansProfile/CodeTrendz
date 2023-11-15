from bs4 import BeautifulSoup
import requests

# ! Linked In only for now

"""
https://www.google.com/search?client=firefox-b-d&q=software+developer+jobs+uk+linked+in&ibp=htl;jobs&sa=X&ved=2ahUKEwjZmcfeqcaCAxWMXUEAHQI9A5sQudcGKAF6BAgVECo&sxsrf=AM9HkKkatznxLrfouDM610IxeNrqhFcBKQ:1700062339130#htivrt=jobs&htidocid=-L0s1oDT06XlRSxWAAAAAA%3D%3D&fpstate=tldetail

we can probably scrape the job urls from the above link

"""


class Web_Scrapper:
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts

        self.job_urls = []
        self.company_name = ""
        self.job_description = ""

    # find the first 10 job posts' urls
    def find_job_urls(self):
        response = requests.get(self.platform_to_scrape)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

        else:
            print("error", response.status_code)

    # scrape the data off of the first 10 job posts
    def scrape(self):
        response = requests.get(self.platform_to_scrape)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # finding the company name
            self.company_name = soup.find(
                "h1",
                class_="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title",
            )

            # finding job description
            container = soup.find("div", class_="topcard__flavor-row")
            self.job_description = soup.find(
                "div", class_="description__text description__text--rich"
            )

            if self.company_name:
                print(self.company_name.text)
                print(container.text)
                print(self.job_description.text)
            else:
                print("Nothing found")
        else:
            print("Failed to retrieve data", response.status_code)


web_scrapper = Web_Scrapper(
    "https://www.linkedin.com/jobs/search/?currentJobId=3744358098&keywords=software%20developer&origin=SUGGESTION",
    5,
)
web_scrapper.find_job_urls()
