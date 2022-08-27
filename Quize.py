# function goes here

from playsound import playsound
import os


def Question(categeory, level):
    myscore = 0
    os.system('clear')
    print(f"\n\t\t\t\t\tQuestion of {categeory} are below :")
    print("_________________________________________________________________________________________________________\n\n")
    # question of science
    if (categeory == 'science'):
        myscore = 0
        print("\t1. Who is the father of Science ?\n")
        print("\t A. Galileo Galilei \t\t B. charles babbage \n\t C. Sir isac newton \t\t D. Michal Fraday")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print('''\n\t2. Who Discovered "Theory of Relativity" ?\n''')
        print(
            "\t A. Gram bell \t\t B. Willam brother \n\t C. Albert Einstien \t D. Stephen hawking")
        answer = str(input("\n\t : "))
        if (answer == 'C'):
            myscore = myscore+1
        print("\n\t3. What is the most abundant gas in the Earth's atmosphere ?\n")
        print(
            "\t A. Nitrogen \t\t B. Oxygen \n\t C. Methan \t\t D. L.p.g")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t4. Which Apollo moon mission was the first to carry a lunar rover ?\n")
        print(
            "\t A. Apollo 11 \t\t B. Apollo 14 \n\t C. Apollo 10 \t\t D. Apollo 15")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print("\n\t5. How many teeth does an adult human have ?\n")
        print(
            "\t A. 28 \t\t B. 34 \n\t C. 32 \t\t D. 20")
        answer = str(input("\n\t : "))
        if (answer == 'C'):
            myscore = myscore+1
        print("\t6. What does DNA stand for?\n")
        print("\t A. Deoxyribonuclear acid \t\t B. Deoxyribonucleic acid \n\t C. Deoxoribonuclear acid \t\t D. Denatured ribonucleic acid")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t7. The concept of gravity was discovered by which famous physicist ?\n")
        print(
            "\t A. Sir Isaac Newton \t\t B. Marie Sklodowska-Curie \n\t C. Henri Becquerel \t\t D. Thomas Edison")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t8. How many vertebrae does the average human possess ?\n")
        print(
            "\t A. 33 \t\t B. 11 \n\t C. 89 \t\t D. 54")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t9. Humans and chimpanzees share roughly how much DNA ?\n")
        print(
            "\t A. 66% \t\t B. 30% \n\t C. 86% \t\t D. 98%")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print("\n\t10. At what temperature are Celsius and Fahrenheit equal ?\n")
        print(
            "\t A. -40 \t B.  34 \n\t C.  60 \t D. -20")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t11. What is the biggest planet in our solar system ?\n")
        print(
            "\t A. Earth \t\t B. Mars \n\t C. Venus \t\t D. Jupiter")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print(f"\n\n\t\t Your total is {myscore} out of 11 ")
    elif (categeory == 'Music'):
        myscore = 0
        print("\t1. Who was the lead singer of Nirvana ?\n")
        print("\t A. Dave Grohl \t\t B. Chad Channing \n\t C. Krist Novoselic \t D. Kurt Cobain")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print("\n\t2. What colour was the Little Rooster according to the title of a Rolling Stones hit ?\n")
        print("\t A. Red \t\t B. Brown \n\t C. White \t\t D. Yellow")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t3. Who introduce Hiphop music in Nepal ?\n")
        print("\t A. Sacar \t\t B. Yamma Buddha  \n\t C. Grish Khatiwada \t D. Vten")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t4. Who was the vocalist of Tribal rain Band ?\n")
        print(
            "\t A. Yabesh Thapa \t B. Prawes Lama \n\t C. Rahul rai \t\t D. Kenneth Adhikari")
        answer = str(input("\n\t : "))
        if (answer == 'C'):
            myscore = myscore+1
        print("\n\t5. Name of singer who is suffering from Ramsay hunt syndrome ?\n")
        print("\t A. Xxx tentacion \t\t B. Justin Bibber \n\t C. Salena Gomez \t\t D. Tylor swift")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t6. Who is the stoner singer popular in Hiphop ?\n")
        print("\n\t A. Bob marley \t\t B. Wiz kalifa \n\t C. Snoop dog \t\t D. Dj khalid")
        answer = str(input("\n\t : "))
        if (answer == 'C'):
            myscore = myscore+1
        print("\n\t7. Name of singer who was the 18 runner-ups in American Idol ?\n")
        print(
            "\t A. Chirs brown \t\t B. Jonny West \n\t C. Arthur Gunn \t\t D. Dillon James")
        answer = str(input("\n\t : "))
        if (answer == 'C'):
            myscore = myscore+1
        print("\n\t8. Which Queen song has the lyrics “Is this the real life? Is this \n\t   just fantasy?” ?\n")
        print(
            "\t A. Kool & the Gang \t\t B. bohemian rhapsody \n\t C. Tony Bennett \t\t D. Billie Eilish")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t9. Which country is Gangnam Style singer PSY from ?\n")
        print("\t A. Canada \t\t B. North korea \n\t C. South Korea \t D. Germany")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print("\t10. In which year was Bruno Mars born ?\n")
        print("\n\t A. 1990 \t\t B. 1985 \n\t C. 1997 \t\t D. 1987")
        answer = str(input("\n\t : "))
        if (answer == 'A'):
            myscore = myscore+1
        print("\n\t11. How many members are in the K-Pop group Twice?\n")
        print("\t A. 2 \t\t B. 4 \n\t C. 6 \t\t D. 8")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t12. What is DJ Marshmello's real name ?\n")
        print("\t A. Brendon Urie \t\t B. Marshall Mellow \n\t C. Patrick Stump \t\t D. Cristopher Comstock")
        answer = str(input("\n\t : "))
        if (answer == 'B'):
            myscore = myscore+1
        print("\n\t13. Which member of One Direction left the group in 2015 ?\n")
        print("\t A. Louis Tomlinson \t\t B. Liam Payne \n\t C. Harry Styles \t\t D. Zayn Malik")
        answer = str(input("\n\t : "))
        if (answer == 'D'):
            myscore = myscore+1
        print(f"\n\t\t Your total is {myscore} out of 13 \n")
    elif (categeory == 'General Knowledge'):
        print("\n Under Developing")
    elif (categeory == 'History'):
        print("\n Under Developing")
    elif (categeory == 'Technology'):
        print("\n Under Developing")


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
    pass


def quit():
    pass

# code start


while (1):
    os.system('clear')
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
        print("\n\t\t\t\t\t\t\t Thanks for using !\n\n")
        break
    else:
        continue
