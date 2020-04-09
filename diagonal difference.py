arr = [[11, 2, 4], 
       [4 , 5, 6], 
       [10, 8, -12]] 

def difference(arr):
    counter = 0
    counter2 = len(arr) - 1
    right_arr = []
    left_arr = []
    for i in range(len(arr)):
        left_arr.append(arr[counter][counter])
        counter += 1
    print(left_arr)
    counter = 0
    for i in range(len(arr)):
        right_arr.append(arr[counter][counter2])
        counter += 1
        counter2 -= 1
    print(right_arr)
    return abs(sum(left_arr) - sum(right_arr))

print(difference(arr))






# def diagonalDifference(arr, n):
#     prim =0
#     sec=0
#     length = len(arr[0])
#     for count in range(length):
#         prim += arr[count][count]
#         sec += arr[count][(length-count-1)]
#     return abs(prim-sec)  

# diagonalDifference([[1,2,3], 
#                     [4,5,6], 
#                     [9,8,9]], 3)

# def difference(arr, n): 
#     # Initialize sums of diagonals 
#     d1 = 0
#     d2 = 0
#     for i in range(0, n): 
#         for j in range(0, n): 
#             # finding sum of primary diagonal 
#             if (i == j): 
#                 d1 += arr[i][j] 
#             # finding sum of secondary diagonal 
#             if (i == n - j - 1): 
#                 d2 += arr[i][j]   
#     # Absolute difference of the sums 
#     # across the diagonals 
#     return abs(d1 - d2); 

# # Driver Code 
# n = 3
# arr = [[11, 2, 4], 
#        [4 , 5, 6], 
#        [10, 8, -12]] 
  
# print(difference(arr, n))