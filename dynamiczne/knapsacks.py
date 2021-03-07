def knapsackScore(cap, weight, price):
    score = []
    for i in range(len(weight)):
        score.append([])
        for j in range(cap + 1): score[i].append(0)
    
    for i in range(weight[0], cap + 1): score[0][i] = price[0]

    for i in range(1, len(weight)):
        for j in range (1, cap + 1):
            score[i][j] = score[i - 1][j]
            if weight[i] <= j: score[i][j] = max(score[i][j], score[i - 1][j - weight[i]] + price[i])
    
    return score[len(weight) - 1][cap]

def knapsackItems(cap, weight, price):
    score, items = [], []
    for i in range(len(weight)):
        score.append([])
        items.append([])
        for j in range(cap + 1):
            score[i].append(0)
            items[i].append ("")

    for i in range(weight[0], cap + 1):
        score[0][i] = price[0]
        items[0][i] = "0,"

    for i in range(1, len(weight)):
        for j in range (1, cap + 1):
            score[i][j] = score[i - 1][j]
            items[i][j] = items[i - 1][j]
            if weight[i] <= j and score[i][j] < score[i - 1][j - weight[i]] + price[i]:
                score[i][j] = score[i - 1][j - weight[i]] + price[i]
                items[i][j] = items[i - 1][j - weight[i]] + str(i) + ","
    
    return strToInt(items[len(weight) - 1][cap])

def strToInt (n):
    output, j = [], ""
    for i in range(len(n)):
        if not n[i] == ",": j+= n[i]
        else:
            output.append(int(j))
            j = ""
    return output

capacity, weight, price = 10, [5, 2, 4, 2], [60, 50, 70, 50]
print ("score:"), print (knapsackScore(capacity, weight, price))
print ("items:"), print (knapsackItems(capacity, weight, price))