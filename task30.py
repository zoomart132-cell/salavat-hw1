a = int(input())
b = int(input())
print((a + b + (a - b) * (a - b) // (a - b if a != b else 1)) // 2)