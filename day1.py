firstNum = newNum = count = 0
newInput = input()
newNum = int(newInput)
firstNum = newNum

while True:
    newInput = input()
    newNum = int(newInput)
    if newNum > firstNum:
        count = count + 1
    firstNum = newNum
    print(count)
