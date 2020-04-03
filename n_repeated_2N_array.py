class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
#Using dictionary
        count_dict = dict()
        for i,e in enumerate(A):
            if(e in count_dict.keys()):
                count_dict[e] += 1
            else:
                count_dict[e] = 1
            if(count_dict[e]>1):
                return e

# Using set
#        uniq_elements = set()
#        for x in A:
#            if x in uniq_elements:
#                return x
#            else:
#                uniq_elements.add(x)
