import heapq

f = open("D15/input15", "r")
lines = f.read().split('\n')
# print(lines)

# 15A
r1 = [[int(lines[i][j]) for j in range(len(lines[0]))] for i in range(len(lines))]

# 15B
r2 = [[x for x in r] for r in r1]
for r in r2:
    tmp = []
    for j in range(1,5):
        tmp += [(r[i]+j)-9 if (r[i]+j)>9 else r[i]+j for i in range(len(r))]
    r += tmp
tmp = []
for j in range(1,5):
    for r in r2:
        tmp += [(r[i]+j)-9 if (r[i]+j)>9 else r[i]+j for i in range(len(r))],
r2 += tmp

# use DFS + heap
def finder(risks):
    print('H, W', len(risks), len(risks[0]))
    bestSeen = [[float('inf') for _ in range(len(risks[0]))] for _ in range(len(risks))]
    H, W = len(risks), len(risks[0])
    hp = [(0,0,0)]      # risks, i, j
    visited = set()

    # pop from the best path (which has minimum risk)
    # if we visit some point twice => can be ignored
    while hp:
        riskSum, i, j = heapq.heappop(hp)
        if riskSum > bestSeen[i][j] or (i, j) in visited: continue
        visited.add((i,j))
        bestSeen[i][j] = riskSum
        if i == H-1 and j == W-1: break     # done
        # add neighbors
        for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0<=a<H and 0<=b<W:
                heapq.heappush(hp, (risks[a][b]+riskSum, a, b))

    print('bestSeen', bestSeen[-1][-1])
    return bestSeen[-1][-1]

finder(r1)
print('r2', r2[-1])
finder(r2)