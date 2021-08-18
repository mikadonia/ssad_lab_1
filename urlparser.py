import requests
import argparse
import re

def getDataByURL(url, post):
    data = ''
    if post:
        r = requests.post(url)
        data = r.text
    else:
        r = requests.get(url)
        data = r.text
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get page content by URL!')
    parser.add_argument('-u', '--url', required=True, action='store', help='URL to parse')
    parser.add_argument('-f', '--file-name', required=True, action='store', help='File where to write the page')
    parser.add_argument('--POST', default=False, action='store_true', help='Send POST request')
    args = parser.parse_args()

    if not re.fullmatch('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', args.url):
        print('URL is not valid!')
        exit()

    data = ''
    try:
        data = getDataByURL(args.url, args.POST)
        with open(args.file_name, 'w') as f:
            f.write(data)
    except Exception:
        print('Something wnt wrong... Check arguments!')
