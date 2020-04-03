class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        """Return maximum difference between i and j 
        such that i<j and A[i]<A[j] (called as "maximum ramp width")
        
        Args:
        A (list): list of non-negative integers
        
        Returns:
        max_diff(int): maximum ramp width if elements satisfying i<j 
        and A[i]<=A[j] are found else 0 
        """
        
        # return 0 if A is empty
        if(not A):
            return 0
        
        # store the tuples of number, index in array and sort it 
        number_index = [(a,i) for i,a in enumerate(A)]
        number_index.sort()
        
        # iterate over the number_index array
        # maintain the minimum index seen so far 
        # and maximum difference seen so far 
        # return the maximum difference after iteration as max ramp width
        min_index = number_index[0][1]
        max_diff = 0
        for a,i in number_index:
            max_diff = max(max_diff,i-min_index)
            min_index = min(min_index,i)
        
        return max_diff