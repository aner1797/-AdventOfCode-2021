my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

numbers = content_list[0].split(',')
boards = content_list[1:]

def generateBoards():
    tmp = []
    finalList = []

    for i in range(len(boards)):
        if boards[i] == "":
            if len(tmp) > 0:
                finalList.append(tmp)
                tmp = []
        else:
            tmp.append(boards[i].split())
    return finalList

def checkBoard(board, numbers):
    for row in board:
        bingo = 0
        for n in numbers:
            if n in row:
                bingo += 1
        if bingo == 5:
            return calculateScore(board, numbers, n)

    
    for col in range(len(board)):
        bingo = 0
        for i in range(len(board)):
            if board[i][col] in numbers:
                bingo += 1
            if bingo == 5:
                return calculateScore(board, numbers, n)
    
    return False
    
def calculateScore(board, numbers, final):
    sum = 0
    for row in board:
        for val in row:
            if val not in numbers:
                sum += int(val)

    return sum * int(final)


boards = generateBoards()
nrs = []

for n in numbers:
    nrs.append(n)
    for b in boards:
        val = checkBoard(b, nrs)
        if val: break
    if val: break

print(val)
