# import os
# from urllib.parse import urlparse
# import requests

# def download_file(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         filename = os.path.basename(urlparse(url).path)
#         if filename == '' or url.endswith('/'):
#             filename = 'index.html'
#         with open(filename, 'wb') as file:
#             file.write(response.content)
#         print(f'File {filename} downloaded successfully.')
#     else:
#         print(f'Failed to download file from {url}.')




# # URL = 'http://docs.python.org/tutorial/interpreter.html'
# URL= 'http://docs.python.org/tutorial/'
# print(download_file(URL))



