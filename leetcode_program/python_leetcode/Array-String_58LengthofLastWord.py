class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the sentence into words
        #ここが結構重要というか新発見な部分
        words = s.split()
        # Get the last word
        last_word = words[-1]
        # print(last_word)
        return len(last_word)