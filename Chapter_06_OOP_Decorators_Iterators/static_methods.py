class StringUtil:

    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # Allow only letters and numbers, discard the rest
        s = "".join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

def main():
    print(StringUtil.is_palindrome("Radar", False))
    print(StringUtil.is_palindrome("Radar"))
    print(StringUtil.is_palindrome("A nut for a jar of Tuna"))
    print(StringUtil.is_palindrome("Never Odd, or Even"))
    print(StringUtil.get_unique_words("I love palindromes. I really love them"))

if __name__ == "__main__":
    main()