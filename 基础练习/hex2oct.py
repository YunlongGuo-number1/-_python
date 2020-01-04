n = int(input())
a8 = [0 for i in range(n)]

for i in range(n):
    a16 = input()
    a10 = 0
    a8[i] = 0
    for j in range(len(a16)):
        a10 = a10 * 16 + int('0x' + a16[j], 16)
    k = 0
    while (a10):
        a8[i] = a8[i] + a10 % 8 * 10 ** k
        k = k + 1
        a10 = a10 // 8

for k in range(n):
    print(a8[k])