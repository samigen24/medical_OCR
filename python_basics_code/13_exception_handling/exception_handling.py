#
# lst = [int(x) for x in input().split(',')]
# a = []
# print(lst)
# i = int(input("Enter Index: "))
#
#
# try:
#     print(lst[i])
# except Exception as e:
#     print("Index error: ", e)

employees = [
    {"id": 1, "first_name": "Karan ", "middle_name": "Rama ", "last_name": "Reddy"},
    {"id": 2, "first_name": "Alex ", "last_name": "Gorge"},
    {"id": 3, "first_name": "Alice ", "middle_name": "M ", "last_name": "Warner"},
]


for employee in employees:
    try:
        full_name = employee['first_name'] + employee['middle_name'] + employee['last_name']
    except KeyError:
        full_name = employee['first_name'] + employee['last_name']
    finally:
        print(full_name)
