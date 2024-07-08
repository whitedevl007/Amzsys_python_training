# import subprocess

# def doc_details(name):
#     command = f'python -m pydoc {name}'
#     result = subprocess.run(command, capture_output=True, text=True, shell=True)
#     if result.returncode != 0:
#         raise Exception(f'Command {command} failed with error: {result.stderr}')
#     return result.stdout

# module = input("Enter a module name: ")
# details = doc_details(module)
# print(details)





# import inspect
# import sys

# def print_module_docstring(module):
#     """Print the docstring for a module."""
#     print(module.__doc__)

# def print_function_docstrings(module):
#     """Print the docstrings for all functions in a module."""
#     print("\nFUNCTIONS\n")
#     for name, obj in inspect.getmembers(module):
#         if inspect.isfunction(obj):
#             print(f"{name}()")
#             print(obj.__doc__)
#             print()

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python mydoc.py <module>")
#         sys.exit(1)

#     module_name = sys.argv[1]
#     module = __import__(module_name)

#     print(f"Help on module {module_name}:")
#     print()
#     print_module_docstring(module)
#     print_function_docstrings(module)

# if __name__ == "__main__":
#     main()
