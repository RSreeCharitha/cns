#!/usr/bin/env python3
t = input('Enter plaintext: ')
k = int(input("Enter Key: "))
c = ''
t = t.lower()
for i in t:
    if i.isalpha():
         cal = ord(i)+k-97
         cal = cal%26
         cal+=97
         c += chr(cal)
    else:
        c+=i

print('Ciphertext:',c.upper())
