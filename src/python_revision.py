def isAnagram():
    '''
    (word1) - > input
    (word2) - > input
    Check if word is anagram
    '''

    word1 = input('Anagram 1: ')
    word2 = input('Anagram 2: ')
    if len(word1) != len(word2):
        return 'Words are not equal length' # throw error message The words are not equal length.

    for char in word1:
        if char not in word2:
            return 'Not anagram' # False
        # remove the character from word2 so it's not matched again
        word2 = word2.replace(char, '', 1)

    # make sure all characters in word1 have been matched
    if len(word2) == 0:
        return 'Is Anagram' # True
    else:
        return 'Not anagram' # False


while True:
    result = isAnagram()
    print(result)
    if result == "Not anagram":
        continue
    leaveloop = input("Exit? (Yes/No) ")
    if leaveloop.upper() == "YES":
        break

