import requests
from pprint import pprint
from bs4 import BeautifulSoup

def getHeroList():
  url = "https://feheroes.gamepedia.com/Hero_list"
  response = requests.get(url)
  rawHTML = BeautifulSoup(response.text, "html.parser")
  lstHeroHTML = rawHTML("tr",{"class": "hero-filter-element"})
  print("Found " + str(len(lstHeroHTML)) + " heroes on Gamepedia.")
  print("Now building hero database.")
  dctHeroes = {}
  for heroTag in lstHeroHTML:
    dctHero = {}
    heroName, heroTitle = heroTag.find("td").next_sibling.find("a").text.split(": ")
    heroKey = heroName.lower() + "_" + "".join(heroTitle.lower().split(" "))
    heroGPediaLink = "https://feheroes.gamepedia.com" + heroTag.find("td").next_sibling.find("a")["href"]
    dctHero.update({
      "name": heroName,
      "title": heroTitle,
      "gpedia": heroGPediaLink
    })
    dctHeroes[heroKey] = dctHero
