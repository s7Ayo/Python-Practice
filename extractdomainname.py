import re


def domain_name(url):
    pattern = re.compile(r'(?:https?://)?(?:www\.)?([a-z0-9-]+)\.[a-z]{2,}(?:/[a-z0-9-]+)*', re.IGNORECASE)
    match = re.search(pattern, url)
    if match:
        return match.group(1)  # return the first capturing group

    print(domain_name("https://google.com"))
    
    pass
domain_name("https://google.com")
