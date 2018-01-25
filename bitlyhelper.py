# coding=utf-8
import urllib.request
import json

TOKEN = '466c6e57ec45c2fc360d4603c30bc9ed22fba10f'
ROOT_URL = 'https://api-ssl.bitly.com'
SHORTEN = '/v3/shorten?access_token={}&longUrl={}'

class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            # python3's library urllib, return a HTTP response object,
            response = urllib.request.urlopen(url).read()
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(e)