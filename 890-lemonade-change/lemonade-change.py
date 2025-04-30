class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            match bill:
                case 5:
                    five += 1
                case 10:
                    if five == 0:
                        return False
                    five -= 1
                    ten += 1
                case 20:
                    if ten > 0 and five > 0:
                        ten -= 1
                        five -= 1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False

        return True
