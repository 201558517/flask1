#  Hangman Game
#
# 猜字游戏，计算机随机选取一个单词，玩家想办法把它一个字母一个字母地猜出来。
#
#模块引入

import random

#常量
HANGMAN = ("""--7--""","""--6--""","""--5--""","""--4--""","""--3--""","""--2--""","""--1--""","""--0--""")
#玩家最大猜错次数
MAX_WRONG = len(HANGMAN)-1
#单词题库
WORDS = ("OVERUSED","CLAM","GUAM","TAFFETA","PYTHON")
#初始化变量
word = random.choice(WORDS) #待猜测的单词
so_far = "-"*len(word) #待猜测的单词 每个 - 表示一个字母
wrong = 0 #玩家已经猜错的次数
used = [] #玩家猜到的字母
print("""Welcome to Hangman, Good Luck!""")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\n You`ve used the fellowing letters: \n",used)
    print("\n So far, the word is: \n",so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You`ve already guessed the letter",guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!",guess ,"is in the word!")

        #创建新的so_far，包含guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,",guess,"isn`t in the word.")
        wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou`ve been hanged")
    else:
        print("\nYou guess it!")

    print("\nthe word is: ",word)

