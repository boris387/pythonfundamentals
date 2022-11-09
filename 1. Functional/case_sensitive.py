# Write function that check whether given strings are this same case
# If one of them is not a string nor You can't check its case return -1

# def case_check():
#     myTuple = ("A", "b")
#     c = ",".join(myTuple)1
#     d = c.islower() or c.isupper()
#     return d

# print(case_check())


def case_check(letter1,letter2):

    for letter in range(1):
        if isinstance(letter1, int) or letter1.isdigit():
            return -1
            break
        letter_list = []
        letter_list.append(letter1)

    for letter in range(1):
        if isinstance(letter2, int) or letter2.isdigit():
            return -1
            break
        letter_list2 = []
        letter_list2.append(letter2)

    final_list = letter_list + letter_list2

    for letter in final_list:
        result = letter1.islower() or letter2.isupper()
        return result

print(case_check("a", "b"))

