import string
import timeit
from binaryEx import *
asciiLetters = (string.ascii_letters)


def convertToShortenedStr(binaryString, number):
    start = timeit.default_timer()
    shortenedBinaryDict = {}
    shortenedStr = ''
    i = 0
    j = 0
    while i != len(binaryString):
        # print(i, j, shortenedBinaryDict)
        nextGroup = (binaryString[i:i + number])
        if nextGroup not in shortenedBinaryDict:
            shortenedBinaryDict[nextGroup] = asciiLetters[j]
            j += 1
        shortenedStr += shortenedBinaryDict[nextGroup]
        i += number
    print('-'*60, 'STARTING', '-'*60)
    print('original binary string: ', binaryString)
    print('shortenedStr: ', shortenedStr)
    print(f'Length of original string: {len(binaryString)}')
    print(f'Length of shortened string: {len(shortenedStr)}')
    print(f'A {int(len(binaryString)/len(shortenedStr) *100)}% impovement!')
    stop = timeit.default_timer()
    print('Time: ', stop - start)


convertToShortenedStr(binary1, 3)
convertToShortenedStr(binary2, 3)
convertToShortenedStr(binary1, 4)
convertToShortenedStr(binary2, 4)
convertToShortenedStr(binary1, 5)
convertToShortenedStr(binary2, 5)
convertToShortenedStr(binary1, 6)
convertToShortenedStr(binary2, 6)
# base 5 has enough characters in ascii to use as a solid base with out a fear of something breaking
convertToShortenedStr(binary3, 5)
convertToShortenedStr(binary4, 5)
convertToShortenedStr(binary5, 5)


# convertToShortenedStr(binary1, 7)
# convertToShortenedStr(binary2, 7)
