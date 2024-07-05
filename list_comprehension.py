# lst=[(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0]
# print(lst)



# lst=[(x,y) for x in range(5) for y in range(5) if (x+y)%2==0 and x!=y]
# print(lst)


# lst = [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
# print(lst)


# def make_zip():
#     return [(x,y) for x,y in zip([1, 2, 3], ["a", "b", "c"])]

# print(make_zip())

# zip([1, 2, 3], ["a", "b", "c"])


# def square(x):
#     return x*x
# result = map(square,range(5))
# print(list(result))


# def square():
#     return [x for x in map(lambda y: y*y, range(5))]

# print(square())



# def even(x):
#     return x%2==0
# result=filter(even,range(10))
# print(even(result))

# def even():
#     return [x for x in filter(lambda x:x%2==0,range(10))]

# print(even())



# def triplets(n):
#     return [(x,y,z) for x in range(n) for y in range (n) for z in range(n) if x+y==z]

# print(triplets(5))
        
        
# def enum(lst):
#     return[x for x in enumerate(lst)]

# result = enum(["a", "b", "c"])
# print(result)



# import numpy as np
# def creating_array(rows,columns):
#     return np.full((rows,columns),None)

# # print(creating_array(2,3))

# a=creating_array(2,3)
# a[0][0]=5
# print(a)



# with open('a.csv','r') as f:
#     re = f.read()
#     print(re)
#     parse_csv = ('a.csv')


# import csv
# def parse_csv():
#     with open('a.csv','r') as f:
#         cr = csv.reader(f,delimiter=",")
#         return [[x,y,z] for x in cr for y in cr for z in cr]
    
# print(parse_csv())



# def parse_txt():
#     with open('a.txt','r')as f:
#         lines =f.readlines()
#         delimeter = '!'
#         return [line.strip().split(delimeter) for line in lines if not line.startswith('#') ]
    
# data = parse_txt()
# print(data)


 

