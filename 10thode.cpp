#include <iostream>
using namespace std;
int longestSubArray(int arr[],int len){
   
    int maxSeq=1;
    for(int i=0;i<len;i++){
        int maxlen=1;
        int curr=arr[i];
        for(int j=i+1;j<len;j++){
            if(arr[j]>curr){
                curr=arr[j];
                maxlen++;
            }
        }
        if(maxSeq<maxlen){
        maxSeq=maxlen;
    }

    }
    
    return maxSeq;



}
int main(){
    int arr[10]={1,2,3,4,5,6,7,0,1};
    int len =10;
    int result=longestSubArray(arr,len);
    cout<<result;
}