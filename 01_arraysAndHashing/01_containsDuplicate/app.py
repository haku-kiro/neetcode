# This has a time complexity of o(n) but also a space complexity of o(n)
# the alternative would be to iterate over the numbers twice, i.e. brute force solution.
def containsDuplicate(numbers):
    hashset = set()
    for n in numbers:
        if n in hashset:
            return True
        hashset.add(n)

    return False

# This is how I would solve it back in the day
def containsDuplicateMike(numbers):
    check = set(numbers)
    if len(check) == len(numbers):
        return False
    return True

# Well, I'd do something like this
containsDuplicateMike = lambda n : False if len(set(n)) == len(n) else True

if __name__ == "__main__":
    someData = [1, 2, 3, 4, 5, 1]
    duplicates = containsDuplicate(someData)
    print(duplicates)
    print(containsDuplicateMike(someData))
