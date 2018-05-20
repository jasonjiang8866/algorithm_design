from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *

class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 


def httpget(url):
    parsed = urlsplit(url)
    if not parsed.scheme: #protocol insertion
        url = 'http://'+url
    elif parsed.scheme != 'http':
        raise ValueError("Unknown protocol")
    try:
        return urlopen(url).read()
    except HTTPError as e:
        raise InternetFail(e)
    except URLError as e:
        raise ValueError(e)
    except Exception as e:
        raise Exception(e)

URLS = [["","impossible.txt"],["http://google.com/login","fail.txt"]]

def download_URLs(URL_filenames):
    for item in URLS:
        url=item[0]
        filename=item[1]
        try:
            contents=httpget(url)
            with open(filename , 'wb') as myFile:
                myFile.write(contents)
        except (InternetFail, ValueError) as e:
            pass
        except Exception as e:
            raise Exception(e)

