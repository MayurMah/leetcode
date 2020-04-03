class Solution:
    def isUnsignedInteger(self, s):
        return len(s) != 0 and s.isdigit()

    def isNonNegativeInteger(self, s):
        if s.find('+') == -1:
            return len(s) != 0 and s.isdigit()
        else:
            return len(s) != 0 and s[1:].isdigit()

    def isInteger(self, s):
        if s.find('-') != -1:
            return self.isNonNegativeInteger(s[1:])
        else:
            return self.isNonNegativeInteger(s)

    def isDecimal(self, s):

        part = s.split(".")
        if len(part) > 2:
            return False
        if len(part[0]) == 0 and len(part[1]) == 0:
            return False
        if not (self.isInteger(part[0]) or part[0] == '+' or part[0] == '-' or len(part[0]) == 0):
            return False
        if not (self.isUnsignedInteger(part[1]) or (len(part[1]) == 0 and part[0] not in ['-', '+'])):
            return False
        return True

    def isSciDecimal(self, s):
        part = s.split("e")

        if len(part) > 2:
            return False

        if part[0].find(".") == -1:
            return self.isInteger(part[0]) and self.isInteger(part[1])
        else:
            return self.isDecimal(part[0]) and self.isInteger(part[1])

    def isNumber(self, s: str) -> bool:
        """Validate is a given string can be interpreted as a decimal number"""

        if len(s) < 1:
            return False

        """
        attempt 1: Using separate functions to identify different types of decimals
        if s.find("e") == -1 and s.find(".") == -1: 
            return self.isInteger(s)
        elif s.find("e") == -1 and s.find(".") != -1:
            return self.isDecimal(s)
        elif s.find("e") != -1:
            return self.isSciDecimal(s)
        else:
            return isInteger(s)
        """

        # attempt 2: DFA Solution

        sign = ['+', '-']

        state = [{},
                 {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                 {'digit': 3, '.': 4},
                 {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
                 {'digit': 5},
                 {'digit': 5, 'e': 6, 'blank': 9},
                 {'sign': 7, 'digit': 8},
                 {'digit': 8},
                 {'digit': 8, 'blank': 9},
                 {'blank': 9}]

        currentState = 1

        for c in s:
            if c.isdigit():
                c = 'digit'
            if c in sign:
                c = 'sign'
            if c == ' ':
                c = 'blank'
            if c not in state[currentState]:
                return False
            currentState = state[currentState][c]

        if currentState not in [3, 5, 8, 9]:
            return False
        return True
