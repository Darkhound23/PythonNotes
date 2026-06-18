#l = [40, 25, 34, 45, 53]
#1/ find max element in list without using function
# maxNum = l[0]
# for i in l:
#     if i > maxNum:
#         maxNum = i
# print(maxNum)

#1/find min element in list without using function
# minNum = l[0]
# for i in l:
#     if i < minNum:
#         minNum = i
# print(minNum)

# count = 0
# for i in l:
#     count += 1
#     print(count)

# # sum of all elements
# total = 0
# for i in l:
#     total += i
#     print(total)
    
#count  even and odd elements
l = [10, 25, 8, 45, 12, 7, 4]

even = 0
odd = 0

for i in l:
    if i % 2 == 0:
        even += 1 
    else:
        odd += 1
        
    print("odd =" ,odd)
    print("even =",even)

# even = 0
# odd = 0

# for i in l:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even =", even)
# print("Odd =", odd)