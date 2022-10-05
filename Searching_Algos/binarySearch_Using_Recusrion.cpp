#include<bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int key, int low, int high) {
    if(low <= high) {
        
        //finding the index of middle most element of the array
        int mid = low + (high - low)/2;
        
        //if middle element is the key wwe are trying to find
        if(arr[mid] == key) {
            return mid;
        }
        
        // if mid element is greater than key, then we have to find in first half of the array
        if (arr[mid] > key) {
            return binarySearch(arr, key, low, mid-1);
        }
        
        // else we have to find the key in the second half of the array
        return binarySearch(arr, key, mid+1, high);
        
    }
    
    return -1;
}

int main() {
    
    // for binary search we need sorted array
    int arr[] = {-3,0,1,4,7,9,12,45};
    int size = sizeof(arr)/sizeof(arr[0]);
    int key;
    
    cout<<"Enter element to search : ";
    cin>>key;
    
    int answer = binarySearch(arr,key,0,size-1);
    
    if(answer == -1) {
        cout<<"Entered Key in not in the array!";
    }
    else {
        cout<<"Entered key is present at index "<<answer<<" of the array!";
    }
    
    return 0;
}