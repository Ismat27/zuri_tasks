def find_anagrams(str1, str2):
    for e in str1.lower():
        if e not in str2.lower():
            return False
    return True

print(find_anagrams('Heavy Rain', 'Hire a Navy'))
print(find_anagrams("below", "elbow"))
print(find_anagrams("hello", "check"))