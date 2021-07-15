import re
from hashids import Hashids
from random import randint
from main.models import Link

def shorten(longLink):
    data = re.compile(r'https\:\/\/.*\/.*')

    mo = data.search(longLink)
    if mo != None:


        hashids = Hashids(min_length=7)
        link = Link.objects.latest('linkId')

        hash = hashids.encode(link.linkId)

        shortLink = 'http://localhost:8000/main/' + str(hash)
        return hash
    else:
        return 0


