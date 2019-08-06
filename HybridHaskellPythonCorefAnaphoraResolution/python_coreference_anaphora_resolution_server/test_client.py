from __future__ import print_function

from urllib.request import Request, urlopen
import urllib

base_uri = 'http://127.0.0.1:8000?text='


def coref(text, no_detail=False):
  def get_raw_data_from_web(a_uri):
    req = Request(a_uri, headers={'User-Agent': 'PythonBook/1.0'})
    http_response = urlopen(req)
    data = http_response.read()
    return data

  encoded_text = urllib.parse.quote(text, safe='')
  if no_detail:
    z = '&no_detail=1'
  else:
    z = ''
  raw_data = get_raw_data_from_web(base_uri + encoded_text + z)
  return raw_data.decode("UTF8")


print(coref('My sister has a dog named Sam. She loves him'))
print(coref('My sister has a dog named Sam. She loves him', no_detail=True))
