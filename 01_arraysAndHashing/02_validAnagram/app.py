# there's two obvious ways to determine a string is anagram of another,
# 1. Create a hash map of each string, using the count of the char as the value
#    iterate over and check that they're the same
# 2. Sort both and iterate over them checking that each char is the same.


def createMap(s):
    result = {}
    for character in s:
        exists = result.get(character, False)
        if not exists:
            result[character] = 1
        else:
            result[character] += 1

    return result


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sHash, tHash = createMap(s), createMap(t)

    for c in sHash:
        exists = tHash.get(c, False)
        if not exists:
            return False
        else:
            if exists != sHash[c]:
                return False

    return True


if __name__ == "__main__":
    s = "anagram"
    t = "anagram"
    anagram = isAnagram(s, t)
    print(anagram)
