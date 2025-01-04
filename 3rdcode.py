def numberOfBalls(arr,n):
 if arr is None:
   return-1
 else:
   sum=0
   for i in range(0,n):
     a_balls = (i+1)
     diff=a_balls-arr[i]  
     sum+=diff
 return sum


if __name__=="__main__":
    arr=list(map(int,input().split(' ')))
    n=int(input())
    result=numberOfBalls(arr,n)
    print(result)