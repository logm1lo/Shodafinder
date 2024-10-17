import requests
import mmh3
import base64
import favicon

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

class FaviconHash:
    def __init__(self, url):
        self.url = url

    def get_favicon_url(self):
        """Get the favicon URL from the website."""
        if self.url.lower().endswith((".ico", ".jpg", ".png", ".gif")):
            return self.url
        try:
            icons = favicon.get(self.url, headers=HEADERS)
            if icons:
                return icons[0].url
        except Exception as e:
            raise RuntimeError(f"Error fetching favicon: {e}")

        raise RuntimeError("No favicon found. Try using the direct URL (e.g., {}/favicon.ico).".format(self.url))

    def fetch_and_hash_favicon(self, favicon_url):
        """Fetch the favicon and calculate its mmh3 hash."""
        try:
            response = requests.get(favicon_url, headers=HEADERS)
            response.raise_for_status()
            icon_data = base64.b64encode(response.content)
            return mmh3.hash(icon_data)
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching favicon from {favicon_url}: {e}")

    @staticmethod
    def print_results(hash_value):
        """Print the hash and provide useful links."""
        print(f"Hash: {hash_value}")
        print(f"Use this on Shodan for searching, http.favicon.hash:{hash_value}")
        print(f"\t or press here: https://www.shodan.io/search?query=http.favicon.hash%3A{hash_value}")
        print(f'Use this on ZoomEye for searching, iconhash:"{hash_value}"')
        print(f"\t or press here: https://www.zoomeye.org/searchResult?q=iconhash%3A%20%22{hash_value}%22")

def main(url):
    """Main entry point for the CLI."""
    favicon_hash = FaviconHash(url)
    favicon_url = favicon_hash.get_favicon_url()
    hash_value = favicon_hash.fetch_and_hash_favicon(favicon_url)
    favicon_hash.print_results(hash_value)

