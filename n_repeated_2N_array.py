class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """In a array A of size 2N, there are N+1 unique elements and exactly one of these elements is repeated N times.
            Return the element repeated N times.

        Args:
            A: target array

        Returns:
            Integer that is repeated N times

        """

        # Using dictionary
        count_dict = dict()
        for i, e in enumerate(A):
            if e in count_dict.keys():
                count_dict[e] += 1
            else:
                count_dict[e] = 1
            if count_dict[e] > 1:
                return e

        # Using set
        # uniq_elements = set()
        # for x in A:
        #     if x in uniq_elements:
        #         return x
        #     else:
        #         uniq_elements.add(x)
