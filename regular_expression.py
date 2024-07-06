# import re

# def make_slug(name):
#     # Replace special characters and spaces with hyphens
#     slug = re.sub(r'[^\w\s]', '-', name)
#     slug = re.sub(r'\s+', '-', slug)

#     # Remove consecutive hyphens
#     slug = re.sub(r'-+', '-', slug)

#     # Remove leading and trailing hyphens
#     slug = slug.strip('-')

#     # Convert to lowercase
#     slug = slug.lower()

#     return slug

# slug = make_slug(" --hello-  world--")
# print(slug)


