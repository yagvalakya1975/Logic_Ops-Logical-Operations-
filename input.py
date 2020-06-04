#          ____    ____   _____   ____          ____    ____   ____
#  |      |    |  |         |    |             |    |  |    | |
#  |      |    |  |  ___    |    |             |    |  |----^ ^---,
#  |____  |____|  |____|  __|__  |____         |____|  |      ____|

# declaration of all files and libraries.
import dataSet

# declare variables and arrays
allStatements = []
toRemove = [0]
separator = ['.', ',', 'and', 'while', 'if', 'when', 'but', ';', '?']
LastKey = -1

print("please leave a space between each word , symbol and punctuation.")
print(" Don't forget to put a full stop or question mark at the end of the question")

question = input('Enter the question ')  # ask the question
questionTuple = question.split(" ")   # convert question into tuple

for index, word in enumerate(questionTuple):
    statement = ''
    if word == '': questionTuple.remove('')
    else:
        for x in separator:
            if word.lower() == x:
                toRemove.append(index)
                for y in range(LastKey + 1, index):
                    if statement != '': statement = statement + ' ' + questionTuple[y]
                    else: statement = questionTuple[y]
                    LastKey = index
        if statement != '': allStatements.append(statement)
print(allStatements)

if len(allStatements) < 3: print('The question is either inappropriate or it is not written in right form')

# Aditya has 5 apples and chinmay has 6 apples . what is the total number of apples ?
for statement in allStatements:
    Tuple_ = statement.split(" ")
    print(Tuple_)
