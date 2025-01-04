
#int fun (a,n):
#fun accept an int arr and size
#replace each num of arr with 1st smaller num on its right

def NextSmallerNum(arr,n):
    for i in range(n):
        next = -1
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                next=arr[j]
                break
        arr[i]=next
    return arr

if __name__=="__main__":
    arr=list(map(int,input().split(' ')))
    n=int(input())
    result=NextSmallerNum(arr,n)
    print(result)