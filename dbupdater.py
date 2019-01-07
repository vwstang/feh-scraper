import json
from pprint import pprint


def dbComparer(currDB,updtDB):
  updtHeroes = {k:v for k,v in updtDB.items() if k not in currDB or v != currDB[k]}
  pprint(updtHeroes)


def main():
  with open("./tests/currentdb.json") as file:
    currentHeroList = json.load(file)
  with open("./tests/newupdates.json") as file:
    updatedHeroList = json.load(file)
  dbComparer(currentHeroList,updatedHeroList)

main()
