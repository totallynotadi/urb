"""
yet anotehr wrapper around teh Urban Dictionary API
provides methods to get results for queried words as well as random words
"""

import sys
import json
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote
else:
    from urllib.request import urlopen
    from urllib.parse import quote


UD_DEFINE_URL = 'https://api.urbandictionary.com/v0/define?term='
UD_RANDOM_URL = 'https://api.urbandictionary.com/v0/random'

class UrbanDefinition():
    def __init__(self, word, definition, example, author, upvotes, downvotes, id) -> None:
        self.word = word
        self.definition = definition
        self.example = example
        self.author = author
        self.thumbs_up = upvotes
        self.thumbs_down  = downvotes
        self.id = id

def _get_urban_json(url: str) -> json:
    f = urlopen(url)
    data = json.loads(f.read().decode('utf-8'))
    f.close()
    return data

def _parse_urban_json(json_response):
    result = []
    # print(json_response)
    # [print(key, ': ', json_response['list'][0][key]) for key in json_response['list'][0].keys()]
    if json_response is None or any([e in json_response for e in ('ERROR', 'error')]):
        raise ValueError("Urb: invalid request")
    if 'list' not in json_response or len(json_response['list']) < 1:
        return result
    for definition in json_response['list']:
        d = UrbanDefinition(
            definition['word'],
            definition['definition'],   
            definition['example'],
            definition['author'],
            definition['thumbs_up'],
            definition['thumbs_down'],
            definition['defid']
            )
        result.append(d)
    return result

def define(term):
    json_response = _get_urban_json(UD_DEFINE_URL + quote(term))
    return _parse_urban_json(json_response)

def random():
    json_response = _get_urban_json(UD_RANDOM_URL)
    return _parse_urban_json(json_response)

if __name__ == '__main__':
    print(random())
