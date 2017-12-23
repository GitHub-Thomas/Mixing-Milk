"""
ID:wzch_di3
TASK:milk
LANG:PYTHON3
"""
import sys
sys.setrecursionlimit(1000000)

fin = open("milk.in","r")
fout = open("milk.out","w")
first = fin.readline()
index = first.find(" ")
target = int(first[0:index])
number = int(first[index+1:len(first)-1])
price = []
for i in range(0,1005):
    price.append(0)
for farmer in fin.readlines():
    index = farmer.find(" ")
    price[int(farmer[0:index])] = price[int(farmer[0:index])] + int(farmer[index+1:len(farmer)])
total = 0
money = 0
for i in range(0,1005):
    if (price[i] > (target - total)):
        money = money + i * (target - total)
        break
    if (price[i] != 0):
        total = total + price[i]
        money = money + i * price[i]
fout.write(str(money)+"\n")
fin.close()
fout.close()
