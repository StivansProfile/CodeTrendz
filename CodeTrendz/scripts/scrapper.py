from bs4 import BeautifulSoup
import requests

# ! Linked In only for now


# https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=25

"""
At the moment the scrapper can do the following:
- Find a custom number of job urls from LinkedIn
- Scrape the job descriptions off of the job urls
"""


class Web_Scrapper:
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts
        self.job_urls = []

        self.company_name = []
        self.job_description = []
        self.skills = []

    # find the job post urls
    def find_job_urls(self):
        response = requests.get(self.platform_to_scrape)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all(
                "a",
                class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]",
            )

            for link in links:
                href = link.get("href")
                self.job_urls.append(href)

            print(self.job_urls)

        else:
            print("error", response.status_code)

    # scrape the data off of the job urls
    def scrape(self):
        self.find_job_urls()

        for url in self.job_urls:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # # finding the company name
                # company_name = soup.find(
                #     "h1",
                #     class_="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title",
                # )
                # self.company_name.append(company_name)

                # # finding job description
                # container = soup.find("div", class_="topcard__flavor-row")
                # job_description = soup.find(
                #     "div", class_="description__text description__text--rich"
                # )
                # self.job_description.append(job_description.text)

                # # print(self.company_name)
                # # print(container.text)
                # print(self.job_description)

                # find relevant skills
                div_with_p5 = soup.find("div", class_="pt5")
                self.skills.append(div_with_p5)

                print(self.skills)

            else:
                print("Failed to retrieve data", response.status_code)


web_scrapper = Web_Scrapper(
    "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=0",
    5,
)
web_scrapper.scrape()
