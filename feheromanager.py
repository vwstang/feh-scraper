# Import libraries
import json
import build


def dbComparer(currDB,updtDB):
  updtHeroes = {k:v for k,v in updtDB.items() if k not in currDB or v != currDB[k]}
  print(updtHeroes)


def comparing():
  with open("./tests/currentdb.json") as file:
    currentHeroList = json.load(file)
  with open("./tests/newupdates.json") as file:
    updatedHeroList = json.load(file)
  dbComparer(currentHeroList,updatedHeroList)


def writeToJSON(dictionary, name):
  filename = str(name) + ".json"
  with open(filename,"w") as outfile:
    json.dump(dictionary,outfile)
  print("Output to " + filename + " completed.")


def main():
  welcomemsg = """
******************************************
FIRE EMBLEM HEROES - HERO DATABASE MANAGER
******************************************

Available commands:

build     build new database


"""
  print(welcomemsg)
  task = input("Your command? ").lower()
  print(task)

main()
