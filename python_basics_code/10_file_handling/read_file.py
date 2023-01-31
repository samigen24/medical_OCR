'''
f = open("funny.txt", "r")

for line in f:
    print(line)

f.close()
'''

with open("funny.txt", "r") as f:
    for line in f:
        print(line)

with open("like.txt", "r") as b:
    for line in b:
        print(line)
