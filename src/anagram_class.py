import csv
import collections

class Anagrams:
    def __init__(self, filename):
        self.filename = filename
        self.anagrams = collections.defaultdict(list)

    def read_file(self):
        # Open the file and read all lines
        with open(self.filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                words = line.strip().split()
                # Loop through each word and add it to the anagrams dictionary
                for word in words:
                    self.add_word(word)

    def add_word(self, word):
        sorted_word = ''.join(sorted(word.strip().lower()))
        # Check if the sorted word is already in an existing anagram list, if yes return
        for anagram in self.anagrams.values():
            if sorted_word in anagram:
                return

        # If sorted word is not already in an anagram list, add it
        self.anagrams[sorted_word].append(word)

    def get_anagrams(self):
        anagrams = []
        duplicates = []

        # Loop through each key and value in the anagrams dictionary
        for sorted_word, words in self.anagrams.items():
            if len(words) > 1:
                if sorted_word not in anagrams:
                    anagrams.append(sorted_word)
                else:
                    duplicates.append(sorted_word)

        # Return tuples containing anagrams and duplicates
        return anagrams, duplicates
