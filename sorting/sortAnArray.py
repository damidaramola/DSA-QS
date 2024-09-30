class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # create 2 functions
        # mergeSort and merge
        def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]

            i,j,k = L,0,0

            while j < len(left) and k < len(right):
                if left[l] <= right[r]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i +=1
            
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1

            while k < len(right):
                num[i] = right[k]
                k+=1
                i+=1

        def mergeSort(arr,l,r):
            if l == r:
                return arr 

            m = (l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        return mergeSort(nums,0,len(nums) -1 )
            
        
        
  # TC- O nlog n
  # space - call stack(recursion) - O(n)      