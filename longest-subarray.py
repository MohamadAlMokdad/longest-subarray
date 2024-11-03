def longest_subarray(array):
  max_length=0 # Variable to keep track for the maximum length of the subarray

  for i in range(len(array)):
        count_0=0
        count_1=0
        for j in range(i,len(array)):
            if array[j] ==0:
             count_0+=1 # Increment value of 0s if the element is 0
            else:
             count_1+=1 # Increment value of 1s if the element is 1

            # Check if the counts are equal  
            if count_0==count_1:
               
               # Update max_length if the current subarray length is greater
               max_length=max(max_length,j-i+1)
  return max_length

     

    

   
   