f = open("D2/input2", "r")
rawmoves = f.read().split('\n')

# 2A
dirDict = {'forward':(1,0), 'up':(0,-1), 'down':(0,1)}
x, y = 0, 0
for rawmove in rawmoves:
    d, val = rawmove.split(' ')
    val = int(val)
    dx, dy = dirDict[d]
    x += dx*val
    y += dy*val
print('ans1', x*y)

# 2B
x, y, aim = 0, 0, 0
for rawmove in rawmoves:
    d, val = rawmove.split(' ')
    val = int(val)
    if d == 'down':
        aim += val
    elif d == 'up':
        aim -= val
    else:
        x += val
        y += val*aim
print('ans2', x*y)
