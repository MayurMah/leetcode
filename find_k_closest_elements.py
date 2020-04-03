class Solution:
    def calculateDistance(self, arr, x):
        """Find distance between x and all elements in the array

        Args:
            arr(list): given array of integers
            x(int): target element

        Returns:
            Dictionary of distances between x and all elements in the array

        """

        dist_dict = dict()
        for i, y in enumerate(arr):
            dist_dict[i] = abs(x - y)
        return dist_dict

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Find k closest elements to x from an array arr

        Args:
            arr(list): given array of integers
            k(int): number of neighbours
            x(int): target element

        Returns:
            List of k integers closest to x in arr

        """

        # Calculate distances
        dist_dict = self.calculateDistance(arr, x)

        # sort dictionary by distance
        sorted_dict = {k1: v1 for k1, v1 in sorted(dist_dict.items(), key=lambda kv: (kv[1], kv[0]))}

        # select first k indexes from the dictionary
        keys = list(sorted_dict.keys())[0:k]
        lo = min(keys)
        hi = max(keys)
        result = arr[lo:hi + 1]

        if len(result) > k:
            return result[len(result) - k:len(result)]
        return result
