#VERNAM ENCRYPTION

# Plain text and keyword length must be same
# Ei = (Pi+Ki) mod 26
p = input('Enter plain text: ')
k = input('Enter keyword: ')

p = p.upper()
k = k.upper()

for i in range(len(p)):
    print(chr(((ord(p[i])+ord(k[i])-65-65) %26)+65),end='')
