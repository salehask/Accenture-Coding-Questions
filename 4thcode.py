#MinimumUnfairness
def minUnfairness(arr,k):
    l_diff=float('inf')         #l_diff=0
    for i in range (len(arr)-k+1):
        x=arr[i:i+k:1]
        diff= max(x)-min(x)
        l_diff=min(l_diff,diff)


if __name__=="__main__":
    arr=list(map(int,input().split(' ')))
    n=int(input())
    result=minUnfairness(arr,n)
    print(result)