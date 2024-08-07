NUMBER = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
NUMBER_DIGIT_2 =  {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
NUMBER_DIGIT_2_1 =  {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}

LEVEL = {0: "", 1: "Thousand", 2: "Million", 3: "Billion"}

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        result = ""
        i = 0
        while num > 0:
            threeDigit = num % 1000
            num //= 1000

            threeDigitWords = self.threeDigitToWords(threeDigit)
            if threeDigitWords != "":
                result = self.threeDigitToWords(threeDigit) + " " + LEVEL[i] + " " + result
            i += 1

        return result.strip()


    def threeDigitToWords(self, num: int) -> str:
        result = ""

        digit1 = num // 100
        digit2 = (num % 100) // 10
        digit3 = num % 10

        # if digit1 == 1:
        #     result += "Hundred "
        if digit1 > 0:
            result += NUMBER[digit1] + " Hundred "

        if digit2 == 1:
            result += NUMBER_DIGIT_2_1[digit3] + " "
        elif digit2 == 0:
            if digit3 > 0:
                result += NUMBER[digit3]
        else:
            result += NUMBER_DIGIT_2[digit2] + " "

            if digit3 > 0:
                result += NUMBER[digit3]

        return result.strip()