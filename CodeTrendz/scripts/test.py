from bs4 import BeautifulSoup
import requests

"""
https://uk.linkedin.com/jobs/view/graduate-software-engineer-at-tiptopjob-3735488680?refId=kPs1jZXLvXv6E0UecvcwJA%3D%3D&trackingId=%2Bj%2FtjgizlfyKYiRaacXWaw%3D%3D&trk=public_jobs_topcard-title
https://uk.linkedin.com/jobs/view/junior-java-developer-at-pepper-mill-3737609892?refId=u1xcaZ1PXKYa6pXOPMw9aQ%3D%3D&trackingId=AwZrzZ9Sg%2BLrfWSLfz%2FTeA%3D%3D&trk=public_jobs_topcard-title
"""


url = "https://uk.linkedin.com/jobs/view/junior-java-developer-at-pepper-mill-3737609892?refId=u1xcaZ1PXKYa6pXOPMw9aQ%3D%3D&trackingId=AwZrzZ9Sg%2BLrfWSLfz%2FTeA%3D%3D&trk=public_jobs_topcard-title"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    specific_a = soup.find(
        "h1",
        class_="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title",
    )

    specific_div = soup.find("div", class_="topcard__flavor-row")
    info_div = soup.find("div", class_="description__text description__text--rich")

    if specific_a:
        print(specific_a.text)
        print(specific_div.text)
        print(info_div.text)
    else:
        print("Nothing found")

else:
    print("Failde to retrieve data", response.status_code)
