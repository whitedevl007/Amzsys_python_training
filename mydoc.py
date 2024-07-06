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
