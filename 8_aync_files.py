# import requests
# from time import time
#
# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
#
# def save_file(response):
#     name = response.url.split('/')[-1]
#
#     with open(name, 'wb') as file:
#         file.write(response.content)
#
#
# def main():
#     start = time()
#     url = "https://loremflickr.com/320/240"
#
#     for _ in range(10):
#         save_file(get_file(url))
#
#     print(time() - start)
#
#
# if __name__ == '__main__':
#     main()

#######################################################################
import asyncio
