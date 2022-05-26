# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def isAnagram(str1, str2):
    # unequal length strings cannot be anagrams
    if len(str1) != len(str2):
        return False

    # sort for the strings
    first = sorted(str1)
    second = sorted(str2)

    # check if both strings are the same
    if first == second:
        return True
    else:
        return False

result = isAnagram("desserts" , "stressed")
print(result)