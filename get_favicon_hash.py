import requests
import mmh3
import base64
import favicon

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

def get_valid_url():
    while True:
        url = input("Enter URL to get the mmh3-HASH: ")
        if "://" in url:
            return url
        print("Invalid URL. Please include a schema (e.g., http://).")

def get_favicon_url(url):
    if url.lower().endswith((".ico", ".jpg", ".png", ".gif")):
        return url
    icons = favicon.get(url, headers=HEADERS)
    if icons:
        return icons[0].url
    print("No favicon found. Try using the direct URL (e.g., {}/favicon.ico).".format(url))
    exit()

def fetch_and_hash_favicon(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Ensure we notice bad responses
    icon_data = base64.b64encode(response.content)
    return mmh3.hash(icon_data)

def print_results(hash_value):
    print(f"Hash: {hash_value}")
    print(f"Use this on Shodan for searching, http.favicon.hash:{hash_value}")
    print(f"\t or press here: https://www.shodan.io/search?query=http.favicon.hash%3A{hash_value}")
    print(f'Use this on ZoomEye for searching, iconhash:"{hash_value}"')
    print(f"\t or press here: https://www.zoomeye.org/searchResult?q=iconhash%3A%20%22{hash_value}%22")

def main():
    url = get_valid_url()
    favicon_url = get_favicon_url(url)
    hash_value = fetch_and_hash_favicon(favicon_url)
    print_results(hash_value)

if __name__ == "__main__":
    main()
