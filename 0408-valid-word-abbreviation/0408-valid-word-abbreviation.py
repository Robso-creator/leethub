"""
input hello, h3o

wp = 4
ap = 2


"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == "0": 
                    return False
                if abbr_ptr >= len(abbr): 
                    return False

                skip = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    skip = skip * 10 + int(abbr[abbr_ptr])

                    abbr_ptr +=1
                word_ptr += skip
            else:
                if word_ptr >= len(word) or word[word_ptr] != abbr[abbr_ptr]: 
                    return False

                word_ptr += 1
                abbr_ptr += 1

        return word_ptr == len(word) and abbr_ptr == len(abbr)


#: T: O(n) where n is amoujmt
#: S: O(1)