# a = input("Nhap so a: ")

# print(type(a))
# print(a)

#List các số từ 0 dến 5
# a = [5, 2, 9, 1]
# a.sort()
# print(a)

person = {
    "name": "Nguyen Phuc Hoai",
    "age": 30,
    "salary": 500000,
    "address": "Kanagawa"
}

for key, value in person.items():
    print(key, value)