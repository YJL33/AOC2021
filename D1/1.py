f = open("D1/input1", "r")
measurements = f.read().split('\n')
print(len(measurements))

# 1A
prev = int(measurements[0])
cnt = 0
for m in measurements[1:]:
    n = int(m)
    if n > prev: cnt += 1
    prev = n

print('cnt1:', cnt)

# 1B: check the diff b/w i and i+3
cnt2 = 0
for i in range(len(measurements)-3):
    a, b = int(measurements[i+3]), int(measurements[i])
    if a-b > 0: cnt2 += 1

print('cnt2', cnt2)
