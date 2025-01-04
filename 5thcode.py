#sumofLeaders


def sumOfLeaders(arr,n):
    sum=0
    if arr is None:
        return -1
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] > arr[j]:
                    sum+=arr[i]
                   
        sum+=arr[n]
    return sum

if __name__=="__main__":
    arr=list(map(int,input().split(' ')))
    n=int(input())
    result=sumOfLeaders(arr,n)
    print(result)