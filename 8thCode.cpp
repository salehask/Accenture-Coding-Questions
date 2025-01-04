#include <iostream>
using namespace std;
int primenum(int num){
    if(num<=1)return 0;
    else{
        for(int i=2;i*i<= num;i++){
            if(num%i==0)return 0;
        }
        return 1;
    }
}

int primeIndices(int arr[],int n){
     int sum=0;
     for(int i=2;i<n;i++){
        if(primenum(i)){
            sum+=arr[i];
            
        }

     }
     return sum;


}
int main(){
    int arr[10]={1,2,3,4,5,6,7,8,9,10};
    int n=10;
    int result=primeIndices(arr,n);
    cout<<result;
}