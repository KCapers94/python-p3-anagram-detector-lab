# your code goes here!


class Anagram:

    def __init__(self, word = "listen"):
        self._match = word

    def is_anagram(self,canidate):
        return sorted(canidate) == sorted(self._match)
    
    def match(self, words):
            return [word for word in words if self.is_anagram(word)]
    
    