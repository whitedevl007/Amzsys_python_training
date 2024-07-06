# import urllib.request
# import re

# def antihtml(url):
#     response = urllib.request.urlopen(url)
#     if response.getcode() == 200:
#         content = response.read().decode()
#         clean_text = re.sub('<[^>]*>', '', content)
#         return clean_text
#     else:
#         return "Failed to fetch data from URL"

# result = antihtml('http://docs.python.org/tutorial/index.html')
# print(result)
