f = open("B-small-practice.txt", "r").read()
splitted_file = f.split("\n")[:]
# print splitted_file

def string_with_spaces_to_list(s):
    ans = []
    tempString = ''
    for i in xrange(len(s)):
        if s[i] == ' ':
            ans.append(int(tempString))
            tempString = ''
        else:
            tempString += s[i]
    ans.append(int(tempString))
    return ans

numTestCases = int(splitted_file[0])
testCaseLine = 1 #Line index where the test case starts, i.e. where the
                # dimensions of the grid are given.

answer = ''

for testCaseNumber in xrange(numTestCases):
    # print splitted_file[testCaseLine]
    y,x = string_with_spaces_to_list(splitted_file[testCaseLine])
    testCase = []
    for z in xrange(testCaseLine+1,testCaseLine+1+y):
        testCase.append(string_with_spaces_to_list(splitted_file[z]))
    for j in xrange(y):
        for i in xrange(x):
            # This is a tile in the grid
            tileIsValidHorizontal = True
            for m in xrange(x):
                if testCase[j][m] > testCase[j][i]:
                    tileIsValidHorizontal = False
                    break
            tileIsValidVertical = True
            for n in xrange(y):
                if testCase[n][i] > testCase[j][i]:
                    tileIsValidVertical = False
                    break
            tileIsValid = tileIsValidHorizontal or tileIsValidVertical
            # Break the iteration over the x axis if found an incompatible tile
            if not tileIsValid:
                break
        # Break the iteration over the y axis if found an incompatible tile
        if not tileIsValid:
            break
    # If at the end of the iteration over the board, there are no incompatible
    # tiles, then the board is a good board
    if tileIsValid:
        print 'Case #' + str(testCaseNumber+1) + ': YES'
    else:
        print 'Case #' + str(testCaseNumber+1) + ': NO'
    testCaseLine = testCaseLine+y+1
