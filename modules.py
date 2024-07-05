# import time
# # tym=time.asctime()
# # tym=time.localtime()
# print(tym)


# import sys

# if len(sys.argv) != 3:
#     print("Usage: python script.py <filename> <search_string>")
#     sys.exit(1)

# filename = sys.argv[1]
# search_string = sys.argv[2]

# with open(filename, 'r') as f:
#     contents = f.read()
#     if search_string in contents:
#         print(f"{search_string} found in {filename}")
#     else:
#         print(f"{search_string} not found in {filename}")


############################################
## importing modules form another page 

# import num
# a=num.square(3)
# print(a)
# b=num.cube(3)
# print(b)

######################################


# import os
# current_dir = os.getcwd()
# print(current_dir)


# import os
# result =os.getcwd.__doc__
# print(result)


# import os 
# def list_dir(pathname):
#     return [x for x in pathname]


# path = os.listdir('/home/nisam/Desktop/Python_training')
# listing = list_dir(path)
# print(listing)



# import os
# def extcount(files):
#     count_py = 0
#     count_txt=0
#     count_csv=0
#     for x in files:
#         if x.endswith('.py'):
#             count_py+=1
#         elif x.endswith('.txt'):
#             count_txt+=1
#         else:
#             count_csv+=1
#     return count_py,count_txt,count_csv
# path = os.listdir('/home/nisam/Desktop/Python_training')
# count_py,count_txt,count_csv = extcount(path)
# print(f'python_files:{count_py}\ntext_files:{count_txt}\ncsv files:{count_csv}')

#####################################################

# import os
# def stat(files):
#     return [os.stat(x) for x in files]

# path = os.listdir('/home/nisam/Desktop/Python_training')
# status =stat(path)
# for i in status:
#     print(f'size:{i.st_atime}, modification time: {i.st_mtime}')

#########################################################

# import os
# def list_directory_tree(starting_directory):
#     for root, directories, files in os.walk(starting_directory):
#         print(f"Directory: {root}")
#         for file in files:
#             print(f"  File: {file}")

# path ='/home/nisam/Desktop/Python_training'
# tree = list_directory_tree(path)
# print(tree)




####in tree method

# import os

# def list_directory_tree(starting_directory, level=0):
#     indent = '  ' * level
#     for root, directories, files in os.walk(starting_directory):
#         print(f"{indent}{os.path.basename(root)}")
#         for directory in directories:
#             print(f"{indent}|__/{directory}")
#         for file in files:
#             print(f"{indent}|___/{file}")
#         for directory in directories:
#             list_directory_tree(os.path.join(root, directory), level + 1)

# starting_directory = '/home/nisam/Desktop/Python_training'
# list_directory_tree(starting_directory)





##################################################################



from urllib.request import urlopen
response = urlopen("http://python.org/")
# print(response.headers)
# print(response.headers['Content-Type'])
# print(response.read().decode())