c, d, e = [int(i) for i in input().split()]
for i in range(1, e + 1, +1):
    if i % c == 0 and i % d == 0:
        print("FizzBuzz")
        continue
    elif i % c == 0:
        print("Fizz")
    elif i % d == 0:
        print("Buzz")
    else:
        print(i)
