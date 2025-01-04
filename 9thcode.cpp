#include <iostream>
using namespace std;
int perfectCube(int arr[],int len){
    int count=0;
    
    for(int i=0;i<len;i++){
        int cuberoot=1;
        while(cuberoot*cuberoot*cuberoot<arr[i]){
           cuberoot++;
             }
        if(cuberoot*cuberoot*cuberoot==arr[i]){
            count+=1;
        }
    }
    return count;
}
int main(){
    int arr[6]={1,8,27,125,7,8};
    int len=6;
    int result=perfectCube(arr,len);
    cout<<result;
}