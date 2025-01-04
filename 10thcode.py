#An inc subarray is defined as contiguous subaray where each element is grater than the previous one
def LongestIncreasingSubarray(arr):
    if arr is None:
        return -1
    else:
        curr=1
        maxi=1
        for i in range(1,len(arr)):
            if(arr[i]>arr[i-1]):
                curr+=1
                maxi=max(curr,maxi)
            else:
                curr=1
    return maxi
