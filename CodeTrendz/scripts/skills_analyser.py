import spacy

nlp = spacy.load("en_core_web_sm")

# Sample unstructured job posting text
job_posting_text = """
23WD70770

Location: Birmingham, UK

Application deadline: 31st December 2023

Position Overview

Autodesk provides engineers with the software they need to imagine, design, and make anything, across every industry you can think of. If you feel excited by the opportunity to wake up every morning, knowing that what you do has a direct impact on shaping our world, then come and join us at Autodesk!

We are looking for undergraduates that have the talent and ambition to become accomplished software engineers. During your placement with us we will ensure that you are challenged and given every opportunity to grow your knowledge and experience with the support of an experienced Autodesk developer.

Summer Interns will get the opportunity to work in an Agile Scrum team, made up of 5-8 experienced software engineers, as part of a larger software development team working on Fusion 360 and reporting to our Engineering Director. While one-year Placements will rotate through four teams in total. The software we develop is both challenging and rewarding - from writing toolpath algorithms in C++ to developing web components in TypeScript - so we will ensure you get the training and support to help you grow and develop your skills during your time with us.

We offer paid leave, flexible working, private medical cover, plus a new starter stipend. We also encourage our staff to get to know each other, in and out of the office, with subsidised social activities.

Responsibilities

    Work on real commercial development projects mentored by experienced Autodesk developers
    Gain experience of working on large team-based software development
    Learn how to write robust commercial software
    Gain knowledge of the commercial development processes used at Autodesk
    Engage with Agile and Scrum working practices.
    Use source control and Continuous Integration platforms such as GitHub and Jenkins

Minimum Qualifications

    Minimum 120 UCAS points and predicted 1st or 2:1 degree

What Are We Looking For

    Bright Computer Science, Maths, Physics, and Engineering students for both our eleven-week summer internships and our one-year placements starting summer 2024
    Programming experience at some level, ideally using a C-style language (eg. C, C++, Java, C#), is desirable

Learn More

About Autodesk

Welcome to Autodesk! Amazing things are created every day with our software – from the greenest buildings and cleanest cars to the smartest factories and biggest hit movies. We help innovators turn their ideas into reality, transforming not only how things are made, but what can be made.

We take great pride in our culture here at Autodesk – our Culture Code is at the core of everything we do. Our values and ways of working help our people thrive and realize their potential, which leads to even better outcomes for our customers.

When you’re an Autodesker, you can be your whole, authentic self and do meaningful work that helps build a better future for all. Ready to shape the world and your future? Join us!

Salary transparency

Salary is one part of Autodesk’s competitive compensation package. Offers are based on the candidate’s experience, educational level, and geographic location.

Diversity & Belonging

We take pride in cultivating a culture of belonging and an equitable workplace where everyone can thrive. Learn more here: https://www.autodesk.com/company/diversity-and-belonging
"""

doc = nlp(job_posting_text)

# Initialize lists to store extracted skills, programming languages, and education
skills = []
programming_languages = []
education = []

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
