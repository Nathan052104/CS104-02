#Nathan Tunnessen
#Average.py
average=0
total=0
howmanyentered=0
howmany= int(input('How many Test Scores do you want to enter?  '))
while howmanyentered<howmany:
    testscore= int(input('Enter Test Scores  '))
    total=total+testscore
    howmanyentered=howmanyentered+1
average=total/howmany
print('The average for the test scores you entered is')
print(average)
