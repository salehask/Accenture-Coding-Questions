#LeastDifference

def leastDiff(arr,n):
    mini=999999;
    for i in arr:
        diff=abs(i-n)
    if diff < mini:
        mini=diff
        num=i
    return num
if __name__=="__main__":
    arr=list(map(int,input().split(' ')))
    n=int(input())
    result=leastDiff(arr,n)
    print(result)


