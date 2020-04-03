class Solution:
    def dfs(self,candidates, results, combination, target, start_index):
        
        # print(candidates, results, combination, target, start_index)
        
        if target == 0:
            results.append(combination.copy())
            return
        
        for i in range(start_index,len(candidates)):
            if i!= start_index and candidates[i] == candidates[i-1]:
                continue
            
            current = candidates[i]
            
            if current > target:
                break
            
            combination.append(current)
            self.dfs(candidates,results,combination,target-current,i+1)
            combination.remove(current)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """ Find all unique combinations that sum to target
        
            Args:
                candidates (list): input list of positive integers
                target (int): target sum 
            
            Returns:
                List of unique combinations that sum to target (list of list)
            
        """
        
        results = []
        if len(candidates) < 1:
            return results
        
        candidates = sorted([x for x in candidates if x <= target])
        
        combination = []
        
        self.dfs(candidates, results , combination, target, 0)
        
        return results