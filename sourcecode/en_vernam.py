#VERNAM ENCRYPTION
# Plain text and keyword length must be same
# For generating key, the given keyword is repeated in a circular manner until it matches the length of the plain text.
# Ei = (Pi + Ki) mod 26
p = input('Enter plain text: ')
k = input('Enter keyword: ')

p = p.upper()
k = k.upper()

l=len(p)
k*=(len(p)//len(k))+1
k = k[:l]
print('Cipher key: ',end='')
for i in range(l):
    print(chr(((ord(p[i])+ord(k[i])-130)%26)+65),end='')
