input = open("input.txt", "r")

result = 0
rightList = []
leftList = []

for line in input:
    line = line.strip()
    num1, num2 = map(int, line.split())
    
    rightList.append(num1)
    leftList.append(num2)

for line in range(len(rightList)):
    count = leftList.count(rightList[line])
    result += rightList[line] * count

print(result)
