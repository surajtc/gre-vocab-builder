import csv
import os

# R  = '\033[30;46;1m' # fg;bg;bold

BOLD = '\033[1m'  # bold
W    = '\033[0m'  # white | default
R    = '\033[31m' # red
G    = '\033[32m' # green
O    = '\033[33m' # orange
B    = '\033[34m' # blue
P    = '\033[35m' # purple

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

# MAIN MENU
def menu():
    option=input(B+'Choose or Change Deck (Y/n):'+W)
    if len(option) == 0 or option.strip().lower() == "y":
        choose_deck()
    elif option.strip().lower() == "n":
        exit()
    else:
        print(R+"Invalid Input! Try Again"+W)
        print_line()
        menu()

# CHOOSING DECK
def choose_deck():
    clear_screen()
    print_line("•")
    print(P+BOLD+"CHOOSE ANY ONE OF THE DECKS BELOW :"+W)
    print_line("•")
    print(O)
    decks=os.listdir(Path)
    line=""
    
    for index,name in enumerate(decks, start=1):
        line=line+str(index)+". "+name.split(".")[0]+"\t\t"
        if index%3 == 0:
            print(line)
            line=""
        if index == len(decks):
            print(line+W)
    
    try:
        print_line()
        deck=int(input(B+"Deck Number "+W+"(1-"+str(len(decks))+") : "))-1
        print(decks[deck])
        global Deck
        Deck = decks[deck]

    except:
        print_line()
        print(R+"Invalid Input! Try Again\n"+W)
        input(B+"PRESS <"+O+"Enter"+B+"> TO CONTINUE "+W)
        choose_deck()

# REVIEW WORDS
def review():
    global Unknown
    clear_screen()
    print_line("•")
    print(P+BOLD+"REVIEWING " + Deck.split('.')[0] + " :"+W)
    print_line("•")

    with open(Path+Deck) as csvfile:
        csvreader=csv.reader(csvfile)
        flag=None
        for index,row in enumerate(csvreader, start=1):
            print(O+BOLD+row[0].capitalize()+W)
            print()
            flag=input(B+"Know This? (Y/n) :"+W)
            if len(flag) == 0 or flag.strip().lower() == 'y':
                print(G+BOLD)
            else:
                Unknown[row[0]]=row[1]
                print(R+BOLD)

            print("{:<10} ".format(row[0])+ W + BOLD + "- " + row[1]+W+B)
            print_line()
            print(P+"{:<9}{:<2} {:<9}{:<2} {:<9}{:<2} ".format("Known: ",(index-len(Unknown)),"Unknown: ",len(Unknown),"Total: ",index)+W)
            print_line("•")
            
    input(B+"PRESS <"+O+"Enter"+B+"> TO CONTINUE "+W)
            
    loop = len(Unknown)
    topop = list()
    while(loop):
        clear_screen()
        print_line("•")
        print(P+BOLD+"REVIEWING "+O+str(loop)+P+" UNKNOWN WORDS IN " + Deck.split('.')[0] + " :"+W)
        print_line("•")
        for word,meaning in Unknown.items():
            print(O+BOLD+word.capitalize() +W)
            print()
            flag=input(B+"Remember? (Y/n) :"+W)
            if len(flag) == 0 or flag.strip().lower() == 'y':
                topop.append(word)
                print(G+BOLD)
            else:
                print(R+BOLD)

            print("{:<10} ".format(word)+ W + BOLD +"- " + meaning+W)
            print()
            print_line("•")
        for pop in topop:
            Unknown.pop(pop)

        topop.clear()
        loop = len(Unknown)
        input(B+"PRESS <"+O+"Enter"+B+"> TO CONTINUE "+W)


# DRIVER FUNCTION
def main():
    clear_screen()
    print_line("•")
    print(P+BOLD+"V O C A B U L A R Y  B U I L D E R".center(int(os.popen('stty size', 'r').read().split()[1]))+W)
    print_line("•")
    menu()
    review()
    global Deck, Unknown
    Deck = None
    Unknown.clear()
    main()

main()