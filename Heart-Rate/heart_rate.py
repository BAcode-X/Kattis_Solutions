a=int(input())
for i in range(a):
    b,c=[float(_) for _ in input().split()]
    BPM=int(b)*(60/c)
    print("%.4f"%(BPM-(60/c)),"%.4f"%BPM,"%.4f"%(BPM+(60/c)))
