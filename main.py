n = input("Enter string:")
countC = 0
countW = 1
for i in n :
    countC = countC+1
    if(i ==' '):
        countW = countW+1

print("Number of words in a string")
print(countW)
print("Number of characters in a string")
print(countC)
