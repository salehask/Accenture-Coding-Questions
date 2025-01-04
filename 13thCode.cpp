//you are a givenn an int your task is to find and
// return the smallest 4 digit that is greater than n and unquie
#include<iostream>
#include <set>
#include <string>
using namespace std;
int smallestNum(int n){
    int num=n+1;
    while(true){
        string num_str=to_string(num);
        if(num_str.length()>4)return -1;
        if(num_str.length()==4){
            set<char>digits(num_str.begin(),num_str.end());
            if(digits.size()==4){
                return num;
            }
        }
        num+=1;

    }
}
int main(){
    int n;
    cout<<"Enter"<<endl;
    cin>>n;
    int result=smallestNum(n);
    cout<<result;

}
