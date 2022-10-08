# in this game you have to answer the question, that give you some point :)
# start ^_^

import random

want_play = input("do you want play : ")
if want_play.lower().strip() != "yes":
    quit()
print(" \n \nchose what the game you need to blay \n GAME 1 | GAME 2 | GMAE 3\n \n")

chose_game = input()
if chose_game.lower().strip() == "game 1" or chose_game.strip() == "1":
# gmae 1
    print(" \n--Game 1--")
    start = ""
    tries = 5
    while start.lower().strip() != "start":
        print(" \nprint 'start' to lunch the game :")
        start = input()
    else:
        print(" \nFirst question : ")

    print("What's the name of my Channel ?")
    channel = input()
    if channel.lower().strip() == "rd1 ff" or channel.lower().strip() == "rd1":
        print(" \nthat's right, YOU WIN!!!\n ")
        point1 = 10
    else:
        print(" \nthat's false, YOU LOSE!!!\n ")
        point1 = 0

    print(" \nsecond question : ")
    print("How many subscribers I have ?")
    sub = int(input())
    if 250 <= sub <= 260:
        print(" \nthat's right, YOU WIN!!!\n ")
        point2 = 10
    else:
        print(" \nthat's false, YOU LOSE!!!\n ")
        point2 = 0

    print(" \nthird question : ")
    print("what's the best VD in my chnnael ?")
    BestVD = input()
    if BestVD.lower().strip() == "for you" or BestVD.lower().strip() == "for you(free fire montage)":
        print(" \nthat's right, YOU WIN!!!")
        point3 = 10
    else:
        print(" \nthat's false, YOU LOSE!!!")
        point3 = 0

    result = ""
    while result.lower().strip() != "result":
        print(" \n \nPrint 'result' to check your score")
        result = input()
    else:
        print(" \nyour score in -game 3- is :",
              int(point1+point2+point3), "points")
# game 2
elif chose_game.lower().strip() == "game 2" or chose_game.strip() == "2":
    print(" \n \n--Game 2--\n \n ")
    correct_num = random.randint(1, 9)
    mohawalat = 3
    Omohawalat = 0
    guess = ""
    out = False
    guesspoint = 30

    print("in this game you have to guess the correct number")
    print(" 0 < correct num < 10")
    print("-- your tries now is : 3 --")

    while guess != correct_num and not out:
        if Omohawalat < mohawalat:
            guess = int(input("Enter your guess\n=>"))
            mohawalat -= 1
            if Omohawalat < mohawalat and guess != correct_num:
                print("\nthat's false !\n-- your tries now is :",
                      mohawalat, "--")
                if correct_num < guess:
                    print("the correct number is smallest")
                elif correct_num > guess:
                    print("the correct numbre is biggest")
                guesspoint -= 10
            if mohawalat == 0 and guess != correct_num:
                print("\nthat's false !\n-- your tries is finished --")
                guesspoint = 0
        else:
            out = True
    if out:
        print("all nembers you guess is false, YOU LOSE !!!")
    else:
        print(correct_num, "is the correct number,so YOU WIN !!!")

    result = ""
    while result.lower().strip() != "result":
        print(" \n \nPrint 'result' to check your score")
        result = input()
    else:
        print(" \nyour score in -game 2- is :", int(guesspoint), "points")
elif chose_game.lower().strip() == "game 3" or chose_game.strip() == "3":
# game 3
    print(" \n \n--Game 3--\n \n ")
    cal1 = str(374+839)
    cal2 = str(243-84)
    cal3 = str(267*2)
    one = ""
    two = ""
    three = ""
    tries = 3
    point1 = 0
    point2 = 0
    point3 = 0

    print("In this game you have to calculate three calculations \nyou have 3 tries")
    while one != cal1:
        one = str(input("-first: 374+839 = "))
        if one != cal1:
            tries -= 1
            if tries == 1:
                print("last trie")
            elif tries == 0:
                print("your tries is finished, YOU LOSE !!!")
                point1 = 0
                break
            else:
                print(f"{tries} tries left")
        else:
            print("that's wright, YOU WIN !!!")
            point1 = 10
            tries = 3
            while two != cal2:
                two = str(input("\n-second: 243-84 = "))
                if two != cal2:
                    tries -= 1
                    if tries == 1:
                        print("last trie")
                    elif tries == 0:
                        print("your tries is finished, YOU LOSE !!!")
                        point2 = 0
                        break
                    else:
                        print(f"{tries} tries left")
                else:
                    print("that's wright, YOU WIN !!!")
                    point2 = 10
                    tries = 3
                    while three != cal3:
                        three = str(input("\n-third: 267*2 = "))
                        if three != cal3:
                            tries -= 1
                            if tries == 1:
                                print("last trie")
                            elif tries == 0:
                                print("your tries is finished, YOU LOSE !!!")
                                point3 = 0
                                break
                            else:
                                print(f"{tries} tries left")
                        else:
                            print("that's wright, YOU WIN !!!")
                            point3 = 10
                            tries = 3
                            break
    result = ""
    while result.lower().strip() != "result":
        print(" \n \nPrint 'result' to check your score")
        result = input()
    else:
        print(" \nyour score in -game 3- is :",
              int(point1+point2+point3), "points")
else:
    quit()
# finish ^_^
