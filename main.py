import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, link):
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {'long_url': link}
    response = requests.post(bitly_url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    parsed_url = urlparse(link)
    link = '{0}{1}'.format(parsed_url.netloc, parsed_url.path)
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'
    url = url_template.format(link)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, link):
    parsed_url = urlparse(link)
    link = '{0}{1}'.format(parsed_url.netloc, parsed_url.path)
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{0}'
    url = url_template.format(link)
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(
        description='Сокращение ссылок с помощью Битли'
    )
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    link = args.link

    try:
        if is_bitlink(bitly_token, link):
            total_clicks = count_clicks(bitly_token, link)
            print('Количество переходов по ссылке битли:', total_clicks)
        else:
            bitlink = shorten_link(bitly_token, link)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print('Введена неправильная ссылка')


if __name__ == '__main__':
    main()
