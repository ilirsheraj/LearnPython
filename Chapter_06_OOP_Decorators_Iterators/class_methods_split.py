class StringUtil:
    # Class and static methods together
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)
        # For case-insensitive comparison, lower-case s
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    # The underscore tells us not to call this outside the class
    def _strip_string(s):
        return "".join(c for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

def main():
    print(StringUtil.is_palindrome("A nut for a jar of Tuna"))
    print(StringUtil.is_palindrome("A nut for a jar of Tuna", False))
    print(StringUtil.is_palindrome("A nut for a jar of Beans"))

if __name__ == "__main__":
    main()