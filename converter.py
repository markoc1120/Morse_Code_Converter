import re


class Converter:
    def __init__(self):
        self.morse_dict = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}
        self.code = []

    def encrypt(self, msg):
        msg = re.sub(r'[^a-zA-Z0-9|.|-|,|/|?|(|) ] ', r'', msg)
        msg = msg.upper().split(' ')
        for word in msg:
            self.code.append(self.encrypt_word(word))

        return ' / '.join(self.code)

    def encrypt_word(self, word):
        result = []
        for letter in word:
            try:
                result.append(self.morse_dict[letter])
            except KeyError:
                pass
        return ' '.join(result)
