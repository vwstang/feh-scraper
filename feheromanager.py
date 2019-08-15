# Fire Emblem Heroes - Hero Database Manager
# Main App Module
# 
# v0.0.3
# 
# Controls tasks to run based on user input

# Import module dependencies
from pprint import pprint
import time
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


def writeToJSON(dictionary,name):
  filename = str(name) + ".json"
  with open(filename,"w") as outfile:
    json.dump(dictionary,outfile)
  print("Output to " + filename + " complete")


def runBuild():
  heroList = build.getHeroList()
  print("Delay between server requests set to 1 second")
  estOpTime = int(len(sorted(heroList))/60)
  if estOpTime == 1:
    print("Please wait - this operation may take over a minute")
  elif estOpTime > 1:
    print("Please wait - this operation may take over %s minutes"%(estOpTime))
  for hero in heroList:
    time.sleep(1)
    print("Fetching data for " + hero,end="",flush=True)
    heroList[hero].update(build.getHeroData(heroList[hero]["gpedia"]))
    print("Done")
  writeToJSON(heroList,"herodb")
  print("Task complete")


def runQuickUpd():
  # with open("herodb.json") as file:
  #   currentHeroList = json.load(file)
  print("I'm in runQuickUpd!")


def runFullUpd():
  print("I'm in runFullUpd!")


def runExit():
  print("Exiting manager")


def runDebug():
  print("I'm in the (hidden) runDebug!")


def main():
  welcomemsg = """
******************************************************
***** FIRE EMBLEM HEROES - HERO DATABASE MANAGER *****
******************************************************

v0.0.2

=== Available tasks ===

build       build new database
q-update    quickly update database for new heroes
f-update    fully check database for new heroes and changes to existing heroes
exit        don't run any tasks and exit

===
"""
  task = {
    "build": runBuild,
    "q-update": runQuickUpd,
    "f-update": runFullUpd,
    "exit": runExit,
    "debug": runDebug
  }
  print(welcomemsg)
  userTask = input("What task would you like to run? ").lower()
  try:
    task[userTask]()
  except KeyError:
    print("INVALID COMMAND: Please rerun the script and enter a valid command")

main()