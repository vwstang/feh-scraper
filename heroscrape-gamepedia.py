# Import libraries
import requests
from bs4 import BeautifulSoup
import time
import json


def listStats(stringStats):
  if len(stringStats) >= 5:
    result = list(map(int,stringStats.split("/")))
  else:
    result = list(int(stringStats))
  return result


def getStats(statTable):
  stats = {}
  currentRarity = "0"
  for i,tblData in enumerate(statTable):
    if i % 7 == 0:
      currentRarity = str(int(tblData.contents[0].encode("utf-8")))
      stats.update({("rarity" + currentRarity): {}})
    elif i % 7 == 1:
      stats["rarity" + currentRarity].update({"HP": listStats(str(tblData.string))})
    elif i % 7 == 2:
      stats["rarity" + currentRarity].update({"ATK": listStats(str(tblData.string))})
    elif i % 7 == 3:
      stats["rarity" + currentRarity].update({"SPD": listStats(str(tblData.string))})
    elif i % 7 == 4:
      stats["rarity" + currentRarity].update({"DEF": listStats(str(tblData.string))})
    elif i % 7 == 5:
      stats["rarity" + currentRarity].update({"RES": listStats(str(tblData.string))})
    elif i % 7 == 6:
      pass
    else:
      print("ERROR OVERFLOW: Table has more than 7 columns.")
  return stats


def grabData():
  # Make the soup from Fire Emblem Gamepedia
  url = "https://feheroes.gamepedia.com/Abel:_The_Panther"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  heroData = {}
  L1Stats = getStats(soup.find("span",{"id": "Level_1_stats"}).parent.next_sibling.find_all("td"))
  L40Stats = getStats(soup.find("span",{"id": "Level_40_stats"}).parent.next_sibling.find_all("td"))
  heroData.update({"lvl1stats": L1Stats,
                   "lvl40stats": L40Stats})
  return heroData


def main():
  sampleHero = {"title": "The Panther",
                "gpedia_link": "https://feheroes.gamepedia.com/Abel:_The_Panther"}
  heroData = grabData()
  sampleHero.update(heroData)
  with open("test-abel.json","w") as outfile:
    json.dump(sampleHero,outfile)

main()
