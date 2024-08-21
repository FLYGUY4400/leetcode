class Solution:
    def reverse(self, x: int) -> int:
       x_reverse = str(x)[::-1]
       if x_reverse[len(x_reverse)-1] == "-":

        x_reverse = int(x_reverse[0:len(x_reverse)-1])

        if x_reverse > 2147483647 or x_reverse < -2147483648: 
            return 0 
        else: 
            return 0 - x_reverse 
       else: 
        if int(x_reverse) > 2147483647 or int(x_reverse) < -2147483648:
            return 0
        else: 
            return int(x_reverse)
        