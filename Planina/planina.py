s=3
def planina(x):
    if x==1:
        return 3
    else:
        return (planina(x-1)*2)-1
a=int(input())
print(planina(a)**2)
