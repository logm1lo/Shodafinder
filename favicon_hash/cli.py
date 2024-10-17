import argparse
from . import main

def run():
    parser = argparse.ArgumentParser(description="Fetch and hash favicons for Shodan and ZoomEye searches.")
    parser.add_argument('-u', '--url',required=True,help="The URL to fetch the favicon from. Example: -u http://example.com")
    args = parser.parse_args()

    main(args.url)

