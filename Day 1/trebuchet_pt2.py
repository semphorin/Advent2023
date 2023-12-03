data = open(r'data.txt', 'r')
ldigits = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

sum = 0
for line in data.readlines():
    curnum = ""
    nums = []
    recent = []
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            nums.append(line[i])
        elif line[i].isalpha():
            recent.append(line[i])
            temp = "".join(recent)
            for key in ldigits:
                if key in temp:
                    nums.append(ldigits[key])
                    recent.clear()
                    i -= 1
        else:
            recent.clear()
        i += 1
    print(nums)
    curnum += nums[0]
    curnum += nums[-1]
    sum += int(curnum)

print(sum)
data.close()