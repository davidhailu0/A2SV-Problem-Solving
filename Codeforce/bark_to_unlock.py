password = input()
count_words_known = int(input())
first_letter_exist = False
second_letter_exist = False
for _ in range(count_words_known):
    tried_password = input()
    if tried_password == password:
        print("YES")
        break
    if tried_password[1]==password[0]:
        first_letter_exist = True
    if tried_password[0]==password[1]:
        second_letter_exist = True
if (first_letter_exist and second_letter_exist):
    print("YES")
else:
    print("NO")
