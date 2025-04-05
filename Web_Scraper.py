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

# get ratings
# need to seperate because the bad and good ratings have diff class 
goodRatings = soup.find_all("div", {"class": "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 ERCLc"})
badRatings = soup.find_all("div", {"class": "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cmIXQn"})
# combine both ratings
ratings = goodRatings + badRatings
# cast to floats 
ratings = [float(x.text) for x in ratings]

#get names 
names = soup.find_all("div", {"class": "CardName__StyledCardName-sc-1gyrgim-0 gGdQEj"})
#cast to strings 
names = [str(x.text) for x in names]



#print ratings
for e in ratings:
    print(e)
    
#print names 
for e in names:
    print(e)

