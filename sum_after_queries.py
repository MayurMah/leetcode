class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        """We have an array A of integers, and an array queries of queries.
        For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
        Then, the answer to the i-th query is the sum of the even values of A.

        Args:
            A(list): given array of integers
            queries(list of list of int): List of queries

        Returns:
            Return sum after processing all queries

        """

        output = []
        even_sum = sum([x for x in A if (x%2) == 0])
        
        for val, index in queries:
            old_num = A[index]
            new_num = old_num + val
            even_sum = even_sum - (old_num % 2 == 0) * old_num + (new_num % 2 == 0) * new_num
            output.append(even_sum)
            A[index] = new_num
        return output
