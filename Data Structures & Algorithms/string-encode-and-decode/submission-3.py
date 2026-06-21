class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            cnt = len(word)
            word = str(cnt) + '*' + word
            encoded_string += word
        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string, i = [], 0
        while i < len(s):

            j = i

            if (s[i].isdigit()):
                while s[j] != '*':
                    j += 1

                word_length = int(s[i:j])

                j += 1

                decoded_string.append(s[j : j + word_length])

                i = word_length + j

        return decoded_string
