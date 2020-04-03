class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Return a list of intersections of closed intervals from the input lists

        Args:
        A (list of list): List 1 (each element is a closed interval)
        B (list of list): List 2 (each element is a closed interval)

        Returns:
        intersection (list of list): List with intersections of closed intervals from the original lists
        """
    
        intersection = []
        # attempt 1: unoptimized (two for loops)
        # for a in A:
        #     for b in B:
        #         if((a[0]<=b[1] and b[1]<=a[1]) or (b[0]<=a[1] and a[1]<=b[1])):
        #             intersection.append([max(a[0],b[0]),min(a[1],b[1])])
        
        # attempt 2: optimized (one loop, len(A)+len(B))
        i,j = 0,0
        
        while i < len(A) and j < len(B):
            first = max(A[i][0],B[j][0])
            second = min(A[i][1],B[j][1])
            if(first <= second):
                intersection.append([first,second])
            if(A[i][1]<=B[j][1]):
                i += 1
            else:
                j += 1
        return intersection