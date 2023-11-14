from bs4 import BeautifulSoup
import requests

# ! Linked In only


class Web_Scrapper:  # web scrapper design
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts

        self.company_name = ""
        self.job_description = ""

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
    "https://uk.linkedin.com/jobs/view/junior-frontend-developer-fully-remote-at-it-talent-solutions-3748049402?refId=GDeZd2Pdvnz2zSledLl2Pw%3D%3D&trackingId=CXzc%2FcrFTuBadYff4oxX9A%3D%3D&trk=public_jobs_topcard-title&original_referer=https%3A%2F%2Fuk.linkedin.com%2Fjobs%2Fsoftware-engineer-jobs%3FcurrentJobId%3D3748049402%26position%3D3%26pageNum%3D0",
    5,
)
web_scrapper.scrape()
