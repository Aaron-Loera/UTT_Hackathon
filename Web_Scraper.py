import requests 
from bs4 import BeautifulSoup 

#rate my professor list of profs from uttyler 
url = "https://www.ratemyprofessors.com/search/professors/4171?q=*"

#bypass 403 error 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'
}

#soup object 
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

# need to seperate because the bad and good ratings have diff class 
goodRatings = soup.find_all("div", {"class": "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 ERCLc"})
badRatings = soup.find_all("div", {"class": "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cmIXQn"})

# combine both ratings
Ratings = goodRatings + badRatings
for e in Ratings:
    print(e)

# cast to floats 
Ratings = [float(x.text) for x in Ratings]
for e in Ratings:
    print(e)
  

