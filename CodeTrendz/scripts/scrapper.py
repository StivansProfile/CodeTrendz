from bs4 import BeautifulSoup
import requests

# ! Linked In only for now

"""
To scrape multiple pages:
https://uk.linkedin.com/jobs/software-engineer-jobs?currentJobId=3758062458&position=1&pageNum=0

collect the ulrs based on position
- scrape the whole page and find the urls with position 1 to maybe 50
- find a way to click on each url and for each url perform the scrapping function

"""


class Web_Scrapper:  # web scrapper design
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts

        self.job_urls = []
        self.company_name = ""
        self.job_description = ""

    def find_job_urls(self):
        pass

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
    "https://uk.linkedin.com/jobs/view/graduate-software-engineer-up-to-%C2%A375-000-%2B-bonus-%2B-package-at-hunter-bond-3762161377?refId=0DlIIe2tVFfIVv%2BFE%2FBVlQ%3D%3D&trackingId=NSOHV1jGfjqIHB%2BCKsFxgQ%3D%3D&trk=public_jobs_topcard-title",
    5,
)
web_scrapper.scrape()
