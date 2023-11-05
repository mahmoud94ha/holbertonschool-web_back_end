import requests
import time
from functools import wraps

def cache_results(expiration_time):
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(url):
            now = time.time()
            if url in cache and now - cache[url]["timestamp"] < expiration_time:
                cache[url]["count"] += 1
                return cache[url]["content"]
            
            content = func(url)
            cache[url] = {
                "content": content,
                "timestamp": time.time(),
                "count": 1
            }
            return content

        return wrapper
    return decorator

@cache_results(expiration_time=10)
def get_page(url):
    response = requests.get(url)
    return response.text