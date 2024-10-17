import csv
import json

with open('books.csv', 'r', encoding='utf-8') as f1, \
        open('users.json', 'r', encoding='utf-8') as f2:

    lst_of_books = list(csv.DictReader(f1))
    k_books = len(lst_of_books)
    dct_of_users = json.load(f2)
    k_users = len(list(dct_of_users))
    books_per_user = k_books // k_users
    left_to_give_again = k_books % k_users

for i, user in enumerate(dct_of_users):
    start_index = i * books_per_user
    end_index = start_index + books_per_user
    user_books = lst_of_books[start_index:end_index]
    user['books'] = user_books

for i, user in enumerate(dct_of_users, start=0):
    if left_to_give_again - 1 == i:
        break
    end_index += 1
    user['books'].append(lst_of_books[end_index])

final_res = []

for user in dct_of_users:
    dct = {}
    for info in user:
        if info in ('name', 'gender', 'address', 'age', 'books'):
            dct[info] = user[info]
    final_res.append(dct)

with open('result.json', 'w', encoding='utf-8') as res_file:
    json.dump(final_res, res_file, indent=4)