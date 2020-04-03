class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        evensum = sum([x for x in A if x%2==0]) 
        for val,index in queries:
            oldnum = A[index]
            newnum = oldnum + val
            evensum = evensum - (oldnum%2==0)*oldnum + (newnum%2==0)*newnum
            output.append(evensum)
            A[index] = newnum
        return output