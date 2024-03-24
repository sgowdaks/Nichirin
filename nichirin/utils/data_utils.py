import yaml

from urllib.parse import urlparse


def load_yaml(path):
    with open(path, "r") as stream:
        return yaml.safe_load(stream)


def is_valid_url(root, url):
    # Check if a URL is valid.
    parsed_url = urlparse(url) 
    if bool(parsed_url.scheme) and bool(parsed_url.netloc):
        return url
    
    if bool(parsed_url.path) and not url.startswith(("java", "javascript")):
        return root + url
    return False


def filter_urls(root, urls):
    # Filter out unwanted URLs.
    filtered_urls = []
    for url in urls:
        output = is_valid_url(root, url) 
        if not isinstance(output, bool):
            filtered_urls.append(output)
    return filtered_urls


def validate_url(root, urls):
    filtered_urls = filter_urls(root, urls)
    return filtered_urls
