from bs4 import BeautifulSoup
import requests

# ! Linked In only for now


# https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=25


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
            divs = soup.find_all("div", class_="base-search-card__info")

            print(divs)

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
    "https://www.linkedin.com/jobs/search/?currentJobId=3727684236&geoId=101165590&keywords=software%20engineer&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true",
    5,
)
web_scrapper.find_job_urls()
