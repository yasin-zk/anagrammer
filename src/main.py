from anagram_class import Anagrams
import argparse
from anagram_testing import TestAnagrams

def main():
    #CLI: py main.py population.txt
    parser = argparse.ArgumentParser(description='Find anagrams in a file')
    parser.add_argument('filename', type=str, help='filename of anagram .txt file ')
    parser.add_argument('debug', type=str, help='YES or NO for testing')
    args = parser.parse_args()

    anagram_finder = Anagrams(args.filename)
    anagram_finder.read_file()

    anagrams, duplicates = anagram_finder.get_anagrams()

    print('Anagrams:')
    for anagram in anagrams:
        print(anagram)
    


if __name__ == '__main__':
    main()
