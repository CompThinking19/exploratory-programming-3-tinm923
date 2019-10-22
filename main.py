import re

def readString(toRead):
    if type(toRead) != str:
        raise TypeError("Argument is not a string!")
    ending = re.findall("[A-Za-z]+at ",toRead)
    filtered = filter(lambda x: len(x) > 4, ending)
    return filtered

source = open('pg1342.txt')
pride = source.read()
readString(pride)