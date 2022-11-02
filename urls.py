import re
from urllib import request 

# # EG. 1: shrunk_url("http://example.com")` => example.com
# # EG. 2: domain_of_url("http://one.example.com/help/me") => example.com
# # EG. 3: url_list('http(s)://subdomain.example.com/path1/path2/') => ['http(s)://', 'subdomain', 'example', 'com', 'path1', 'path2']
# # (s) means it should work with both https and http protocols

# url = "http://example.com"
# shrunk_url = print(url[7:])

# domain_of_url = "http://one.example.com/help/me"
# domain_extracted = print(domain_of_url[11:22])

# def shrunk_url(url,shrunk_url):
#     return shrunk_url

# print(shrunk_url)


# def domain_of_url(domain_of_url, domain_extracted):
#     return domain_extracted


# print(domain_extracted)


# url = 'https://subdomain.example.com/path1/path2/'
# # Create a list of each bit between slashes
# slashparts = url.split('/')
# # Now join back the first three sections 'http:', '' and 'example.com'
# basename = '/'.join(slashparts[:3]) + '/'
# # All except the last one
# dirname = '/'.join(slashparts[:-1]) + '/'
# test = url.split(".")
# print ('slashparts = %s' % slashparts)
# print (test)

url = "https://subdomain.example.com/path1/path2/"
slashed = url.split('/')
blank = []
temporary = blank.append(slashed)
temporary2 = url.split(".")


def url_list():
    return()

print(blank)
print(slashed)
print(temporary)