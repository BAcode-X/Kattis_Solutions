a = input()
A = 0
B = 0
Tie = False
for i in range(0, len(a), 2):
    if a[i] == "A":
        A += int(a[i + 1])
        if Tie and A > B + 1:
            winner = "A"
            break
        elif Tie == False and A >= 11:
            winner = "A"
            break
    elif a[i] == "B":
        B += int(a[i + 1])
        if Tie and B > A + 1:
            winner = "B"
            break
        elif Tie == False and B >= 11:
            winner = "B"
            break
    if A == 10 and B == 10:
        Tie = True
print(winner)
