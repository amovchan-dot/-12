# Завдання 6
a6 = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13]
for i in range(5):
    print(a6[i + 5], end=" ")
print()

# Завдання 7
n = int(input())
a7 = [float(input()) for _ in range(n)]
k = 0
for i in range(n - 1):
    if a7[i] > 0 and a7[i + 1] > 0:
        k += 1
print(f"k={k}")

# Завдання 8
a8 = [float(input()) for _ in range(30)]
b8 = [float(input()) for _ in range(30)]
y = 1.0
for i in range(30):
    y *= (a8[i] + b8[29 - i])
print(f"y={y:8.4f}")

# Завдання 9
a9 = [[int(input()) for _ in range(4)] for _ in range(10)]
s = 0
for i in range(10):
    for j in range(4):
        if a9[i][j] % 2 == 0:
            s += a9[i][j]
print(s)