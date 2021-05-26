# Randomize 100 times heads or tails and write it to a list

import random

totalNumberOfStreaks = 0

listOfResults = []

def randCoin(listOfResults):
    for i in range(100):
        result = random.randint(0,1)
        if result == 0:
            throw = 'head'
        else:
            throw = 'tails'
        listOfResults.append(throw)
    return listOfResults


def checkStreak(listOfResults):
    numOfStreaks = 0
    for i in range(100):
        if listOfResults[i] == listOfResults[i - 1] and listOfResults[i] == listOfResults[i - 2] and listOfResults[i]  == listOfResults[i - 3] and listOfResults[i] == listOfResults[i - 4] and listOfResults[i] == listOfResults[i - 5] and listOfResults[i] == listOfResults[i - 6]:
            # print('streak')
            numOfStreaks += 1
    return numOfStreaks            

for experimentNumber in range(10000):
    randCoin(listOfResults)
    # print(checkStreak(listOfResults))
    totalNumberOfStreaks += checkStreak(listOfResults)
# print(totalNumberOfStreaks)    

print('Chance of streak: %s%%' % (totalNumberOfStreaks / 100))