string = ""
count = 0
longestCount = 0
longestString = ""
for i in range(len(s)):
    if i == 0:
        string += s[i]
        count += 1
    elif s[i] >= s[i - 1]:
        string += s[i]
        count += 1
    elif s[i] < s[i - 1]:
        if count > longestCount:
            longestCount = count
            longestString = string
        count = 0
        count = 1
        string = ""
        string += s[i]
    if i == len(s) - 1:
        if count > 1:
            if count > longestCount:
                longestCount = count
                longestString = string
print("Longest substring in alphabetical order is: " + longestString)
