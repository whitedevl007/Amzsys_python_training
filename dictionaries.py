# a={'x':1, 'y':2, 'z':3}
# print(a['y'])


# b={}
# b[2]="apple"
# b[1]="mango"
# b[0]=b[1]
# # print(b)
# del b[0]
# # print(b)

# print(b.keys())
# print(b.values())
# print(b.items())

# for key in b:
#     print(key)


# for key,value in b.items():
#     print(key,value)
    
# d={'x':1,'y':2,'z':3}
# print(d.setdefault('p',0))
# print(d)


# data = 'hello %(name)s' % {'name': 'python'}
# print(data)

# second_data = 'Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'}
# print(second_data)



# def word_frequency(words):
#     """Returns frequency of each word given a list of words.

#         >>> word_frequency(['a', 'b', 'a'])
#         {'a': 2, 'b': 1}
#     """
#     frequency = {}
#     for w in words:
#         frequency[w] = frequency.get(w, 0) + 1
#     return frequency


# result = word_frequency(['a', 'b', 'a'])
# print(result)
 
# import json
# with open('test.txt','w+')as f:
#     f.write(json.dumps(
#        {'a': 2, 'b': 3,'c': 4} )
#     )

# def word_frequency(words):
#     """Returns frequency of each word given a list of words.

#         >>> word_frequency(['a', 'b', 'a'])
#         {'a': 2, 'b': 1}
#     """
#     frequency = {}
#     for w in words:
#         frequency[w] = frequency.get(w, 0) + 1
#     return frequency

# def read_words(filename):
#     return open(filename).read().split()

# def main(filename):
#     frequency = word_frequency(read_words(filename))
#     for word, count in frequency.items():
#         print(word, count)

# if __name__ == "__main__":
#     import sys
#     main(sys.argv[1])




#############################################################

# def word_frequency(words):
#     """Returns frequency of each word given a list of words.

#         >>> word_frequency(['a', 'b', 'a'])
#         {'a': 2, 'b': 1}
#     """
#     frequency = {}
#     for w in words:
#         frequency[w] = frequency.get(w, 0) + 1
#     print(frequency)
#     return frequency

# def read_words(filename):
#     return open(filename).read().split()

# def main(filename):
#     frequency = word_frequency(read_words(filename))
#     # sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
#     for word in reversed(frequency):
#         print(word)

# if __name__ == "__main__":
#     import sys
#     main(sys.argv[1])




############################################################
# import os

# def word_frequency(words):
#     """Returns frequency of each word given a list of words.

#         >>> word_frequency(['a', 'b', 'a'])
#         {'a': 2, 'b': 1}
#     """
#     frequency = {}
#     for w in words:
#         frequency[w] = frequency.get(w, 0) + 1
#     print(frequency)
#     return frequency

# def read_words(filename):
#     return open(filename).read().split()

# def main(filename):
#     _,ext = os.path.splitext(filename)
#     if ext == '.py':
#         print('This is a Python program file.')
#     elif ext == '.c':
#         print('This is a C program file.')
#     elif ext == '.txt':
#         print('This is a text file.')
#     frequency = word_frequency(read_words(filename))
#     # sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
#     for word in reversed(frequency):
#         print(word)

# if __name__ == "__main__":
#     import sys
#     main(sys.argv[1])


############################################################

# def valuesort(dict1):
#     return [values for keys,values in sorted(dict1.items())]

# result = valuesort({'x': 1, 'y': 2, 'a': 3})
# print(result)



#####################################################

# def invertdict(x):
#     return {value:key for key,value in x.items()}

# result = invertdict({'x': 1, 'y': 2, 'z': 3})
# print(result)



######################################################

##Python Execution Environment ----globals()

# print(globals())

# x = 1
# globals()['x']=2
# print(x)




## locals()

# def f(a,b):
#     print(locals())
    
# print(f(1, 2))

# def f(name):
#     return "Hello %(name)s "% locals()

# print(f("nizam"))

