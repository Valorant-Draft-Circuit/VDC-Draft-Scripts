from asyncore import read
import csv
from yaml import dump
franchises = dict()
picks = dict()

def populateFranchises(file):
    global franchises
    file = open(file)
    reader = csv.reader(file)
    header = []
    header = next(reader)
    for row in reader:
        if row[0] != "":
            if row[2] in franchises:
                franchises[row[2]][row[3]] = row[0]
            else:
                franchises[row[2]] = {}
                franchises[row[2]]["Franchise"] = row[1]
                franchises[row[2]][row[3]] = row[0]

    file.close()
    #print(franchises)
    
populateFranchises("VDCContracts-Teams.csv")


def tierPulls(file, tier):
    global franchises
    global picks
    file = open(file)
    reader = csv.reader(file)
    picks[tier] = {}
    header = next(reader)
    for row in reader:
        if row[0] == tier:
            picks[tier][row[2]+','+row[3]+','+row[1]] = {
                "Round":row[2],
                "Pick":row[3],
                "Overall Pick":row[1],
                "Player Selected":row[8],
                "Team":row[6],
                "Franchise":row[5],
                "GM":row[4]
            }
    file.close()
    #print(dump(picks, default_flow_style=False))

    

    return None


