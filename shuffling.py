import random
import secrets
import os

def get_list(filename):
    my_file = open(filename, "r")
    my_list = []

    for line in my_file:
        if line.strip() != "":
            my_list.append(line.strip())

    my_file.close()
    return my_list

def confirmation():
    ask = input("Confirm exit? (y/N): ")

    if ask.upper() == "Y":
        return True
    else:
        return False

# "words" function takes a list of Japanese words in a file, then shuffle it,
# then print them. It can also take English words.

def words(filename, eng=False):
    my_words = get_list(filename)
    counter = 1
    comma = ""

    if eng == False:
        comma = "、"
    elif eng == True:
        comma = ", "
    else:
        print("\"eng\" argument can only take boolean variable.")
        print("True for English comma, False or empty for Japanese comma.")
        print("Proceed with Japanese comma.\n")
        comma = "、"

    while True:
        random.shuffle(my_words)

        for word in my_words:
            if counter > 5:
                print("\n", end = "")
                counter = 1

            print(word, end = "")
            counter = counter + 1

            if counter <= 5:
                print(comma, end = "")

        answer = input()

        if answer != "":
            confirm = confirmation()
            if confirm: break

        counter = 1
        os.system("clear")
        my_words = get_list(filename)

# "hiragana" function takes a list of hiragana characters and shuffle them. Some
# hiragana characters have dakuten. It can choose one with dakuten or one
# without it.

def hiragana(filename):
    my_chars = get_list(filename)
    counter = 1

    while True:
        random.shuffle(my_chars)

        for char in my_chars:
            if counter > 5:
                print("\n", end = "")
                counter = 1

            if len(char) == 1: #If it has no dakuten
                print(char, end = "、")
            else:
                try: #Some characters have handakuten
                    print(char[secrets.randbelow(3)], end = "、")
                except:
                    print(char[secrets.randbelow(2)], end = "、")

            counter = counter + 1

        answer = input()

        if answer != "":
            confirm = confirmation()
            if confirm: break

        counter = 1
        os.system("clear")
        my_chars = get_list(filename)

def katakana(filename):
    hiragana(filename)

# "sentences" function takes a list of sentences from a file and then
# shuffle it before print it. But it prints an empty line in between
# unlike the "words" function

def sentences(filename):
    my_sentences = get_list(filename)

    while True:
        random.shuffle(my_sentences)

        for sentence in my_sentences:
            print("\n", end = "")
            print(f"{sentence}", end = "\n")

        answer = input()

        if answer != "":
            confirm = confirmation()
            if confirm: break

        os.system("clear")
        my_sentences = get_list(filename)
