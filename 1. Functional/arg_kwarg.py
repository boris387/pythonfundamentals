# def numbers(*integers):
#     result = 0
#     for x in integers:
#         result += x
#     return result

# def team(**details):
#     for key,value in details.items():
#         return details


# print(team(Name = "FemCode", Project = "Edpresso", Number = "Two Members"))

# print(numbers(1,2,3,4,5,6,7,8,9))


my_dict = {'id': 1,  'name': 'Boris'}

print(my_dict.values())
 
my_dict = {
    'id': 1,
    'name': 'Boris',
    'age': 30,
}

keys = ['name', 'age']

for key in keys:
    if key in my_dict:
        print(f'{key} - {list(my_dict).index(key)}')