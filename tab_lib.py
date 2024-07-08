# import tablib

# # create a dataset
# data = tablib.Dataset()

# Add rows
# data.append(["A", 1])
# data.append(["B", 2])
# data.append(["C", 3])

# with open('test.csv', 'w') as f:
#     f.write(data.csv)
    
# with open('test.xls', 'wb') as f:
#     f.write(data.export('xls'))





# import tablib

# sheet1 = tablib.Dataset()
# sheet1.append(["A1", 1])
# sheet1.append(["A2", 2])

# sheet2 = tablib.Dataset()
# sheet2.append(["B1", 1])
# sheet2.append(["B2", 2])


# book = tablib.Databook([sheet1, sheet2])
# with open('book.xls', 'wb') as f:
#     f.write(book.export('xls'))