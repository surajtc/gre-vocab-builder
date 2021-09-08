import csv
import os

W  = '\033[0m'  # white (normal)
R  = '\033[30;46;1m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

Deck_path="Decks/"

for deck in os.listdir(Deck_path):
    print(deck.split('.')[0])
Deck=os.listdir(Deck_path)[int(input("choose Deck No : "))-1]

with open(Deck_path+Deck) as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        print(R+row[0]+W+row[1]+W)