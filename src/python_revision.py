# this is a comment

def isAnagram():
    '''
    (word1) - > input
    (word2) - > input
    Check if word is anagram
    '''

    word1 = input('Anagram 1 : ')
    word2 = input('Anagram 2 : ')
    if(len(word1) != len(word2)):
        return 'Words are not equal length' # throw error message The words are not equal length.
    
    for char in word1:
        if char not in word2:
            return 'Not anagram' #False
        return 'is Anagram' #True

print(isAnagram())

