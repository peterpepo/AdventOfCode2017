from puzzle_commons.puzzle_commons import read_puzzle_input
import os, re


def solve():
    """Advent Of Code 2017 - Day 04 Solution.

    :return: tuple(part_a_result[int], part_b_result[int])
    """
    def containsDuplicateWords(sourceString):
        """Checks string containing duplicate words.

        :param sourceString: string to check for duplicate words
        :return: [boolean] does string contains duplicate words
        """
        """Regexp explanation: (?:^|\s)([a-zA-Z]+)\s.*\1(?:$|\s)
        (?:^|\s)    - beginning of a string or whitespace
        ([a-zA-Z]+) - sequence on 1..n alpha characters
        \s.*        - whitespace followed by sequence of any characters
        \1          - backreference to 1st capture group (same sequence returned by ([a-zA-Z]+))
        (?:$|\s)    - end of line or whitespace
        """
        regex_pattern = r"(?:^|\s)([a-zA-Z]+)\s.*\1(?:$|\s)"
        return re.search(regex_pattern, sourceString) is not None

    def containsAnagram(sourceString):
        """Checks string containing anagrams.
        An anagram is word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        Anagram: https://en.wikipedia.org/wiki/Anagram

        :param sourceString:
        :return: [boolean] does string contains anagram
        """
        words = [str.strip(word) for word in sourceString.split(" ")]

        def isWordAnagramOfWord(word_one, word_two):
            # Set of characters used in both words
            words_characters = set(word_one + word_two)

            # Check count of each character matching between words
            for character in words_characters:
                # If count for any mismatch, these words are not anagrams
                if word_one.count(character) != word_two.count(character):
                    return False

            # Words are anagrapgs, when no mismatch has been found
            return True

        # Loop through all words from beginning to last-1
        for current_word_index in range(len(words) - 1):
            # Loop from next word to last word
            for next_word_index in range(current_word_index + 1, len(words)):
                # Check, whether words are anagrams. Once first is anagram is found, we know that string contains anagram.
                if isWordAnagramOfWord(words[current_word_index], words[next_word_index]):
                    return True
        # No anagram was found
        return False

    puzzle_a_valid_passphrases_count = 0
    puzzle_b_valid_passphrases_count = 0

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_04_input.txt"):

        # Part-A
        if not containsDuplicateWords(puzzle_input):
            puzzle_a_valid_passphrases_count += 1

        # Part-B
        if not containsAnagram(puzzle_input):
            puzzle_b_valid_passphrases_count += 1

    return puzzle_a_valid_passphrases_count, puzzle_b_valid_passphrases_count
