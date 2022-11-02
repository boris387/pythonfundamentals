def shrunk_url(url, shrunk_list=['http://','https://']):
    for x in shrunk_list:
        url = url.replace(x, '')
    return url
    
    
def domain_url(url):
    url = shrunk_url(url)
    url = url.split("/")[0] #Split by the /
    url = url.split(".")[-2:] #Then split by the .
    url = ".".join(url) #
    return url


def url_list(url):
    # 2 consecutive forward slashes are only protocol-related
    input = url.split("//")
    if len(input) > 2:
        print('The type of the url is not supported')
    output = []

    # Add protocol with slashes as the task requires
    output += [input[0]+ "//"]
    
    # Prepare the rest of the elements
    elements = input[1].split('/')
    # Add domain information (Assume that it comes first after protocol)
    output += elements[0].split('.')
    # Add rest of the paths if they are not empty str
    for element in elements[1:]:
        if len(element) > 0:
            output += [element]
    return output

url = "http://one.example.com/help/me"

print(shrunk_url(url))
print(domain_url(url))
print(url_list(url))