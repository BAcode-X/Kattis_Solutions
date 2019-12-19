d,m = [int(_)for _ in input().split()]
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def prt_day(msd):
    a = d % 7
    if msd+a<7:
        print(str(days[(msd+a)-1]))
    else:
        print(str(days[(msd+a)-8]))
if m==1:
    msd=4
    prt_day(msd)
if m==2:
    msd=0
    prt_day(msd)
if m==3:
    msd=0
    prt_day(msd)
if m==4:
    msd=3
    prt_day(msd)
if m==5:
    msd=5
    prt_day(msd)
if m==6:
    msd=1
    prt_day(msd)
if m==7:
    msd=3
    prt_day(msd)
if m==8:
    msd=6
    prt_day(msd)
if m==9:
    msd=2
    prt_day(msd)
if m==10:
    msd=4
    prt_day(msd)
if m==11:
    msd=0
    prt_day(msd)
if m==12:
    msd=2
    prt_day(msd)
