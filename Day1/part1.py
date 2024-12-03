input = open("input.txt", "r")

result = 0
rightList = []
leftList = []

for line in input:
    line = line.strip()
    num1, num2 = map(int, line.split())
    
    rightList.append(num1)
    leftList.append(num2)
    
    rightList.sort()
    leftList.sort()

for x in range(len(rightList)):
    result += abs(rightList[x] - leftList[x])
print(result)
