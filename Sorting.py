def segregateEvenOdd(arr):
    left,right = 0,len(arr)-1
    while left < right:
         while (arr[left]%2==0 and left < right):
            left += 1
         while (arr[right]%2 == 1 and left < right):
            right -= 1
         if (left < right):
             arr[left],arr[right] = arr[right],arr[left]
             left += 1
             right = right-1
arr = [12, 11, 43, 68, 99]
segregateEvenOdd(arr)
print ("Array after segregation "),
for i in range(0,len(arr)):
    print (arr[i],end=" ")

 

            
 


 

 

 
