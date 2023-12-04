import spacy, csv
import pandas as pd
from scrapper import Web_Scrapper

nlp = spacy.load("en_core_web_sm")

web_scrapper = Web_Scrapper(
    "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3744358098&keywords=software%20developer&originalSubdomain=uk&start=150",
    5,
)
web_scrapper.scrape()

# Sample unstructured job posting text
job_posting_texts = web_scrapper.job_description

# Initialize lists to store extracted skills, programming languages, and education
skills = []
programming_languages = []
education = []

for text in job_posting_texts:
    doc = nlp(text)

    # Define keywords related to skills, programming languages, and education
    skill_keywords = ["skills", "abilities", "experience", "knowledge"]
    language_keywords = ["programming languages", "coding languages"]
    education_keywords = ["degree", "qualification", "education"]

    # Extract information using spaCy
    for sentence in doc.sents:
        # Extract skills
        if any(keyword in sentence.text.lower() for keyword in skill_keywords):
            for token in sentence:
                if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                    skills.append(token.text)

        # Extract programming languages
        if any(keyword in sentence.text.lower() for keyword in language_keywords):
            for token in sentence:
                if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                    programming_languages.append(token.text)

        # Extract education requirements
        if any(keyword in sentence.text.lower() for keyword in education_keywords):
            for token in sentence:
                if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                    education.append(token.text)

    # Remove duplicates and display the extracted information
    skills = list(set(skills))
    programming_languages = list(set(programming_languages))
    education = list(set(education))

    print("Extracted Skills:", skills)
    print("Extracted Programming Languages:", programming_languages)
    print("Extracted Education Requirements:", education)


file_path = "C:\\Users\\disco\\Desktop\\Programming\Portfolio\\CodeTrendzRepo\\CodeTrendz\\scripts\\data\\skills_data.csv"

# Saving the extracted information to a CSV file
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write headers
    writer.writerow(["Skills", "Programming Languages", "Education Requirements"])

    if len(skills) != 0 or len(programming_languages) != 0 or len(education) != 0:
        # Combine lists into rows to ensure each row has all data
        max_length = max(len(skills), len(programming_languages), len(education))
        for i in range(max_length):
            skill = skills[i] if i < len(skills) else ""
            lang = programming_languages[i] if i < len(programming_languages) else ""
            edu = education[i] if i < len(education) else ""
            writer.writerow([skill, lang, edu])

    print("Data saved to 'skills_data.csv'")

data = pd.read_csv(file_path)

# Count occurrences of each column
skill_counts = data["Skills"].value_counts()
lang_counts = data["Programming Languages"].value_counts()
edu_counts = data["Education Requirements"].value_counts()

top_skills = skill_counts.head(10)
