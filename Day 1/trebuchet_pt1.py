data = open(r'data.txt', 'r')

sum = 0
for line in data.readlines():
    curnum = ""
    linenums = []
    for letter in line:
        if letter.isnumeric():
            linenums.append(letter)
    curnum += linenums[0]
    curnum += linenums[-1]
    sum += int(curnum)
    print(int(curnum))

print(sum)
data.close()