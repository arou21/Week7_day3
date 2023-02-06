# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# def twoString():
#     ransomeNote = [""]
#     magazine = [""]

#     for letter in ransomeNote:
#         if letter == magazine:
#             return True
#         print(ransomeNote)

#     else:
#         return False

# print(twoString)


def words(ransomeNote, magazine):
    letters = {}
    for letter in ransomeNote:
        if letter not in letters:
            letters[letter] =1

        else:
            letters[letter] += 1
            if letter in letters:
                letters[letter] -=1
        for x in letters.values(): # makes a list from the dictionary
            if x > 0: 
                return False
        return True

print(words('aa', 'aab'))




