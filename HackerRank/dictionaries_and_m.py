number_of_entries = int(input())
phone_book = {}
for _ in range(number_of_entries):
    entry = input().split(' ')
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone
try:
    entry = input()
    while entry:
        if entry in phone_book.keys():
            print(f"{entry}={phone_book[entry]}")
        else:
            print("Not found")
        entry = input()
except EOFError:
    pass