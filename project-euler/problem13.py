numbers = raw_input("Insert many numbers")

numList = []

tempNum = ''

for n in numbers:
    if n == '\n':
        numList.append(tempNum)
        tempNum = ''
    else:
        tempNum = tempNum + n

numList.append(tempNum)

numList2 = []

for n in numList:
    numList2.append(int(n))

print sum(numList2)[:10]
