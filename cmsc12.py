'''
def ave_score():
    x = int(input("Input score: "))
    y = int(input("Input score: "))
    z = int(input("Input score: "))

    ave = (x+y+z)/3
    if ave >= 55:
        print(f"Ave. score is {ave} - PASS")
    else:
        print(f"Ave. score is {ave} - FAIL")
    
    highest = x
    if y > highest:
        highest = y
    if z > highest:
        highest = z
    
    print(f"Highest score is {highest}.")

ave_score()
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LT1 problem soliving solution
# N = int(input("Enter N: "))

# largest = 0
# larger = 0
# for i in range(N):
#     num = int(input("Enter n: "))
#     if num > largest:
#         larger = largest
#         largest = num
#     elif num > larger:
#         larger = num

# print(largest)
# print(larger) 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem #18
# negative indexes
# def reverseStrings(s):
#     reverse = ""
#     for i in range(len(s)):
#         reverse = s[i] + reverse #reverse s[len(s)-1-i] 
#     return reverse
# s = reverseStrings(str(input("word: ")))
# print(s)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# l1 = [x for x in range(5)]
# print(l1)
#output:
#[0, 1, 2, 3, 4]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# list3= [[x,y] for x in [1, 2, 3,] for y in [3, 1, 4] if x!=y]
# print(list3)
#output: pairs
#[[1, 3], [1, 4], [2, 3], [2, 1], [2, 4], [3, 1], [3, 4]]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#list1 = [1, 2, 3, 4, 5]
#list2 = list1 #same lists, copies the location of list1

#print(list1, list2)

#list1[4] = 10 #changing in list2 will also change list1
#print(list1, list2)
#[1, 2, 3, 4, 10] [1, 2, 3, 4, 10]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#list1 = [0, 1, 2, 3, 4]
#list2 = list1.copy() #actually copies the dictionary list1

#list1[4] = 10
#print(list1, list2)
#output: [0, 1, 2, 3, 10] [0, 1, 2, 3, 4]
#list1 changed value, list2 remains the same
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#QUEUE - first in first out
#STACK - last in first out
#stack <- push
#ace <- 2 <- 3
#pop 3, 2 is now on top
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#linear search
# worst case is o(n)
def lsearch (L, x):
    for i in range(0, len(L)):
        if L[i] == x:
            return i
        if L[i] > x: #applicable for ascending order lists
            return None
    return None
    
sampleList = [0, 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 16, 18, 20]
search_target = 3

result = lsearch(sampleList, search_target)
print(result)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#binary search
#worst case O(logn)