binary1 = '101010100101'


def convertTriSectionToSingle(str):
    print(len(str))
    i = 0
    while i is not len(str):
        print(str[i: i + 3])
        i += 3


convertTriSectionToSingle(binary1)
