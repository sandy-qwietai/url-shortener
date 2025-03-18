from hashlib import md5
from collections import Counter
from urllib.parse import urlparse

# global variable for storing the data
url_dict = {}
short_url_dict = {}
domain_count_dict = {}

def shorten_url(url: str) -> str:
    """Generate a shortened url."""
    if url in url_dict:
        return url_dict[url]
    # Create a md5 hash of the url provided
    hash_object = md5(str(url).encode())
    short_url = hash_object.hexdigest()[:6]
    url_dict[url] = short_url
    short_url_dict[short_url] = url
    # Increment count of the domain of the url provided
    domain = urlparse(str(url)).netloc
    if domain in domain_count_dict:
        domain_count_dict[domain] = domain_count_dict[domain] + 1
    else:
        domain_count_dict[domain] = 1
    return short_url

def get_original_url(short_url: str) -> str:
    """fetch the original url from a short url."""
    return short_url_dict.get(short_url)

def get_top_domains(limit: int = 3):
    """fetch the top 3 domains that have been shortened the most."""
    sorted_items = sorted(domain_count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # get the top n domains from the sorted list
    top_n_items = sorted_items[:limit]
    
    # converting the list of tuples back to a dict
    top_n_dict = dict(top_n_items)
    
    return top_n_dict