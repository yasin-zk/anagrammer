import csv
import collections

class Anagrams:
    def __init__(self, filename):
        self.filename = filename
        self.anagrams = collections.defaultdict(list)
    
    def read_file(self):
        with open(self.filename, 'r') as fil:
            reader = csv.reader(fil)
            for row in reader:
                for word in row:
                    pass

    def add_word(self, word):
        sorted_word = ''.join(sorted(word.strip().lower()))
        self.anagrams[sorted_word].append(word)

    def get_anagrams(self):
        pass

    