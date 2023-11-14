class Web_Scrapper:  # web scrapper design
    def __init__(self, platform_to_scrape, number_of_job_posts):
        self.platform_to_scrape = platform_to_scrape
        self.num_of_job_posts = number_of_job_posts


job_posts = 5
scrapper = Web_Scrapper("LinkedIn", job_posts)

print(scrapper.platform_to_scrape)
print(scrapper.num_of_job_posts)
