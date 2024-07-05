# f=open('nizam.txt','r')
# print(f.readline())
# print(f.readlines()) --returns all contetnts in a single list
# for i in f:
#     print(i)


# f=open('nizam.txt','a')
# f.writelines(['a\n', 'b\n', 'c\n'])
# f.close()

###################################################

# def charcount(filename):
#     return len(open(filename).read())

# count = charcount('nizam.txt')
# print(count)

###################################################

# def wordcount(filename):
#     return len(open(filename).read().split())

# spt=wordcount('nizam.txt')
# print(spt)


##############################################

def linecount(filename):
    return len(open(filename).readlines())

reads = linecount('nizam.txt')
print(reads)