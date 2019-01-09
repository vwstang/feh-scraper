# Build Module
# 
# This module contains all web scraping functions used by the manager in performing tasks to build and update the JSON database

# Import module dependencies
import requests
from bs4 import BeautifulSoup


def getHeroList():
  url = "https://feheroes.gamepedia.com/Hero_list"
  response = requests.get(url)
  rawHTML = BeautifulSoup(response.text, "html.parser")
  lstHeroHTML = rawHTML("tr",{"class": "hero-filter-element"})
  print("Found " + str(len(lstHeroHTML)) + " heroes on Gamepedia")
  print("Building hero database")
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
  print("Hero database build complete")
  return dctHeroes


def listStats(stringStats):
  if len(stringStats) >= 5:
    result = list(map(int,stringStats.split("/")))
  else:
    result = [int(stringStats)]
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
      print("OVERFLOW ERROR: Table has more than 7 columns.")
  return stats


def getSkills(skillTables):
  skills = []
  for skillTypes in skillTables:
    for i, skillRow in enumerate(skillTypes("tr")):
      if i > 0:
        skills.append("".join(skillRow.find("a").string.lower().split(" ")))
  return skills


def getHeroData(url):
  response = requests.get(url)
  print(".",end="",flush=True)
  soup = BeautifulSoup(response.text, "html.parser")
  print(".",end="",flush=True)
  heroData = {}
  lvl1Stats = getStats(soup.find("span",{"id": "Level_1_stats"}).parent.next_sibling.find_all("td"))
  lvl40Stats = getStats(soup.find("span",{"id": "Level_40_stats"}).parent.next_sibling.find_all("td"))
  defaultSkills = getSkills(soup("table",{"class": "skills-table"}))
  print(".",end="",flush=True)
  heroData.update({"lvl1stats": lvl1Stats,
                   "lvl40stats": lvl40Stats,
                   "defaultskills": defaultSkills})
  return heroData