f = open("D3/input3", "r")
reports = f.read().split('\n')

# 3A
counter = [0 for _ in reports[0]]
for r in reports:
    for i in range(len(counter)):
        counter[i] += 1 if r[i] == '1' else -1

print('counter:', counter)
gamma, epsilon = 0, 0
x = 1
for c in counter[::-1]:
    mostCommon = 1 if c > 0 else 0
    leastCommon = 1-mostCommon
    gamma += x*mostCommon
    epsilon += x*leastCommon
    x *= 2

print('gamma', gamma, 'epsilon', epsilon, 'power consumption', gamma*epsilon)

# 3B
# find oxygen
rep1 = [r for r in reports]
for i in range(12):
    ones, zeros = [], []
    for r in rep1:
        if r[i] == '1': ones += r,
        else: zeros += r,
    rep1 = ones if len(ones) >= len(zeros) else zeros
    if len(rep1) == 1:
        break

# find co2
rep2 = [r for r in reports],
for i in range(12):
    ones, zeros = [], []
    for r in rep2:
        if r[i] == '1': ones += r,
        else: zeros += r,
    rep2 = zeros if len(zeros) <= len(ones) else ones
    if len(rep2) == 1: break
    
print('rep1:', rep1, 'rep2:', rep2)
oxy, co2 = 0, 0
oxybit, co2bit = rep1[0], rep2[0]
x = 1
for i in range(11,-1,-1):
    oxy += x*int(oxybit[i])
    co2 += x*int(co2bit[i])
    x *= 2
print('oxy', oxy, 'co2', co2, 'multiply', oxy*co2)
