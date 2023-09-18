# group anagrams, two possible ways to solve,
# 1. You could sort each string in the list - then check if equal and
#    if so - append to same list, combine lists as result.
# 2. Count all the characters of each word to create a unique key - create hash map with
#    that key, and the value a list of strings that have that key.

# Note, using python3 annotations here because I've never done it and type safety is cool.

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        result[tuple(count)].append(s)

    return list(result.values())


if __name__ == "__main__":
    testData = ["tea", "eat", "fun", "nuf", "ufn", "god", "dog", "asdfasdf", "asd"]
    result = groupAnagrams(testData)
    print(result)
