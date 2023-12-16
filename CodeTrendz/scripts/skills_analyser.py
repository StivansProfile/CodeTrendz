import spacy, csv
import pandas as pd
from scrapper import Web_Scrapper

languages_technologies = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "PHP",
    "Ruby",
    "Swift",
    "TypeScript",
    "Kotlin",
    "Go",
    "Rust",
    "Perl",
    "Objective-C",
    "Scala",
    "HTML/CSS",
    "SQL",
    "Shell",
    "Assembly",
    "R",
    "Matlab",
    "Dart",
    "Haskell",
    "Groovy",
    "Lua",
    "VB.NET",
    "VBA",
    "COBOL",
    "Fortran",
    "Ada",
    "Lisp",
    "Scheme",
    "Prolog",
    "Smalltalk",
    "Erlang",
    "Clojure",
    "F#",
    "Verilog",
    "VHDL",
    "LabVIEW",
    "React",
    "Angular",
    "Vue.js",
    "Node.js",
    "Express.js",
    "Django",
    "Flask",
    "Ruby on Rails",
    "Spring Framework",
    "ASP.NET",
    "Laravel",
    "Symfony",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Spark",
    "Hadoop",
    "MongoDB",
    "MySQL",
    "PostgreSQL",
    "Redis",
    "GitHub",
    "HTML",
    "CSS",
    "HTML5",
    "CSS3",
    "jQuery",
    "Git",
    "TypeScript",
    "GitLab",
    "Express",
    "Express.js",
    "Redux",
    "Typescript",
    "AWS",
    "ASP",
    "ASP.Net",
    ".Net",
    "API",
    "React.js",
    "Reddis",
    "APIs",
    "AJAX",
    "Ajax",
    "Next.js",
    "Kubernetes",
    "SEO",
    "Figma",
    "WordPress",
    "UX",
    "UI",
    "Rust",
    "Go",
    "GoLang",
]
file_path = "C:\\Users\\disco\\Desktop\\Programming\Portfolio\\CodeTrendzRepo\\CodeTrendz\\scripts\\data\\skills_data.csv"


def scrape_and_store_data():
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

    # Extraction of relevant information
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
                lang = (
                    programming_languages[i] if i < len(programming_languages) else ""
                )
                edu = education[i] if i < len(education) else ""
                writer.writerow([skill, lang, edu])

        print("Data saved to 'skills_data.csv'")


scrape_and_store_data()

df = pd.read_csv(file_path)

# Initialize a dictionary to store occurrences of technologies
tech_occurrences = {tech: 0 for tech in languages_technologies}


# Function to find and count occurrences of technologies in a string
def find_technologies(text):
    if isinstance(text, str):  # Check if the value is a string
        for tech in languages_technologies:
            if tech in text:
                tech_occurrences[tech] += 1


# Apply the function to every cell in the dataframe
df.applymap(find_technologies)

# Get the duplicates
duplicates = {tech: count for tech, count in tech_occurrences.items() if count > 1}

# Print occurrences and duplicates
print("Occurrences of technologies:")
for tech, count in tech_occurrences.items():
    if count > 0:
        print(f"{tech}: {count} occurrences")

print("\nDuplicates:")
print(duplicates)
