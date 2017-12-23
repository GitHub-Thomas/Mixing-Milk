"""
ID:wzch_di3
TASK:milk
LANG:PYTHON3
"""
import sys
sys.setrecursionlimit(1000000)
def quick_sort(lists, left, right,list2):  
    # 快速排序  
    if left >= right:  
        return ()  
    key = lists[left]
    key2 = list2[left]
    low = left  
    high = right  
    while left < right:  
        while left < right and lists[right] >= key:  
            right -= 1  
        lists[left] = lists[right]
        list2[left] = list2[right]
        while left < right and lists[left] <= key:  
            left += 1  
        lists[right] = lists[left]
        list2[right] = list2[left]
    lists[right] = key
    list2[right] = key2
    quick_sort(lists, low, left - 1,list2)  
    quick_sort(lists, left + 1, high,list2)  
    return ()

fin = open("milk.in","r")
fout = open("milk.out","w")
first = fin.readline()
index = first.find(" ")
target = int(first[0:index])
number = int(first[index+1:len(first)-1])
price = []
quantity = []
for farmer in fin.readlines():
    index = farmer.find(" ")
    price.append(int(farmer[0:index]))
    quantity.append(int(farmer[index+1:len(farmer)]))
quick_sort(price,0,number-1,quantity)
total = 0
money = 0
flag = 0
while (total<target):
    if (quantity[flag] >= (target - total)):
        money = money + price[flag] * (target - total)
        break
    money = money + price[flag] * quantity[flag]
    total = total + quantity[flag]
    flag = flag + 1
fout.write(str(money)+"\n")
fin.close()
fout.close()
