import csv
import collections

class Anagrams:
    def __init__(self, filename):
        self.filename = filename
        self.anagrams = collections.defaultdict(list)
    
    def read_file(self):
        