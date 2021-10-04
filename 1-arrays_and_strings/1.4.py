# Given a string, write a function to check if it is a permutation of a palindrome.


# O(n), where n s length
def palindrome_permutation(s):
    used_characters = {}

    for c in s:
        if c != ' ':
            if c in used_characters:
                used_characters[c] += 1
            else:
                used_characters[c] = 1

    odd_already_used = False
    for key in used_characters:
        if used_characters[key] % 2 == 1:
            if odd_already_used:
                return False
            else:
                odd_already_used = True
    return True


def main():
    print(palindrome_permutation('Mr John Smith    '))
    print(palindrome_permutation('taco cat'))
    print(palindrome_permutation('taco cat   '))


if __name__ == "__main__":
    main()
