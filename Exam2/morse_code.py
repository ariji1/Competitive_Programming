class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        lookup = {"".join(MORSE[ord(c) - ord('a')] for c in word) \
                  for word in words}
        return len(lookup)
s = Solution()
words = ["gin", "zen", "gig", "msg"]
words1 = ["a", "z", "g", "m"]
words2 = ["bhi", "vsv", "sgh", "vbi"]
words3 = ["a", "b", "c", "d"]
words4 = ["hig", "sip", "pot"]
print(s.uniqueMorseRepresentations(words))      
print(s.uniqueMorseRepresentations(words1))
print(s.uniqueMorseRepresentations(words2))
print(s.uniqueMorseRepresentations(words3))
print(s.uniqueMorseRepresentations(words4))
