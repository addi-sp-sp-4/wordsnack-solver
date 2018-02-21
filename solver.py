from typing import *

from sys import argv


def is_part_anagram(word: str, charset: str) -> bool:
    """
    Checks if `word` can be formed with the characters from `charset`. 
    Every character in `charset` can only be used once, so: 
    
        For `word` = "cookie" and `charset` = "eocik"  returns False
        For `word` = "cookie" and `charset` = "eociko" returns True
    """

    for character in word:
        if character not in charset:
            return False

        charset = charset.replace(character, '', 1)

    return True




def main() -> None:

    charset = argv[1]
    wordlist = argv[2]
    min_wordlen = int(argv[3]) if len(argv) == 4 else 2

    with open(wordlist, 'r') as wlist:
        
        found = []

        while True:

            read_word = wlist.readline()
            
            # EOF

            if read_word == '':
                break
            
            # Remove newline since it is unneeded
            read_word = read_word[:-1]

            if len(read_word) < min_wordlen:
                continue

            if is_part_anagram(read_word, charset):
                found.append(read_word)


        found = sorted(found, key=lambda x: len(x), reverse=True)

        for word in found:
            print("[+] {}:{}".format(len(word), word))

    pass


if __name__ == "__main__":
    main()

