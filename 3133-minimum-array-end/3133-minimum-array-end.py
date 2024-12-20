class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bit_cnt = len(bin(x)) - 2
        zero_cnt = bin(x).count("0") - 1
        possible_each_n_bit = pow(2, zero_cnt)
        
        n -= 1
        over_bit = n // possible_each_n_bit
        under_bit = n % possible_each_n_bit
        
        bin_x = bin(x)
        over_value = pow(2, bit_cnt) * (over_bit)
        
        bin_under = bin(under_bit)
        j = 0
        under_value = x
        
        for i in range(len(bin_x)):
            if under_bit == 0 or j >= len(bin_under):
                break
            if bin_x[-i-1] == "0":
                if bin_under[-j-1] == "1":
                    under_value += pow(2, i)                
                under_bit -= 1
                j += 1

        return over_value + under_value
        