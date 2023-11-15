# cleaning job data and storing it in an csv
# so we can later perform the topic modelling on the data
from scrapper import Web_Scrapper

# https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=25

scrapper = Web_Scrapper(
    "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=25",
    5,
)

job_postings = []
scrapper.scrape()

for description in scrapper.job_description:
    data_obj = {"title": "", "description": description}
    job_postings.append(data_obj)

print(job_postings)
