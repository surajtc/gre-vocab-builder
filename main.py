import csv
import os

W  = '\033[0m'  # white (normal)
# R  = '\033[30;46;1m' # red
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

Path="Decks/"

Deck=None
Unknown=dict()

def print_line(char='-'):
    rows, columns = os.popen('stty size', 'r').read().split()
    print(char*int(columns))

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def choose_deck():
    clear_screen()
    print("inside choose deck")
    decks=os.listdir(Path)
    line=""
    
    for index,name in enumerate(decks, start=1):
        line=line+str(index)+". "+name.split(".")[0]+"\t\t"
        if index%3 == 0:
            print(line)
            line=""
        if index == len(decks):
            print(line)
    
    try:
        deck=int(input("Deck Number (1-"+str(len(decks))+") : "))-1
        print(decks[deck])
        global Deck
        Deck = decks[deck]

    except:
        print_line()
        print("Invalid Input! Try Again")
        input("Press Enter to continue")
        choose_deck()


def menu():
    option=input('Choose or Change Deck (Y/N):').lower()
    if option == "y":
        choose_deck()
    elif option == "n":
        exit()
    else:
        print(R+"Invalid Input! Try Again"+W)
        print_line()
        menu()

def review():
    global Unknown
    clear_screen()
    print_line("•")
    print("Reviewing " + Deck.split('.')[0] + " :")
    print_line("•")

    with open(Path+Deck) as csvfile:
        csvreader=csv.reader(csvfile)
        flag=None
        for index,row in enumerate(csvreader, start=1):
            print_line()
            print(B+row[0]+W)
            flag=input("Know This? (Y/n) : ")
            if len(flag) == 0 or flag.strip().lower() == 'y':
                print(G)
            else:
                Unknown[row[0]]=row[1]
                print(R)

            print("{:<10} ".format(row[0])+ W + "- " + row[1])
            print("{:<9}{:<2}{:<9}{:<2}{:<9}{:<2} ".format("Known: ",(index-len(Unknown)),"Unknown: ",len(Unknown),"Total: ",index))
            
    loop = len(Unknown)
    topop = list()
    while(loop):
        for word,meaning in Unknown.items():
            print_line()
            print(B+word+W)
            flag=input("Remember? (Y/n) : ")
            if len(flag) == 0 or flag.strip().lower() == 'y':
                topop.append(word)
                print(G)
            else:
                print(R)

            print("{:<10} ".format(word)+ W + "- " + meaning)
        for pop in topop:
            Unknown.pop(pop)

        topop.clear()
        loop = len(Unknown)
    
def main():
    clear_screen()
    print_line("•")
    print(O+"V O C A B U L A R Y  B U I L D E R".center(int(os.popen('stty size', 'r').read().split()[1]))+W)
    print_line("•")
    menu()
    review()
    global Deck, Unknown
    Deck = None
    Unknown.clear()
    main()

main()