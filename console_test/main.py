import re
from hashids import Hashids
from random import randint

while True:
    longLink = str(input("Print your link: "))

    data = re.compile(r'https\:\/\/.*\/.*')

    mo = data.search(longLink)
    if mo != None:
        print("Link is correct!")
        break
    else:
        print("Link is not correct!")

domen = re.compile(r'https\:\/\/.*\/')
mainLink = domen.search(longLink)

hashids = Hashids(min_length=7)
hash = hashids.encode(randint(1,1000))

shortLink = str(mainLink.group()) + str(hash)

print(shortLink)

