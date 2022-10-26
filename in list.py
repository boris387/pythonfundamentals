food = ["apple", "pizza", "tomatoes", "fish", "cola", "water"]
biedronka = ["test1"]
i = "cola"

# def is_in_list():
#     if pizza in food:
#         print("True")
#     else:
#         print("False")
# print("pizza" in food)

# def is_in_list():
#     if "apple" in food:
#         print("True")
#     else: 
#      print("False")

# x = input("Please enter the name of the item: ")

# def is_in_list():
#     x = x.lower()
#     while True:
#         if x in biedronka:
#             return True
#             break
#         else:
#             return False
#             break
# is_in_list()


def count_values_in_list(_list):
    return len(_list)
    


count = count_values_in_list(_list=biedronka)
print(count)