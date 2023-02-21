class AnagramChecker:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def check_anagram(self):
        if len(self.word1) != len(self.word2):
            return 'Words are not equal length'

        for char in self.word1:
            if char not in self.word2:
                return 'Not anagram'
            self.word2 = self.word2.replace(char, '', 1)

        if len(self.word2) == 0:
            return 'Is Anagram'
        else:
            return 'Not anagram'


while True:
    word1 = input('Anagram 1: ')
    word2 = input('Anagram 2: ')

    checker = AnagramChecker(word1, word2)
    result = checker.check_anagram()
    print(result)

    leave_loop = input("Exit? (Yes/No)")
    if leave_loop.lower() == "yes":
        break
