# Write a method to replace all spaces i a string with '%20'. You are given the true length of the string.


# O(n), where n is max(l, len(s))
def urlify(s, l):
    url = ''
    count = 0
    for c in s:
        if c == ' ':
            url += '%20'
        else:
            url += c

        count += 1
        if count == l:
            break

    return url


def main():
    print(urlify('Mr John Smith    ', 13))


if __name__ == "__main__":
    main()
