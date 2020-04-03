class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Return product of two non-negative integers passed as strings
        
        Args:
            num1 (str): non-negative integer 1 passed as a string
            num2 (str): non-negative integer 2 passed as a string
        
        Returns:
            Product of num1 and num2 as a string
        
        """

        if num1 == "0" or num2 == "0":
            return "0"

        total_prod = [0] * (len(num1) + len(num2))

        ptr = len(total_prod) - 1

        for i, n1 in enumerate(num1[::-1]):
            temp_ptr = ptr
            for j, n2 in enumerate(num2[::-1]):
                temp = int(n1) * int(n2)
                total_prod[temp_ptr] += temp
                total_prod[temp_ptr - 1] += total_prod[temp_ptr] // 10
                total_prod[temp_ptr] = total_prod[temp_ptr] % 10

                # print(i,j,ptr,temp_ptr,total_prod)
                temp_ptr -= 1

            ptr -= 1

        ptr = 0
        while ptr < len(total_prod) and total_prod[ptr] == 0:
            ptr += 1

        result = ''.join(map(str, total_prod[ptr:]))

        return result
