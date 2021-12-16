f = open("D16/input16", "r")
# f = open("D16/test1", "r")
rawData = f.read().split('\n')[0]

global verSum
verSum = 0

def convertToBinary(rawData):
    binary = ""
    dict = {"0": '0000',"1": '0001',"2": '0010',"3": '0011',"4": '0100',"5": '0101',"6": '0110',"7": '0111',"8": '1000',"9": '1001',"A": '1010',"B": '1011',"C": '1100',"D": '1101',"E": '1110',"F": '1111',}
    for i in range(len(rawData)):
        binary += dict[rawData[i]]
    return binary

# 16A
def addToVerSum(x):
    global verSum
    verSum += x
    return

def toDecimal(b):
    ans, x = 0, 1
    for c in b[::-1]:
        if c == '1': ans += x
        x *= 2
    return ans

# 16B
def helper(typeID, packetsVals):
    if typeID == 0:
        return sum(packetsVals)
    elif typeID == 1:
        x = 1
        for n in packetsVals: x *= n
        return x
    elif typeID == 2:
        return min(packetsVals)
    elif typeID == 3:
        return max(packetsVals)
    elif typeID == 5:
        return 1 if packetsVals[0] > packetsVals[1] else 0
    elif typeID == 6:
        return 1 if packetsVals[0] < packetsVals[1] else 0
    elif typeID == 7:
        return 1 if packetsVals[0] == packetsVals[1] else 0

def readPackets(binaryData):
    verID, typeID, binaryData = toDecimal(binaryData[:3]), toDecimal(binaryData[3:6]), binaryData[6:]
    addToVerSum(verID)
    if typeID == 4:
        groupsOfPackets = ""
        while True:
            packet, binaryData = binaryData[:5], binaryData[5:]
            groupsOfPackets += packet[1:]
            if packet[0] == '0': break
        return toDecimal(groupsOfPackets), binaryData
    
    else:
        lengthTypeID, binaryData = binaryData[0], binaryData[1:]
        packetVals = []

        if lengthTypeID == '0':
            toParseLength, binaryData = toDecimal(binaryData[:15]), binaryData[15:]
            toParse, binaryData = binaryData[:toParseLength], binaryData[toParseLength:]
            while toParse:
                # print('toParse, packetVals', toParse, packetVals)
                val, toParse = readPackets(toParse)
                packetVals.append(val)
        else:
            n, binaryData = toDecimal(binaryData[:11]), binaryData[11:]
            for _ in range(n):
                val, binaryData = readPackets(binaryData)
                packetVals.append(val)
        
        val = helper(typeID, packetVals)
        # print('val, pkts', val, packetVals)
        return val, binaryData

binaryData = convertToBinary(rawData)
# print('binary length:', len(binaryData))

val, binary = readPackets(binaryData)
print('version sum:', verSum)
print('val, bin', val, binary)
