

a16 = input()
a10 = 0

for j in range(len(a16)):
    a10 = a10 * 16 + int('0x' + a16[j], 16)

print(a10)