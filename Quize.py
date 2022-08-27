# function goes here

from playsound import playsound
import question as Question
import os


def play():
    while (1):
        mylist = ["Science", "Music", "General Knowledge",
                  "History", "Technology", "Back"]
        print("\nSelect Categeory you want to play\n")
        for item in mylist:
            print(f"{mylist.index(item)+1}. {item}")
        select = int(input("\n SELECT : "))
        if (select == 1):
            Question("science", "1")
        elif (select == 2):
            Question("Music", "1")
        elif (select == 3):
            Question("General Knowledge", "1")
        elif (select == 4):
            Question("History", "1")
        elif (select == 5):
            Question("Technology", "1")
        elif (select == 6):
            break
        else:
            continue


def chooseLevel():
    pass


def Score():
    os.system("clear||cls")
    f = open('score.txt')
    print(f"\n\n\t\t\t Your High Score is {f.read()} \n")
    exit()


def quit():
    pass

# code start


while (1):
    os.system('cls||clear')
    print("\n\n\t\t\t\t\t Welcome to Quize game !")
    print("\t\t\t\t_______________________________________")
    print("\n_________________________________________________________________________________________________________")
    print("\n\t 1. Start the game")
    print("\n\t 2. Choose Level")
    print("\n\t 3. High Score")
    print("\n\t 4. Quite")
    print("\n_________________________________________________________________________________________________________")
    select = int(input("\n\t SELECT : "))

    if (select == 1):
        play()
    elif (select == 2):
        chooseLevel()
        print("\n\t....choosing")
    elif (select == 3):
        Score()
        print("\n\t....score list")
    elif (select == 4):
        print("\n\t\t\t\t\t\t\t Thanks for playing this game !\n\n")
        break
    else:
        continue
