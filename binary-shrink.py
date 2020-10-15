import string
asciiLetters = (string.ascii_letters)


binary1 = '101010100101101010100101101010100101101010100101101010100101101010100101'


def convertTriSectionToSingle(binaryString):
    shortenedBinaryDict = {}
    print('here is the dict: ', shortenedBinaryDict)
    shortenedStr = ''
    i = 0
    j = 0
    while i is not len(binaryString):
        print(shortenedBinaryDict)
        nextThree = (binaryString[i:i + 3])
        if nextThree not in shortenedBinaryDict:
            shortenedBinaryDict[nextThree] = asciiLetters[j]
            j += 1
        shortenedStr += shortenedBinaryDict[nextThree]
        i += 3

    print('original binary string: ', binaryString)
    print('shortenedStr: ', shortenedStr)
    print(f'Length of original string: {len(binaryString)}')
    print(f'Length of shortened string: {len(shortenedStr)}')
    print(f'A {int(len(binaryString)/len(shortenedStr) *100)}% impovement!')


convertTriSectionToSingle(binary1)
