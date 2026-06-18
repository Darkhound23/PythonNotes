
# no=1
# for i in range(5):
#     for j in range(3):
#         print(no,end= "")
#         no+=1
#     print()
#     no +=1
        
    #ipyn
    
    
    ###########################
# no=65
# for i in range(5):
#     for j in range(3):
#         print(chr(no),end="")
#         no+= 1
#     print()
#     no= 65
    
# *
# **
# ***
# ****
#noStar=1

# for i in range(5):
#     for j in range(noStar):
#         print("*",end="")
#     print()
#     noStar += 1
       
####inverse 
# noStar = 5

# for i in range(5):
#     for j in range(noStar):
#         print("*", end="")
#     print()
#     noStar -= 1

#****
#***
#**
#* 

# noStar = 5
# for i in range(noStar):
#     for j in range(noStar-i):
#         print("*",end="")
#     print()
#center triangle star
#rows = 5
# for i in range(rows):
#     for j in range(rows -i + 1):
#         print(" ",end="")
#     for k in range(2 * i + 1):
#         print("*",end="")
#     print()

# rows = 5
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2 * (rows -i)- 1):
#         print("*",end="")
#     print()


# 3 candle ,uneven 1 candle burn time 30 min 
#52 min 30 mo sec 

# num =123
# rev =0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print(rev)

# num = 123
# total = 0

# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10

# print(total)
# def reverse_number(num):
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10

#     return rev

# print(reverse_number(123))

# def sum_of_digits(num):
#     total = 0

#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10

#     return total

# num = 123
# print(sum_of_digits(num))

# 1. Find common elements in 2 arrays
def common_elements(arr1, arr2):
    common = []

    for i in arr1:
        for j in arr2:
            if i == j and i not in common:
                common.append(i)

    return common


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

print(common_elements(a, b))


# # 2. Find unique elements in array
# def unielements(arr):
#     result = []

#     for i in arr:
#         if arr.count(i) == 1:
#             result.append(i)

#     return result


# # 3. Left rotate array by 1
# def left_rotate(arr):
#     first = arr[0]

#     for i in range(len(arr) - 1):
#         arr[i] = arr[i + 1]

#     arr[-1] = first
#     return arr


# # 4. Right rotate array by 1
# def right_rotate(arr):
#     last = arr[-1]

#     for i in range(len(arr) - 1, 0, -1):
#         arr[i] = arr[i - 1]

#     arr[0] = last
#     return arr


# # 5. Move all zeroes at end
# def move_zeroes_end(arr):
#     result = []

#     for i in arr:
#         if i != 0:
#             result.append(i)

#     zero_count = arr.count(0)

#     for i in range(zero_count):
#         result.append(0)

#     return result


# # 6. Check 2 arrays are equal
# def arrays_equal(a, b):
#     return sorted(a) == sorted(b)


# # 7. Find first non-repeating element
# def first_non_repeating(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i

#     return None


# # 8. Find pair with max product
# def max_product_pair(arr):
#     max_product = arr[0] * arr[1]
#     pair = (arr[0], arr[1])

#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             product = arr[i] * arr[j]

#             if product > max_product:
#                 max_product = product
#                 pair = (arr[i], arr[j])

#     return pair, max_product


# arr = [1, 2, 2, 3, 4, 4, 5]
# zero_arr = [1, 0, 2, 0, 3, 0, 4]
# product_arr = [1, 10, -5, 2, -20]

# print(commonelements(arr1, arr2))
# print(unielements(arr))
# print(left_rotate(arr1.copy()))
# print(right_rotate(arr1.copy()))
# print(move_zeroes_end(zero_arr))
# print(arrays_equal([1, 2, 3], [3, 2, 1]))
# print(first_non_repeating(arr))
# print(max_product_pair(product_arr))