a,b=map(int,input().split())
def tub(a):
    s=0
    for x in range(2,a):
        if a%x==0:
            s +=1
    if s==0:
        return True
    else:
        return False
if a>0 and b>0 and ((abs(a-b))==2) and tub(a) and tub(b):
    print('yes')
else:
    print('no')



    
