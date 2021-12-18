for i in range(int(input())):
    c = input()
    p = int(input())
    a = input().split(",")
    a[0] = a[0].replace("[", "")
    a[-1] = a[-1].replace("]", "")
    r = False
    error = False
    reverse = 0
    front = 0
    for j in c:
        if j == "R":
            if r:
                r = False
            else:
                r = True
        elif j == "D":
            if r:
                reverse += 1
            else:
                front += 1
    if error or reverse + front > p:
        print("error")
    else:
        print("[", sep="", end="")
        if r:
            for j in range((len(a) - 1 - reverse), (front - 1), -1):
                if j == (len(a) - reverse - 1):
                    print(a[j], sep="", end="")
                else:
                    print(",", a[j], sep="", end="")
        else:
            for j in range(front, (len(a) - reverse)):
                if j == front:
                    print(a[j], sep="", end="")
                else:
                    print(",", a[j], sep="", end="")
        print("]")
