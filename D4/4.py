import collections

f = open("D4/input4", "r")
input = f.read().split('\n')
# print(len(input))
draw = input[0].split(',')
boards, tmp = [], []     # store boards

for i in range(2, len(input)):
    if input[i] == "":
        boards.append(tmp)
        tmp = []
    else:
        row = [x for x in input[i].split(' ') if x != '']
        tmp.append(row)
print('number of boards', len(boards))

# make a boardDict (dict of dict)
# key: i-th board, val: {key: number, val: (i, j)}
# make a status of board
# key: i-th board, val: 5x5 array
bd = collections.defaultdict()
boardStatus = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
for i in range(len(boards)):
    bd[i] = collections.defaultdict()
    for p in range(5):
        for q in range(5):
            bd[i][boards[i][p][q]] = (p,q)

# find whether there's a line
def finder(bd, x, y):
    cnts = []
    cnts += sum([bd[i][y] == True for i in range(5)]),
    cnts += sum([bd[x][j] == True for j in range(5)]),
    if (x == y): cnts += sum([bd[k][k] == True for k in range(5)]),
    if (x+y == 4): cnts += sum([bd[k][4-k] == True for k in range(5)]),
    return any([cnt == 5 for cnt in cnts])


def calcScore(w, d):
    print('given winner', w, d)
    unMarkedSum = 0
    for i in range(5):
        for j in range(5):
            if boardStatus[w][i][j] == False:
                unMarkedSum += int(boards[w][i][j])
    return d*unMarkedSum

# start to draw
winners = set()
firstWinnerScore = None
lastWinnerScore = None              # assume all board will win
for d in draw:
    for i in range(len(boards)):    # check all boards for each draw
        if i not in winners and d in bd[i]:         # draw is on this board, lets check theres a line or not
            p, q = bd[i][d]
            boardStatus[i][p][q] = True
            if finder(boardStatus[i], p, q):        # there's a win!
                if not firstWinnerScore:
                    firstWinnerScore = calcScore(i, int(d))             # first Winner
                winners.add(i)
                if len(winners) == 100:
                    lastWinnerScore = calcScore(i, int(d))              # last Winner
                    break

print('final score of first Winner', firstWinnerScore)
print('final score of last Winner', lastWinnerScore)
