class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #We want to use a divide and conquer approach to figure out how we would sort these arrays and index to find median 
        #The goal is to not use extra memory i.e. creating a new list 

        #If the combined lenght is odd, we want to take len(n)//2. If even, we would just compute the average of len(n)//2 and len(n)//2 + 1 

        #If len(0), then return None
        #If len(1), then return array[0]
        #If len(2), then return arra[0] + array[1] / 2 

        # Base Cases 
        if len(nums1) == 0 and len(nums2) > 0: 
            if len(nums2) % 2 == 0: 
                return (nums2[len(nums2)//2 -1 ] + nums2[len(nums2)//2])/2.0
            else: 
                return nums2[len(nums2)//2]
            
        if len(nums2) == 0 and len(nums1) > 0: 
            if len(nums1) % 2 == 0: 
                return (nums1[len(nums1)//2 -1 ] + nums1[len(nums1)//2])/2.0
            else: 
                return nums1[len(nums1)//2]
            

        k = len(nums1) + len(nums2) 
        if k % 2 == 0:    
            return (self.kth(nums1, nums2, len(nums1), len(nums2), k//2) + self.kth(nums1, nums2, len(nums1), len(nums2), k//2+1 ))/2.0 
        else:
            return self.kth(nums1, nums2, len(nums1), len(nums2), k//2 + 1 )

    def kth(self, arr1, arr2, n, m, k):
    
        if n == 1 or m == 1:
            if m == 1:
                arr2, arr1 = arr1, arr2
                m = n
            if k == 1:
                return min(arr1[0], arr2[0])
            elif k == m + 1:
                return max(arr1[0], arr2[0])
            else:
                if arr2[k - 1] < arr1[0]:
                    return arr2[k - 1]
                else:
                    return max(arr1[0], arr2[k - 2])
    
        mid1 = (n - 1)//2
        mid2 = (m - 1)//2
    
        if mid1+mid2+1 < k:
            if arr1[mid1] < arr2[mid2]:
                return self.kth(arr1[mid1 + 1:], arr2, n - mid1 - 1, m, k - mid1 - 1)
            else:
                return self.kth(arr1, arr2[mid2 + 1:], n, m - mid2 - 1, k - mid2 - 1)
        else:
            if arr1[mid1] < arr2[mid2]:
                return self.kth(arr1, arr2[:mid2 + 1], n, mid2 + 1, k)
            else:
                return self.kth(arr1[:mid1 + 1], arr2, mid1 + 1, m, k)