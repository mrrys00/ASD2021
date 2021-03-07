def changeMin(money, coins):
    score, score[0] = [float("inf")] * (money + 1), 0
    for i in range(1, len(score)):
        for c in coins:
            score[i] = min(score[i], score[i - c] + 1)
    return score[money]

def changeCoins(money, coins):
    score, score[0] = [float("inf")] * (money + 1), 0
    changeCoins = [""] * (money + 1)
    for i in range(1, len(score)):
        for c in coins:
            if score[i] > score[i - c] + 1:
                score[i] = score[i - c] + 1
                changeCoins[i] = changeCoins[i - c] + str(c) + ","
    return strToInt(changeCoins[money])

def strToInt (n):
    output, j = [], ""
    for i in range(len(n)):
        if not n[i] == ",": j+= n[i]
        else:
            output.append(int(j))
            j = ""
    return output

money, coins = 17, [11, 5, 2, 1]
print ("min coins:"), print (changeMin(money, coins))
print ("change:"), print (changeCoins(money, coins))