import sys
allGood=True
with open("mySol.txt") as f1, open("naiveSol.txt") as f2:
    for line1, line2 in zip(f1, f2):
        if line1 == line2:
           pass
        else:
           allGood=False
           print(line1,line2)
if allGood:
    print("Compared and all is well")
