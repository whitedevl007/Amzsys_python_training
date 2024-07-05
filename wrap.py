import textwrap

def wrap_text(filename, width):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        wrapped_line = textwrap.wrap(line, width)
        for part in wrapped_line:
            print(part)
wrapp=wrap_text('she.txt',30)
print(wrapp)


