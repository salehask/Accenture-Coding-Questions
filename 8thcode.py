#SumofPrimeIndices

def isPrime(num):
    if num<=1:
        return False
    else:
        for i in range(2,(num//2)+1):
            if num%2==0:
                return False
        return True
def sumPrime(arr,num):
    s=0
    for i in range(0,num):
        if isPrime(i):
            s=s+arr[i]
        return s


arr=list(map(int,input().split()))
num=int(input())
print(sumPrime(arr,num))
