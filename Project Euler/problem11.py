nums = raw_input('Insert grid of numbers: ')

subList = []
bigList = []

for n in xrange(len(nums)/3+1):
    subList.append(int(nums[3*n] + nums[3*n+1]))
    if (n+1)%20 == 0:
        bigList.append(subList)
        subList = []

maxProd = 0

#Diagonal decreasing

for i in xrange(17):
    for j in xrange(17):
        currentProd = bigList[i][j]*bigList[i+1][j+1]*bigList[i+2][j+2]*bigList[i+3][j+3]
        maxProd = max(currentProd, maxProd)

#Diagonal increasing

for i in xrange(3,20):
    for j in xrange(17):
        currentProd = bigList[j][j]*bigList[j+1][i-1]*bigList[j+2][i-2]*bigList[j+3][i-3]
        maxProd = max(currentProd, maxProd)

#Horizontal

for i in xrange(17):
    for j in xrange(20):
        currentProd = bigList[j][i]*bigList[j][i+1]*bigList[j][i+2]*bigList[j][i+3]
        maxProd = max(currentProd, maxProd)

#Vertical

for i in xrange(20):
    for j in xrange(17):
        currentProd = bigList[j][i]*bigList[j+1][i]*bigList[j+2][i]*bigList[j+3][i]
        maxProd = max(currentProd, maxProd)

print maxProd
