# x = [0, 1, [2]]
# x[2][0] = 3
# print(x)
# x[2].append(4)
# print(x)
# x[2] = 2
# print(x)

########################################

# for i  in range(10):
#    print(i, i*i, i*i*i)


# names = ["a", "b", "c"]
# values = [1, 2, 3]
# for name, value in zip(names, values):
#     print(name, value)

# product = [2,3,4]
# print(sum(product))



# def factorial(n):
#     if n==0:
#         return 1
#     else :
#         return n* factorial(n-1)
    
# result = factorial(3)
# print(result)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# product = [1, 2, 3]
# result = [factorial(n) for n in product]
# print(result)


# def reverse(x):
#     return x[::-1]

# reversed_list = reverse([1,2,3,4])
# print(reversed_list)


# def reverse(x):
#     return list(reversed(x[::-1]))
# reversed_list = reverse([1,2,3,4])
# print(reversed_list)

##############################################
# min && max

# list1=['php','python','java']
# print(min(list1))
# print(max(list1))

#################################################


# def cumulative_sum(x):
#     cu=[]
#     j=0
#     for i in range(len(x)):
#         j+=x[i]
#         cu.append(j)
#     return cu

# result1 = cumulative_sum([1, 2, 3, 4])
# result2 = cumulative_sum([4, 3, 2, 1])
# print(result1)
# print(result2)




# def cumulative_product(x):
#     cu=[]
#     j=1
#     for i in range(len(x)):
#         j*=x[i]
#         cu.append(j)
#     return cu

# result = cumulative_product([1, 2, 3, 4])
# print(result)



# def unique(x):
#     unique_list=[]
#     for i in x:
#         if i not in unique_list:
#             unique_list.append(i)
#         else:
#             continue
#     return unique_list

# result = unique([1, 2, 1, 3, 2, 5])
# print(result)
    
    
# def dups(x):
#     unique_list=[]
#     dups_list=[]
#     for i in x:
#         if i not in unique_list:
#             unique_list.append(i)
#         else:
#             dups_list.append(i)
#     return dups_list
# result = dups([1, 2, 1, 3, 2, 5])
# print(result)


# def group(list,size):
#     return [list[i:i+size] for i in range(0,len(list),size)]

# result =group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
# print(result)
    
###################################################
