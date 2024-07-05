def cental_align(filename):
    with open(filename) as f:
        lines =f.readlines()
        for line in lines:
            align = line.center(100)
            print(align)
    
sentences = cental_align('she.txt')