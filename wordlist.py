import itertools
import time

ism = input('victim name: ')
tugulgan_yil = input('victim birth year: ')
tugulgan_kun = input('victim birth day: ')
nickname = input('victim nicknames: ').split(',')
tel = input('victim phone number: ')
raqami = input('victim fav number: ')

data = [ism, tugulgan_yil, tugulgan_kun, tel, raqami] + nickname

data = [item for item in data if item]

belgilar = ['_', '-', '.']

passwords = set()

min_password_count = 10_000_000

start_time = time.time()

for length in range(1, len(data) + 1):
    for combo in itertools.permutations(data, length):
        passwords.add(''.join(combo))
        if len(passwords) >= min_password_count:
            break
    
    if len(passwords) >= min_password_count:
        break

for length in range(1, len(data) + 1):
    for combo in itertools.permutations(data, length):
        for belgi in belgilar:
            passwords.add(belgi.join(combo))

        if len(passwords) >= min_password_count:
            break

with open('result.txt', 'w') as file:
    for password in sorted(passwords, key=len):
        file.write(password + '\n')

end_time = time.time()
elapsed_time = end_time - start_time

print(f'parollar muvaffaqiatli {elapsed_time: 2f} saqlandi')