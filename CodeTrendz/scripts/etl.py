# cleaning job data and storing it in an csv
# so we can later perform the topic modelling on the data
from scrapper import Web_Scrapper
from topic_modelling import TopicModelling
import csv

# https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=25

scrapper = Web_Scrapper(
    "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=100",
    5,
)

job_postings = []
scrapper.scrape()

cleaned_job_descriptions = [
    "\n".join([line for line in s.splitlines() if line.strip()])
    for s in scrapper.job_description
]

for description in cleaned_job_descriptions:
    data_obj = {"title": "", "description": description}
    job_postings.append(data_obj)


# csv_file_name = "./data/linkedin_data.csv"
# field_names = ["title", "description"]

# with open(csv_file_name, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=field_names)

#     writer.writeheader()
#     writer.writerows(job_postings)


modelling = TopicModelling(job_postings)
modelling.start_modelling()
