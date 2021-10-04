# There are three types of edits that can be performed on strings: insert a character, remove a character or replace
# a character. Given two strings, write a function to check if they are one edit (or zero edits) away.


# O(n), where n is min(len(string_a), len(string_b))
def are_one_edit_away(string_a, string_b, edit_already_used=False):
    if abs(len(string_a) - len(string_b)) > 1:
        return False

    if len(string_a) == 0 and len(string_b) == 0:
        return True
    if len(string_a) == 0 or len(string_b) == 0:
        return not edit_already_used

    if string_a[0] == string_b[0]:
        return are_one_edit_away(string_a[1:], string_b[1:], edit_already_used)
    else:
        if edit_already_used:
            return False
        else:
            return \
                are_one_edit_away(string_a[1:], string_b[2:], True) or \
                are_one_edit_away(string_a[2:], string_b[1:], True) or \
                are_one_edit_away(string_a[1:], string_b[1:], True)


def main():
    print(are_one_edit_away('Mr John Smith    ', 'potato'))  # False
    print(are_one_edit_away('pot', 'potato'))  # False
    print(are_one_edit_away('pale', 'ple'))  # True
    print(are_one_edit_away('pales', 'pale'))  # True
    print(are_one_edit_away('pale', 'pale'))  # True
    print(are_one_edit_away('pale', 'bale'))  # True
    print(are_one_edit_away('pale', 'bake'))  # False


if __name__ == "__main__":
    main()
