# import requests
# import json

# def get_external_ip():
#     response = requests.get('https://www.expertzlab.com/')
#     data = json.loads(response.text)
#     return data['origin']

# if __name__ == "__main__":
#     print(get_external_ip())




# import requests
# from urllib.parse import urlparse

# def get_external_ip():
#     response = requests.get('https://www.expertzlab.com/')
#     url = response.url
#     parsed_url = urlparse(url)
#     ip_address = parsed_url.netloc
#     return ip_address

# if __name__ == "__main__":
#     print(get_external_ip())







# import requests

# def get_response_format(url):
#     response = requests.get(url)
#     content_type = response.headers.get('Content-Type')

#     if 'json' in content_type:
#         return 'JSON'
#     elif 'xml' in content_type:
#         return 'XML'
#     elif 'text' in content_type:
#         return 'Text'
#     else:
#         return 'Unknown'

# if __name__ == "__main__":
#     url = 'https://www.expertzlab.com/'
#     format = get_response_format(url)
#     print(f'The response format for {url} is {format}')




import socket

def get_ip_address(url):
    try:
        hostname = socket.gethostbyname(url)
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

if __name__ == "__main__":
    url = 'www.expertzlab.com'
    ip_address = get_ip_address(url)
    if ip_address:
        print(f'The IP address for {url} is {ip_address}')
    else:
        print(f'Could not find the IP address for {url}')
