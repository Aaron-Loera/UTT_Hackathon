import requests 
from bs4 import BeautifulSoup 
import re



#rate my professor list of profs from uttyler 
url = "https://www.ratemyprofessors.com/search/professors/4171?q=*"

#bypass 403 error 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'
}

#soup object 
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

#each profs tuple from url
cards = soup.find_all("div", class_="TeacherCard__InfoRatingWrapper-syjs0d-3 kAxNBg")

#new list
data = []

for card in cards:
    # get names 
    name_tag = card.find("div", class_="CardName__StyledCardName-sc-1gyrgim-0 gGdQEj")
    name = name_tag.text.strip() if name_tag else "No Name"
    
    # Get the rating (good or bad)
    rating_tag = card.find("div", class_=re.compile("CardNumRating__CardNumRatingNumber"))
    rating = float(rating_tag.text.strip()) if rating_tag else None

    # get department
    department_tag = card.find("div", class_="CardSchool__Department-sc-19lmz2k-0 hRJPlj")
    department = department_tag.text.strip() if department_tag else "No Name"

    #get number of reviews 
    numRatings_tag = card.find("div", class_=("CardNumRating__CardNumRatingCount-sc-17t4b9u-3 ckSFVh"))
    department = numRatings_tag.text.strip() if numRatings_tag else "No Ratings"

    # get feedback numbers
    feedback_tags = card.find_all("div", class_="CardFeedback__CardFeedbackNumber-lq6nix-2 iHkSBk")
    retake = feedback_tags[0].text.strip() if len(feedback_tags) > 0 else "No % given"
    difficulty = feedback_tags[1].text.strip() if len(feedback_tags) > 1 else "No difficulty given"







    data.append((name, rating, department, rating, retake, difficulty))

for name, rating, department, rating, retake, difficulty in data:
    print(f"{name}:  {rating}, {department}, {rating}, {retake}, {difficulty}")

