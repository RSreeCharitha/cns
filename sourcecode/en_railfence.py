#RAILFENCE CIPHER
#Plaintext='I am happy today'
#key=3

# i - - - a - - - t - - - y
# - a - h - p - y - o - a -
# - - m - - - p - - - d - -
# Cipher text - iatyahpyoampd

mat = []
p=input('Enter plain text: ')
key = int(input('enter key: '))
p = p.split()
p = ''.join(p)
p = p.upper()
print(p)
for i in range(key):
    mat.append(['-']*len(p))
i=0
j=0
while i<(len(p)):
    if j==key-1:
        while (j!=0):
            mat[j][i]=p[i]
            #print(j,i)
            i+=1
            j-=1
    elif j>=0:
        mat[j][i]=p[i]
        #print(j,i)
        i+=1
        j+=1
'''
for i in range(key):
    for j in range(len(p)):
        print(mat[i][j], end=' ')
    print()
'''
print('Cipher text: ',end='')
for i in range(key):
    for j in range(len(p)):
        if mat[i][j]!='-':
            print(mat[i][j], end='')
