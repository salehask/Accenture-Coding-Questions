def smallest(n):
    next=n+1
    while(True):
        next_str=str(next)
        if len(next_str)>4:
            return -1
        elif len(next_str)==4 and len(next_str)==len(set(next_str)):
           return next
        next+=1
n= int(input())
print(smallest(n))