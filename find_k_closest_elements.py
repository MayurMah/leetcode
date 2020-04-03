class Solution:
    def calculateDistance(self,arr,x):
        dist_dict = dict()
        for i,y in enumerate(arr):
            dist_dict[i] = abs(x-y)
        return dist_dict
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:       
        # find distance between x and all elements of arr 
        # and store in dictionary of {index:distance}
        dist_dict = self.calculateDistance(arr,x)
        
        # sort dictionary by distance  
        #print(dist_dict)
        sorted_dict = {k1:v1 for k1,v1 in sorted(dist_dict.items(),key=lambda kv:(kv[1],kv[0]))}
        
        # select first k indexes from the dictionary
        keys = list(sorted_dict.keys())[0:k]
        lo = min(keys)
        hi = max(keys)
        #print(sorted_dict,lo,hi,len(arr[lo:hi]))
        result = arr[lo:hi+1]
        if(len(result)>k):
            return result[len(result)-k:len(result)]
        return result        
    