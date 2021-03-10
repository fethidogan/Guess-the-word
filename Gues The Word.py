import random
with open("computer.txt","r") as read_file:
    source = read_file.read()
with open("food.txt","r") as read_foods:
    source_food = read_foods.read()

source = source.split("\n")
source.pop()
word = random.choice(source)

source_foods = source_food.split("\n")
source_foods.pop()

point = 0

def play(word):
    num_of_try_left = 5
    guesses = []
    flag = False
    global point

    underscore = len(word) * "_"
    underscore = list(underscore)
    print(underscore)

    while not flag and num_of_try_left > 0:
        submitted = input("Enter a character")
        if submitted in guesses:
            num_of_try_left -= 1
            print("Same Character Typed")

        elif submitted not in word:
            num_of_try_left -= 1
            guesses.append(submitted)
            print("Character / syllable not in word")

        elif submitted in word:
            if len(submitted) > 1:
                import re
                index = [[m.start(),m.end()] for m in re.finditer(submitted,word)]
                for i in range(index[0][0],index[0][1]):
                    underscore[i] = word[i]
                print(underscore)
            else:
                index = [k for k,v in enumerate(word) if v == submitted]
                for i in index:
                    underscore[i] = submitted
                print(underscore)

        if "".join(underscore) == word:
            flag = True
            point += 5

if __name__ == '__main__':
    play(word)
    print(f"Play Again Y/N {point}")
    giris = input("")
    count = 0
    while giris == "y" or giris =="Y":
        if point > 10:
            word = random.choice(source_foods)
        elif point < 10:
            word = random.choice(source)
        count += 1
        if count % 4 == 0:
            print("Continue Playing ? Y/N")
            giris = input("")
            if giris == "N" or giris == "n":
                quit()
            else:
                continue
        print(f"Current Point {point}")
        print(count)
        play(word)
