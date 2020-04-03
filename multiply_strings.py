class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """ Return product of two non-negative intgers passed as strings
        
        Args:
            num1 (str): non-negative integer 1 passed as a string
            num2 (str): non-negative integer 2 passed as a string
        
        Returns:
            Product of num1 and num2 as a string
        
        """
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        """
        totalprod = 0
        for i, n1 in enumerate(num1[::-1]):
            innerprod = 0
            carry = 0
            for j, n2 in enumerate(num2[::-1]):
                temp = (int(n1)*int(n2))+carry
                if temp >= 10:
                    carry = temp//10
                else:
                    carry = 0
                if j < len(num2)-1:
                    innerprod += (10**j)*(temp%10)
                else:
                    innerprod += (10**j)*(temp)
            innerprod = (10**i)*innerprod
            totalprod += innerprod
            # print(innerprod,totalprod)
        
        # print(totalprod)
        return str(totalprod)
        """
        
        totalprod = [0]*(len(num1)+len(num2))
        # print("cp1",totalprod)
        ptr  = len(totalprod)-1
        
        for i, n1 in enumerate(num1[::-1]):
            temp_ptr = ptr
            for j, n2 in enumerate(num2[::-1]):
                temp = int(n1)*int(n2)
                totalprod[temp_ptr] += temp                
                totalprod[temp_ptr-1] += totalprod[temp_ptr]//10
                totalprod[temp_ptr] = totalprod[temp_ptr]%10
                
                # print(i,j,ptr,temp_ptr,totalprod)
                temp_ptr -=1 

            ptr -= 1
        
        ptr = 0
        while ptr < len(totalprod) and totalprod[ptr] == 0:
            ptr += 1
        
        result = ''.join(map(str,totalprod[ptr:]))
        # print(result)
        return result