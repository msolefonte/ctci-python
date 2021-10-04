# Given two strings, write a method to decide if one is a permutation of the other


# O(n), where n is a length
def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    else:
        for i in range(len(string_a)):
            if string_a[i] != string_b[len(string_b)-1-i]:
                return False
    return True


def main():
    print(check_permutation('hello', 'goodbye'))
    print(check_permutation('aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa'))
    print(check_permutation('arribalabirra', 'arribalabirra'))


if __name__ == "__main__":
    main()
