import requests 
from bs4 import BeautifulSoup 
import re
import time
import csv

base_url = "https://www.ratemyprofessors.com/search/professors/4171?q=*&page={}"
page_num = 1
all_data = []
seen_names = set()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'
}

while True:
    url = base_url.format(page_num)
    print(f"Scraping page {page_num}...")
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    cards = soup.find_all("div", class_="TeacherCard__InfoRatingWrapper-syjs0d-3 kAxNBg")
    if not cards:
        print("No cards found, ending loop.")
        break  # End loop if no cards

    page_data = []
    for card in cards:
        name_tag = card.find("div", class_="CardName__StyledCardName-sc-1gyrgim-0 gGdQEj")
        name = name_tag.text.strip() if name_tag else "No Name"

        rating_tag = card.find("div", class_=re.compile("CardNumRating__CardNumRatingNumber"))
        rating = float(rating_tag.text.strip()) if rating_tag else None

        department_tag = card.find("div", class_="CardSchool__Department-sc-19lmz2k-0 hRJPlj")
        department = department_tag.text.strip() if department_tag else "No Dept"

        numRatings_tag = card.find("div", class_="CardNumRating__CardNumRatingCount-sc-17t4b9u-3 ckSFVh")
        num_ratings = numRatings_tag.text.strip() if numRatings_tag else "No Ratings"

        feedback_tags = card.find_all("div", class_="CardFeedback__CardFeedbackNumber-lq6nix-2 iHkSBk")
        retake = feedback_tags[0].text.strip() if len(feedback_tags) > 0 else "No % given"
        difficulty = feedback_tags[1].text.strip() if len(feedback_tags) > 1 else "No difficulty given"

        page_data.append((name, rating, department, num_ratings, retake, difficulty))

    # Check for duplicate data; if duplicate detected, break out
    if page_data:
        first_name = page_data[0][0]
        if first_name in seen_names:
            print("Duplicate data detected, ending loop.")
            break

    for entry in page_data:
        seen_names.add(entry[0])
        all_data.append(entry)

    page_num += 1
    time.sleep(1)  # Pause between pages

# Write the data to a CSV file
with open("uttyler_professors.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["Name", "Rating", "Department", "Num Ratings", "Retake %", "Difficulty"])
    # Write all data rows
    writer.writerows(all_data)

print("Data saved to uttyler_professors.csv")
