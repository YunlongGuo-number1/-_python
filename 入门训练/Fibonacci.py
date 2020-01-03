'''def Fbi(n):
    if (n != 1 and n != 2):
        return (Fbi(n - 1) + Fbi(n - 2))%10007
    else:
        return 1
a = input()
print(Fbi(int(a)))
'''

a = input()
a1  = a2 = a3 =1
for i in range(2, int(a)):
    a3 = (a1 + a2) % 10007
    a1 = a2
    a2 = a3
print(a3)