n = int(input())

t = 9 * 60 + n * 45 + (n - 1) // 2 * 5 + n // 2 * 10

print(t // 60, t % 60)