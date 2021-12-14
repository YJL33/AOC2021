import collections

# get the input
f = open("D14/input14", "r")
lines = f.read().split('\n')
template = lines[0]
ruleDict = collections.defaultdict()

for l in lines[1:]:
    pair, insert = l.split(" -> ")
    ruleDict[pair] = insert

# initial state
elementCounter = collections.Counter(template)

# only check those pairs both in polymer and rules
pairs = collections.defaultdict(int)
for i in range(len(template)-1):
    if template[i:i+2] in ruleDict:
        pairs[template[i:i+2]] += 1

# simply iterate x times to get the result
x = 40
while x:
    tmp = collections.defaultdict(int)
    for pair, val in pairs.items():
        a, b = pair[0]+ruleDict[pair], ruleDict[pair]+pair[1]
        elementCounter[ruleDict[pair]] += val
        if a in ruleDict: tmp[a] += val
        if b in ruleDict: tmp[b] += val

    pairs = tmp
    # print('now:', template, 'steps left', x-1)
    x -= 1

print('counter', elementCounter.most_common())
