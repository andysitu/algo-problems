class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative_status = False
        if dividend < 0 and divisor < 0:
            pass
        elif dividend < 0:
            negative_status = True
        elif divisor < 0:
            negative_status = True
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0
        sum = 0 

        if divisor == 1 or divisor == -1:
            count = dividend
        else:
            while True:
                v = divisor << maxi + 1
                if sum + v > dividend:
                    break
                sum += 100 * divisor
                count += 100
            while sum < dividend:
                sum += divisor
                if sum > dividend:
                    break
                count += 1
        if negative_status and  count > 2147483648:
            count = 2147483648
        elif not negative_status and count >2147483647:
            count = 2147483647

        if negative_status:
            return count * -1
        else:
            return count