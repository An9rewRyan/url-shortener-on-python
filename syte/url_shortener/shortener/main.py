import re
from hashids import Hashids
from random import randint

def shorten(longLink):
    data = re.compile(r'https\:\/\/.*\/.*')

    mo = data.search(longLink)
    if mo != None:


        hashids = Hashids(min_length=7)
        hash = hashids.encode(randint(1,1000))

        shortLink = 'http://localhost:8000/main/' + str(hash)
        return hash
    else:
        return 0


