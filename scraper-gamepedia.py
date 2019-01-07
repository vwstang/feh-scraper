# Import libraries
import requests
import json
from bs4 import BeautifulSoup


def grabTags():
  # # LOCAL VERSION
  # file = r"H:\Development\feh-scraper\dev-assets\190105\fehgp_heroes.html"
  # soup = BeautifulSoup(open(file,encoding="utf8"),"html.parser")

  # Make the soup from Fire Emblem Gamepedia
  url = "https://feheroes.gamepedia.com/Hero_list"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  savedTags = soup("tr",{"class": "hero-filter-element"})
  return savedTags


def parseTags(tags):
  heroes = {}
  for heroTag in tags:
    hero = {}
    heroName, heroTitle = heroTag.find("td").next_sibling.find("a").text.split(": ")
    heroKey = heroName.lower() + "_" + "".join(heroTitle.lower().split(" "))
    heroGPLink = "https://feheroes.gamepedia.com" + heroTag.find("td").next_sibling.find("a")["href"]
    hero.update({
      "name": heroName,
      "title": heroTitle,
      "gpedia_link": heroGPLink
    })
    heroes[heroKey] = hero
  return heroes


def main():
  savedTags = grabTags()
  heroes = parseTags(savedTags)
  with open("feh-heroes.json","w") as outfile:
    json.dump(heroes,outfile)


main()
