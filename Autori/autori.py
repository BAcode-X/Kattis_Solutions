a=input()
aut=[a[0]]
for i in range(len(a)):
    if a[i]=="-":aut.append(a[i+1])
print(''.join(aut))
