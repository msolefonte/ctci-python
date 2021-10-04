# Implement and algorithm to determine if a string has all unique characters


# O(n), where n is s length
def is_unique(s):
    known_characters = {}

    for char in s:
        if char in known_characters:
            return False
        else:
            known_characters[char] = 1

    return True


# What if you cannot use additional data structures?

# O(n^2), where n is s length
def is_unique_but_slower(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def main():
    print(is_unique('a'))
    print(is_unique('random'))
    print(is_unique('life is great'))
    print(is_unique('1234567890¡qwertyuiopasdfghjklñzxcvbnm,.'))
    print(is_unique('hello'))

    print('*********')

    print(is_unique_but_slower('a'))
    print(is_unique_but_slower('random'))
    print(is_unique_but_slower('life is great'))
    print(is_unique_but_slower('1234567890¡qwertyuiopasdfghjklñzxcvbnm,.'))
    print(is_unique_but_slower('hello'))


if __name__ == "__main__":
    main()
