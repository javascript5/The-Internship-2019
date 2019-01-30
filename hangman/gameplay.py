import json
import random
category = ""

def inputFunction(inputText):
    while True:
        print(inputText)
        userInput = input(">>> ")
        if len(userInput) == 1:
            return userInput
        else:
            print("Please Input 1 character")

def frameFunction(textInFrame):
    for num in range(46):
        print("#", end="")
    print("")

    print(textInFrame.center(46), end="")

    print("")
    for num in range(46):
        print("#", end="")
    print("")
    print("")
    
def frameTwoVersionFunction(textInFrame):
    for num in range(46):
        print("-", end="")
    print("")

    print(textInFrame.center(46), end="")

    print("")
    for num in range(46):
        print("-", end="")
    print("")
    print("")

def logo():
    frameFunction("Hangman")
    

def selectCategory(category):
    print("Category")
    print("")
    print("  1 ) Thai Food")
    print("  2 ) Fruits")
    print("  3 ) Movies")
    print("")
    userInput = inputFunction("Select Category (ex.1)")
    while True:
        if userInput >= "1" and userInput <= "3":
                break
        else:
            print("Please input number 1-3 ")
            userInput = inputFunction("Input 1-3")

    from pprint import pprint
    with open('category_'+userInput+'.json') as f:
        category = json.load(f)

    return category

def randomWord(category):
    categoryLength = len(category)
    category = category[str(random.randint(0, categoryLength-1))]
    category["word"] = category["word"].replace(' ', '')
    return category

def randomGuessChar(word):
    word = word["word"]
    guessChar = ''
    guessChar += ''.join(i for i in word if i.isdigit())
    word = ''.join(i for i in word if not i.isdigit())
    guessChar += word[random.randint(0, len(word)-1)]

    return guessChar


def showGuessWord(word, answer, guessWord):
    guessWord = ""
    validLetters = "abcdefghijklmnopqrstuvwxyz"

    for char in word["word"]:
        if char not in answer:
            if char in validLetters or char in validLetters.upper():
                guessWord += "_"
        else:
            guessWord += char
    frameTwoVersionFunction("Hint : " + word["hint"])
    frameTwoVersionFunction(guessWord)

    return guessWord

def healthPointCalculator(healthPoint, status):
    if status == "add":
        if healthPoint < 5:
            healthPoint += 1
    else:
        if healthPoint > 0:
            healthPoint -= 1
    return healthPoint

def checkInput(word, answer , answerInput):
    for char in word["word"]:
        if char == answerInput:
            return True
    return False


def gameOver():
    frameFunction("Game Over")

def gameWin():
    frameFunction("Game Win")

def checkAnswer(guessWord):
    for char in guessWord:
        if char == "_":
            return False
    return True

def gamePlay():
    while True:
        logo()
        category = ""
        word = ""
        guessChar = ''
        answer = ''
        healthPoint = 5
        guessWord = ""
        incorrectCharBuf = ""
        category = selectCategory(category)
        word = randomWord(category)

        guessChar = randomGuessChar(word)
        answer += guessChar
        while True:
            guessWord = showGuessWord(word, answer, guessWord)
            
            if healthPoint == 0:
                gameOver()
                break
            
            if checkAnswer(guessWord):
                gameWin()
                break

            

            frameTwoVersionFunction("HP : " + str(healthPoint))

            frameTwoVersionFunction("Incorrect : " + incorrectCharBuf)

            
            answerInput = inputFunction("Input ex.A")



            if checkInput(word, answer , answerInput):
                if answerInput not in answer:
                    answer += answerInput
                    healthPoint = healthPointCalculator(healthPoint, "add")
            else:
                healthPoint = healthPointCalculator(healthPoint, "remove")
                if answerInput not in incorrectCharBuf:
                    incorrectCharBuf += answerInput
            

        
    

    # startGame()

gamePlay()