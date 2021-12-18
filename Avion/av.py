b = []
for i in range(5):
    a = input()
    if "FBI" in a:
        b.append(f"{i+1}")
if b:
    print(" ".join(b))
else:
    print("HE GOT AWAY!")
